﻿using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using Drizzle.Lingo.Runtime.Cast;
using Serilog;

namespace Drizzle.Lingo.Runtime
{
    public partial class LingoRuntime
    {
        private static readonly bool LoadCastParallel = true;

        private static readonly Regex CastPathRegex = new Regex(@"([^_]+)_(\d+)_(.+)?\.([a-z]*)");

        private static readonly string CastPath = Path.Join(MovieBasePath, "Export");

        private readonly Dictionary<string, LingoCastLib>
            _castLibNames = new(StringComparer.InvariantCultureIgnoreCase);

        private readonly LingoCastLib[] _castLibs = new LingoCastLib[5];

        private bool _buildingCast;

        public CastMember? GetCastMember(object nameOrNum, object? cast=null)
        {
            var found = cast switch
            {
                string castName => _castLibNames[castName].GetMember(nameOrNum),
                int castNumber => _castLibs[castNumber - 1].GetMember(nameOrNum),
                null => GetCastMemberAnyCast(nameOrNum),
                _ => throw new ArgumentException("Invalid cast name")
            };

            if (found == null)
                Log.Warning(
                    "Failed to find member with name {MissingMemberName} cast {MissingMemberCast}",
                    nameOrNum, cast);

            return found;
        }

        private CastMember? GetCastMemberAnyCast(object nameOrNum)
        {
            foreach (var castLib in _castLibs)
            {
                var mem = castLib.GetMember(nameOrNum);
                if (mem != null)
                    return mem;
            }

            return null;
        }

        private void LoadCast()
        {
            _buildingCast = true;
            Log.Debug("Loading cast...");

            InitCastLibs();

            var sw = Stopwatch.StartNew();
            var files = Directory.EnumerateFiles(CastPath);

            var count = 0;
            if (LoadCastParallel)
            {
                Parallel.ForEach(files, DoWork);
            }
            else
            {
                foreach (var s in files)
                {
                    DoWork(s);
                }
            }

            void DoWork(string s)
            {
                var member = LoadSingleCastMember(s);
                if (member != null)
                {
                    Interlocked.Increment(ref count);
                    //Log.Debug("Loading cast member: {MemberName} {MemberNum} {MemberCast}",
                    //    member!.name, member.Number, member.Cast);
                }
            }

            _buildingCast = false;
            UpdateNameIndex();

            Log.Debug("Loaded {CastSize} cast members in {Time}", count, sw.Elapsed);
        }

        private void InitCastLibs()
        {
            var i = 0;
            // These offsets make no sense wtf director
            InitLib("Internal", 0);
            InitLib("customMems", 131072);
            InitLib("soundCast", 196608);
            InitLib("levelEditor", 262144);
            InitLib("exportBitmaps", 327680);

            void InitLib(string name, int offset)
            {
                var castLib = new LingoCastLib(this, name, offset);
                _castLibNames.Add(name, castLib);
                _castLibs[i] = castLib;
                i += 1;
            }
        }

        private CastMember? LoadSingleCastMember(string file)
        {
            var fileName = Path.GetFileName(file);
            var match = CastPathRegex.Match(fileName);
            if (!match.Success)
            {
                Log.Warning("Warning: Unable to parse {CastFileName} for cast file name", fileName);
                return null;
            }

            var cast = match.Groups[1].Value;
            var number = int.Parse(match.Groups[2].Value);
            var ext = match.Groups[4].Value;
            string? name = null;

            if (match.Groups[3].Success)
                name = match.Groups[3].Value;

            var member = GetCastMember(number, cast)!;
            member.ImportFile(file, ext, name);

            if (member.Type == CastMemberType.Empty)
                Log.Warning("Warning: unrecognized cast member type {CastFileName}", file);

            return member;
        }

        public void UpdateNameIndex()
        {
            if (_buildingCast)
                return;

            foreach (var castLib in _castLibs)
            {
                castLib.UpdateNameIndex();
            }
        }
    }
}
