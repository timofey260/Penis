using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml.Linq;
using Drizzle.Lingo.Runtime;
using Drizzle.Lingo.Runtime.Parser;
using Drizzle.Lingo.Runtime.Utils;
using Pidgin;

namespace Drizzle.Transpiler;

internal static class Program
{
    public static readonly HashSet<string> MovieScripts = new()
    {
        "testDraw",
        "stop",
        "spelrelaterat",
        "ropeModel",
        "lvl",
        "levelRendering",
        "fiffigt",
        "TEdraw",
        "FILE",
        "comEditorUtils",
        "LSlime",
        "LMats"
    };

    public static readonly HashSet<string> ParentScripts = new()
    {
        "PNG_encode",
        "levelEdit_parentscript"
    };

    private static readonly Dictionary<string, ScriptQuirks> Quirks = new()
    {
        ["fiffigt"] = new ScriptQuirks
        {
            BlackListHandlers = { "giveHitSurf", "cacheloadimage" }
        },
        ["PNG_encode"] = new ScriptQuirks
        {
            BlackListHandlers =
            {
                "png_encode", "writeChunk", "writeBytes", "writeInt", "gzcompress", "writeCRC", "lingo_crc32",
                "bitShift8", "xtraPresent"
            }
        }
    };

    private static readonly Dictionary<string, string> TypeKeywords = new()
    {
        { "point", "LingoPoint" },
        { "rect", "LingoRect" },
        { "list", "LingoList" },
        { "proplist", "LingoPropertyList" },
        { "number", "LingoNumber" },
        { "color", "LingoColor" },
        { "image", "LingoImage" },
        { "member", "CastMember" }
    };

    private const string OutputNamespace = "Drizzle.Ported";

    private static void Main(string[] args)
    {
        CultureFix.FixCulture();

        var drizzleRoot = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        if (drizzleRoot == null)
        {
            throw new Exception("Build environment is not sane. What did you do???");
        }

        drizzleRoot = Path.Combine(drizzleRoot, "..", "..", "..", "..");
        var sourcesRoot = Path.Combine(drizzleRoot, "LingoSource");
        var sourcesDest = Path.Combine(drizzleRoot, "Drizzle.Ported", "Translated");

        if (args.Length == 2)
        {
            sourcesRoot = args[0];
            sourcesDest = args[1];
        }

        var scripts = Directory.GetFiles(sourcesRoot, "*.lingo")
            .AsParallel()
            .Select(n =>
            {
                using var reader = new StreamReader(n);
                var script = LingoParser.Script.Parse(reader);
                if (!script.Success)
                {
                    throw new Exception($"Parsing failed in file {n}\n{script.Error!.RenderErrorMessage()}");
                }

                var name = Path.GetFileNameWithoutExtension(n);
                return (name, script: script.Value);
            })
            .ToDictionary(n => n.name, n => n.script);

        var movieScripts = scripts.Where(kv => MovieScripts.Contains(kv.Key))
            .ToDictionary(kv => kv.Key, kv => kv.Value);
        var parentScripts = scripts.Where(kv => ParentScripts.Contains(kv.Key))
            .ToDictionary(kv => kv.Key, kv => kv.Value);
        var behaviorScripts = scripts.Except(movieScripts).Except(parentScripts)
            .ToDictionary(kv => kv.Key, kv => kv.Value);

        var movieHandlers = movieScripts.Values
            .SelectMany(s => s.Nodes)
            .OfType<AstNode.Handler>()
            .Select(h => h.Name)
            .ToHashSet(StringComparer.InvariantCultureIgnoreCase);

        var globalContext = new GlobalContext(movieHandlers, sourcesDest);

        OutputMovieScripts(movieScripts, globalContext);
        OutputParentScripts(parentScripts, globalContext);
        OutputBehaviorScripts(behaviorScripts, globalContext);

        OutputMovieGlobals(globalContext);


        //recompile_shit(movieScripts, globalContext, "Movie");
        recompile_shit(parentScripts, globalContext, "Parent");
        recompile_shit(behaviorScripts, globalContext, "Behavior");
        //recompile_globals(globalContext);
    }

    private static void recompile_globals(GlobalContext ctx)
    {
        var path = Path.Combine(ctx.SourcesDest, "Movie_globals.py");
        var read = new StreamReader(path);
        string text = read.ReadToEnd();
        read.Close();

        using var file = new StreamWriter(path);
        file.Write(FixText(text));
        file.Close();
    }

    private static void recompile_shit(IEnumerable<KeyValuePair<string, AstNode.Script>> scripts, GlobalContext ctx, string add)
    {
        foreach (var (name, script) in scripts.OrderBy(pair => pair.Key))
        {
            var path = Path.Combine(ctx.SourcesDest, add + $"_{name}.py");
            var read = new StreamReader(path);
            string text = read.ReadToEnd();
            read.Close();

            using var file = new StreamWriter(path);
            file.Write(FixText(text));
        }
    }

    private static string FixText(string text)
    {
        int indent = 0;
        string newtext = "";
        foreach (string line in text.Split('\n'))
        {
            string textindent = String.Concat(Enumerable.Repeat("    ", indent));
            newtext += textindent + line.Replace("{", "").Replace("}", "").Replace("elifif", "elif").Replace("string", "str").Replace("_global", "self._global").Replace("_movieScript", "self._movieScript");
            newtext = Regex.Replace(newtext, @"\)([a-zA-Z_])", $")\n{textindent}$1");
            //newtext = Regex.Replace(newtext, @"LingoSymbol\(""([a-zA-Z0-9]+)""\)", "$1");
            newtext = Regex.Replace(newtext, @"""([a-zA-Z0-9]+)""=", "$1=");
            newtext = Regex.Replace(newtext, @"\bdel\b", "tempdel");
            if (line.Contains('{')) indent++;
            else if (line.Contains('}')) indent--;
        }
        return newtext;
    }

    private static void OutputBehaviorScripts(
        IEnumerable<KeyValuePair<string, AstNode.Script>> scripts,
        GlobalContext ctx)
    {
        foreach (var (name, script) in scripts.OrderBy(pair => pair.Key))
        {
            var path = Path.Combine(ctx.SourcesDest, $"Behavior_{name}.py");
            using var file = new StreamWriter(path);

            OutputSingleBehaviorScript(name, script, file, ctx);
            file.Close();
        }
    }

    private static void OutputSingleBehaviorScript(
        string name,
        AstNode.Script script,
        TextWriter writer,
        GlobalContext ctx)
    {
        WriteFileHeader(writer);
        writer.WriteLine($"#\n# Behavior script: {name}\n#");
        //writer.WriteLine("[BehaviorScript]");
        writer.WriteLine($"class {name}(LingoBehaviorScript): {{");

        EmitScriptBody(name, script, writer, ctx, isMovieScript: false);

        // End class and namespace.
        writer.WriteLine("}\n");
    }

    private static void OutputParentScripts(
        IEnumerable<KeyValuePair<string, AstNode.Script>> scripts,
        GlobalContext ctx)
    {
        foreach (var (name, script) in scripts.OrderBy(pair => pair.Key))
        {
            var path = Path.Combine(ctx.SourcesDest, $"Parent_{name}.py");
            using var file = new StreamWriter(path);

            OutputSingleParentScript(name, script, file, ctx);
            file.Close();
        }
    }

    private static void OutputSingleParentScript(
        string name,
        AstNode.Script script,
        TextWriter writer,
        GlobalContext ctx)
    {
        WriteFileHeader(writer);
        writer.WriteLine($"#\n# Parent script: {name}\n#");
        //writer.WriteLine("[ParentScript]");
        writer.WriteLine($"class {name}(LingoParentScript): {{");

        EmitScriptBody(name, script, writer, ctx, isMovieScript: false);

        // End class and namespace.
        writer.WriteLine("}\n");
    }

    private static void OutputMovieGlobals(GlobalContext ctx)
    {
        var path = Path.Combine(ctx.SourcesDest, "MovieScript.py");
        using var file = new StreamWriter(path, true);

        /*
        WriteFileHeader(file);
        file.WriteLine();
        file.WriteLine($"#\n# Movie globals\n#");
        file.WriteLine("class MovieScript: {");*/

        foreach (var glob in ctx.AllGlobals)
        {
            var type = MapType(glob, ctx.GlobalTypes);
            file.WriteLine($"{glob}: {type} = None");
        }
        
        file.WriteLine("}\n");
        file.Close();
        
        var read = new StreamReader(path);
        string text = read.ReadToEnd();
        read.Close();

        using var file1 = new StreamWriter(path);
        file1.Write(FixText(text));
        file1.WriteLine("""
                @dispatch(LingoGlobal)
                def Init(self, glob: LingoGlobal):
                    super().Init(self, glob)

                def __init__(self):
                    super().__init__()
                    self._imageCache = LruCache(64)

                def cacheloadimage(self, fileName: str):
                    return self._imageCache.Get(fileName, self, lambda state, fileName: state.CacheLoadImageLoad(fileName))

                def CacheLoadImageLoad(self, fileName: str):
                    member = self._global.member("previewImprt")
                    member.importfileinto(fileName)
                    member.name = "previewImprt"
                    return member.image

                def ImageCacheClear(self):
                    self._imageCache.Clear()


            class MovieScriptExt:
                @staticmethod
                def MovieScript(runtime: LingoRuntime):
                    return runtime.MovieScriptInstance
            """); // just to be sure
    }

    private static void OutputMovieScripts(
        IEnumerable<KeyValuePair<string, AstNode.Script>> scripts,
        GlobalContext ctx)
    {
        var path = Path.Combine(ctx.SourcesDest, $"MovieScript.py");
        Directory.CreateDirectory(ctx.SourcesDest);
        using var file = new StreamWriter(path);

        WriteFileHeader(file);
        file.WriteLine("from multipledispatch import dispatch");
        file.WriteLine($"#\n# Movie script\n#");
        file.WriteLine("class MovieScript(LingoScriptBase): {");

        foreach (var (name, script) in scripts.OrderBy(pair => pair.Key))
        {
            OutputSingleMovieScript(name, script, file, ctx);
        }
        //file.Write("}\n");
        file.Close();
    }

    private static void WriteFileHeader(TextWriter writer)
    {
        /*
        writer.WriteLine("using System;");
        writer.WriteLine("using Drizzle.Lingo.Runtime;");
        writer.WriteLine("using Drizzle.Lingo.Runtime.Cast;");
        writer.WriteLine($"namespace {OutputNamespace};");
        */
        // todo
        writer.WriteLine("from Drizzle.Runtime import *");
    }

    private static void OutputSingleMovieScript(
        string name,
        AstNode.Script script,
        TextWriter writer,
        GlobalContext ctx)
    {
        EmitScriptBody(name, script, writer, ctx, isMovieScript: true);

    }

    private static void EmitScriptBody(
        string name,
        AstNode.Script script,
        TextWriter writer,
        GlobalContext ctx,
        bool isMovieScript)
    {
        var allGlobals = script.Nodes.OfType<AstNode.Global>().SelectMany(g => g.Identifiers)
            .ToHashSet(StringComparer.InvariantCultureIgnoreCase);
        var allHandlers = script.Nodes.OfType<AstNode.Handler>().Select(h => h.Name)
            .ToHashSet(StringComparer.InvariantCultureIgnoreCase);
        var scriptContext = new ScriptContext(ctx, allGlobals, allHandlers, isMovieScript);

        ctx.AllGlobals.UnionWith(allGlobals);

        foreach (var globalType in script.Nodes.OfType<AstNode.TypeSpec>())
        {
            ctx.GlobalTypes.Add(globalType.Name, globalType.Type);
        }
        if (!isMovieScript)
        {
            writer.WriteLine("def __init__(self): {");
            writer.WriteLine("super().__init__()");
        }
        
        var props = new HashSet<string>();
        foreach (var prop in script.Nodes.OfType<AstNode.Property>().SelectMany(p => p.Identifiers))
        {
            props.Add(prop);
            if (!isMovieScript)
                writer.WriteLine($"self.{prop} = None");
            // todo
        }
        if (!isMovieScript)
            writer.WriteLine("}");

        var quirks = Quirks.GetValueOrDefault(name);

        foreach (var handler in script.Nodes.OfType<AstNode.Handler>())
        {
            if (quirks?.BlackListHandlers.Contains(handler.Name) ?? false)
                continue;

            // Have to write into a temporary buffer because we need to pre-declare all variables.
            var tempWriter = new StringWriter();
            var handlerContext = new HandlerContext(scriptContext, handler.Name, tempWriter, props);
            handlerContext.Locals.UnionWith(handler.Parameters.Select(k => k.Name));
            handlerContext.Locals.UnionWith(props);

            // Writing statements discovers some property of the code we need to know, like type declarations.
            try
            {
                WriteStatementBlock(handler.Body, handlerContext);
            }
            catch (Exception e)
            {
                Console.WriteLine($"Failed to write handler {handler.Name}:\n{e}");
                writer.WriteLine("raise NotImplementedException(\"Compilation failed\")\n}");
                continue;
            }

            var types = handlerContext.Types;
            foreach (var param in handler.Parameters)
            {
                if (param.Type is { } type)
                    types.Add(param.Name, type);
            }

            var paramsList = handler.Parameters.ToList();
            if (paramsList.Count > 0 && paramsList[0].Name == "me")
                paramsList.RemoveAt(0);
            paramsList.Insert(0, new("self", "me"));

            var paramsText = string.Join(", ", paramsList.Select(p => $"{p.Name.ToLower()}"));
            var handlerLower = handler.Name.ToLower();
            var returnType = MapType("return", types);
            writer.WriteLine($"def {WriteSanitizeIdentifier(handlerLower)}({paramsText}): {{");

            /*
            foreach (var local in handlerContext.DeclaredLocals)
            {
                writer.WriteLine($"{local.ToLower()} = None"); // todo
            }*/

            writer.WriteLine(tempWriter.GetStringBuilder());

            if (handler.Body.Statements.Length == 0 || handler.Body.Statements[^1] is not AstNode.Return)
                writer.WriteLine("return None"); // todo

            // Handler end.
            writer.WriteLine("}");
        }
    }

    private static void WriteStatementBlock(AstNode.StatementBlock node, HandlerContext ctx)
    {
        if (node.Statements.Length == 0) ctx.Writer.WriteLine("pass");
        foreach (var statement in node.Statements)
        {
            WriteStatement(statement, ctx);
        }
    }

    private static void WriteStatement(AstNode.Base node, HandlerContext ctx)
    {
        switch (node)
        {
            case AstNode.Assignment ass:
                WriteAssignment(ass, ctx);
                break;
            case AstNode.Return ret:
                WriteReturn(ret, ctx);
                break;
            case AstNode.ExitRepeat exitRepeat:
                WriteExitRepeat(exitRepeat, ctx);
                break;
            case AstNode.Case @case:
                WriteCase(@case, ctx);
                break;
            case AstNode.RepeatWhile repeatWhile:
                WriteRepeatWhile(repeatWhile, ctx);
                break;
            case AstNode.RepeatWithCounter repeatWithCounter:
                WriteRepeatWithCounter(repeatWithCounter, ctx);
                break;
            case AstNode.RepeatWithList repeatWithList:
                WriteRepeatWithList(repeatWithList, ctx);
                break;
            case AstNode.If @if:
                WriteIf(@if, ctx);
                break;
            case AstNode.PutInto putInto:
                WritePutInto(putInto, ctx);
                break;
            case AstNode.Global global:
                WriteGlobal(global, ctx);
                break;
            case AstNode.Property prop:

                break;
            case AstNode.TypeSpec spec:
                MergeTypeSpec(ctx, spec.Name, spec.Type);
                break;

            default:
                if (node is AstNode.VariableName
                    or AstNode.MemberProp or AstNode.MemberIndex or AstNode.BinaryOperator or AstNode.UnaryOperator
                    or AstNode.String or AstNode.Number or AstNode.Symbol or AstNode.List or
                    AstNode.Property)
                {
                    Console.WriteLine($"Warning: {ctx.Name} has loose expression {node}");
                }

                var exprValue = WriteExpression(node, ctx);
                ctx.Writer.Write(exprValue);
                break;
        }
    }

    private static void MergeTypeSpec(HandlerContext ctx, string name, string? type)
    {
        if (type == null)
            return;

        ref var curType = ref CollectionsMarshal.GetValueRefOrAddDefault(ctx.Types, name, out _);
        if (curType == null)
        {
            curType = type;
        }
        else if (curType != type)
        {
            Console.WriteLine(
                $"Warning: tried to set local variable '{name}' to conflicting types in handler {ctx.Name}");
        }
    }

    private static void WriteGlobal(AstNode.Global node, HandlerContext ctx)
    {
        foreach (var declared in node.Identifiers.Except(ctx.Globals))
        {
            // These get handled when locals are declared.
            /*ctx.DeclaredGlobals.Add(declared);
            ctx.Locals.Add(declared);*/
            ctx.Globals.Add(declared);
            ctx.Parent.Parent.AllGlobals.Add(declared);
        }
    }

    private static void WritePutInto(AstNode.PutInto node, HandlerContext ctx)
    {
        if (node.Type != AstNode.PutType.After)
            throw new NotSupportedException();

        var coll = WriteExpression(node.Collection, ctx);
        var expr = WriteExpression(node.Expression, ctx);
        ctx.Writer.WriteLine($"{coll} += str({expr})");
    }

    private static void WriteIf(AstNode.If node, HandlerContext ctx)
    {
        var exprParams = new ExpressionParams { WantBool = true };
        var cond = WriteExpression(node.Condition, ctx, exprParams);

        ctx.Writer.WriteLine(exprParams.BoolGranted
            ? $"if {cond}: {{"
            : $"if LingoGlobal.ToBool({cond}): {{");

        WriteStatementBlock(node.Statements, ctx);
        ctx.Writer.WriteLine('}');

        if (node.Else != null && node.Else.Statements.Length > 0)
        {
            var elseIf = node.Else.Statements.Length == 1 && node.Else.Statements[0] is AstNode.If;


            ctx.Writer.Write(elseIf ? "elif" : "else:");
            // If the else clause is another if it's an else-if chain
            // and we forego the braces around the else.
            if (!elseIf)
                ctx.Writer.WriteLine('{');

            WriteStatementBlock(node.Else, ctx);
            if (!elseIf)
                ctx.Writer.WriteLine('}');
        }
    }

    private static void WriteRepeatWithList(AstNode.RepeatWithList node, HandlerContext ctx)
    {
        var expr = WriteExpression(node.ListExpr, ctx);
        var name = node.Variable;
        var loopTmp = $"tmp_{name}";
        ctx.Writer.WriteLine($"for {loopTmp} in {expr}: {{");

        MakeLoopTmp(ctx, name, loopTmp, number: false);
        WriteStatementBlock(node.Block, ctx);

        ctx.Writer.WriteLine("}");
    }

    private static void WriteRepeatWithCounter(AstNode.RepeatWithCounter node, HandlerContext ctx)
    {
        var start = WriteExpression(node.Start, ctx);
        var end = WriteExpression(node.Finish, ctx);
        var name = node.Variable;
        var loopTmp = $"tmp_{name}";

        ctx.Writer.WriteLine($"{loopTmp} = {start}");
        ctx.Writer.WriteLine($"while {loopTmp} < {end}: {{");

        MakeLoopTmp(ctx, name, $"{loopTmp}", number: true); // todo
        WriteStatementBlock(node.Block, ctx);

        ctx.Writer.WriteLine($"{loopTmp} = {WriteVariableNameCore(name, ctx)}");
        ctx.Writer.WriteLine($"{loopTmp} += LingoNumber(1)");
        ctx.Writer.WriteLine("}");

        // ctx.LoopTempIdx--;
    }

    private static void MakeLoopTmp(HandlerContext ctx, string name, string loopTmp, bool number)
    {
        if (!IsGlobal(name, ctx, out _) && ctx.Locals.Add(name))
        {
            ctx.DeclaredLocals.Add(name);
            if (number)
                MergeTypeSpec(ctx, name, "number");
        }

        ctx.Writer.WriteLine($"{WriteVariableNameCore(name, ctx)} = {loopTmp}");
    }

    private static void WriteRepeatWhile(AstNode.RepeatWhile node, HandlerContext ctx)
    {
        var exprParams = new ExpressionParams { WantBool = true };
        var expr = WriteExpression(node.Condition, ctx);

        ctx.Writer.WriteLine(exprParams.BoolGranted
            ? $"while {expr}: {{"
            : $"while LingoGlobal.ToBool({expr}): {{");

        WriteStatementBlock(node.Block, ctx);

        ctx.Writer.WriteLine('}');
    }

    private static void WriteCase(AstNode.Case node, HandlerContext ctx)
    {
        // Check if all expressions are literal.
        // If so we can translate it as a switch statement.
        var literals = node.Cases.SelectMany(c => c.exprs).All(e => e is AstNode.Constant or AstNode.String);

        var allInts = node.Cases.All(c => c.exprs.All(e => e is AstNode.Number { Value: { IsDecimal: false } }));
        literals |= allInts;

        if (literals)
        {
            ctx.Writer.Write("match ");
            /*
            if (allInts)
                ctx.Writer.Write("(int?)");*/
            ctx.Writer.Write(WriteExpression(node.Expression, ctx));
            // If this is a string switch, .ToLower() it and switch on lowercase values.
            // to avoid any case problems.
            if (node.Cases.Length > 0 && node.Cases[0].exprs[0] is AstNode.String)
                ctx.Writer.Write(".lower()");
            else if (allInts)
            {
                // Handle null int value in switch case.
                // I'm gonna assume Joar never felt like using int.MaxValue anywhere.
                ctx.Writer.Write(" if "); // todo
                ctx.Writer.Write(WriteExpression(node.Expression, ctx));
                ctx.Writer.Write(" is not None else 9999999999");
            }

            ctx.Writer.WriteLine(": {");

            foreach ((AstNode.Base[] exprs, AstNode.StatementBlock block) in node.Cases)
            {
                bool first = true;
                foreach (var expr in exprs)
                {
                    bool last = expr == exprs.Last();
                    ctx.Writer.Write(first ? "case " : " | ");
                    first = false;
                    if (expr is AstNode.String str)
                        ctx.Writer.Write(DoWriteString(str.Value.ToLowerInvariant()));
                    else if (expr is AstNode.Number num)
                    {
                        Debug.Assert(allInts);
                        ctx.Writer.Write(num.Value.ToString());
                    }
                    else
                        ctx.Writer.Write(WriteExpression(expr, ctx));
                    if (last)
                        ctx.Writer.WriteLine(":{");
                }

                WriteStatementBlock(block, ctx);

                //ctx.Writer.WriteLine("break");
                ctx.Writer.WriteLine('}');
            }

            if (node.Otherwise != null)
            {
                ctx.Writer.WriteLine("case _: {");
                WriteStatementBlock(node.Otherwise, ctx);
                //ctx.Writer.WriteLine("break");
                ctx.Writer.WriteLine("}");
            }

            ctx.Writer.WriteLine("}");
        }
        else
        {
            // Will have to be translated as if-else chain.
            // If you run into this again: "var: type = value" syntax is erroneously parsed as a switch case.
            // So make sure you didn't do that lol.
            throw new NotImplementedException();
        }
    }

    private static void WriteExitRepeat(AstNode.ExitRepeat node, HandlerContext ctx)
    {
        ctx.Writer.WriteLine("break");
    }

    private static void WriteReturn(AstNode.Return ret, HandlerContext ctx)
    {
        if (ret.Value != null)
        {
            var value = WriteExpression(ret.Value, ctx);
            ctx.Writer.WriteLine($"return {value}");
        }
        else
        {
            ctx.Writer.WriteLine($"return None"); // todo
        }
    }

    private static void WriteAssignment(AstNode.Assignment node, HandlerContext ctx)
    {
        if (node.Assigned is AstNode.VariableName simpleTarget)
        {
            var name = simpleTarget.Name.ToLower();
            // Define local variable if necessary.
            if (!IsGlobal(name, ctx, out _))
            {
                // Local variable, not global
                // Make sure it's not a parameter though.
                if (ctx.Locals.Add(name))
                    ctx.DeclaredLocals.Add(name);

                MergeTypeSpec(ctx, name, node.Type);
            }
            else if (node.Type != null)
            {
                Console.WriteLine($"Trying to assign-declare type on global: {node.Type}, {node.Assigned}");
            }
        }
        else if (node.Type != null)
        {
            Console.WriteLine($"Unable to infer variable name of assignment type: {node.Type}, {node.Assigned}");
        }

        var lhs = WriteExpression(node.Assigned, ctx);
        var rhs = WriteExpression(node.Value, ctx);
        ctx.Writer.WriteLine($"{lhs} = {rhs}");
    }

    private static string WriteExpression(AstNode.Base node, HandlerContext ctx, ExpressionParams? param = null)
    {
        return node switch
        {
            // Turn pxl member access into a static lookup.
            AstNode.MemberProp
            {
                Property: "image",
                Expression: AstNode.GlobalCall { Name: "member", Arguments: [AstNode.String { Value: "pxl" }] }
            } => "LingoImage.Pxl",
            // Special case concat binary operators for chaining.
            AstNode.BinaryOperator
            {
                Type: AstNode.BinaryOperatorType.Concat or AstNode.BinaryOperatorType.ConcatSpace
            } concatOperator => WriteConcatOperator(concatOperator, ctx),
            AstNode.BinaryOperator binaryOperator => WriteBinaryOperator(binaryOperator, ctx, param),
            AstNode.Constant constant => WriteConstant(constant, ctx),
            AstNode.Number number => WriteNumber(number, ctx),
            AstNode.GlobalCall globalCall => WriteGlobalCall(globalCall, ctx),
            AstNode.List list => WriteList(list, ctx),
            AstNode.MemberCall memberCall => WriteMemberCall(memberCall, ctx),
            AstNode.MemberIndex memberIndex => WriteMemberIndex(memberIndex, ctx),
            AstNode.MemberProp memberProp => WriteMemberProp(memberProp, ctx),
            AstNode.MemberSlice memberSlice => WriteMemberSlice(memberSlice, ctx),
            AstNode.NewCastLib newCastLib => WriteNewCastLib(newCastLib, ctx),
            AstNode.NewScript newScript => WriteNewScript(newScript, ctx),
            AstNode.PropertyList propertyList => WritePropertyList(propertyList, ctx),
            AstNode.String str => WriteString(str, ctx),
            AstNode.Symbol symbol => WriteSymbol(symbol, ctx),
            AstNode.The the => WriteThe(the, ctx),
            AstNode.TheNumberOf theNumberOf => WriteTheNumberOf(theNumberOf, ctx),
            AstNode.TheNumberOfLines theNumberOfLines => WriteTheNumberOfLines(theNumberOfLines, ctx),
            AstNode.ThingOf thingOf => WriteThingOf(thingOf, ctx),
            AstNode.UnaryOperator unaryOperator => WriteUnaryOperator(unaryOperator, ctx, param),
            AstNode.VariableName variableName => WriteVariableName(variableName, ctx),
            _ => throw new NotSupportedException($"{node.GetType()} is not a supported expression type")
        };
    }

    private static string WriteConcatOperator(AstNode.BinaryOperator node, HandlerContext ctx)
    {
        // Flatten recursive chain of concat operators to a straight list.
        var expressions = new List<AstNode.Base> { node.Right };
        var lhs = node.Left;
        while (lhs is AstNode.BinaryOperator binOp && binOp.Type == node.Type)
        {
            expressions.Add(binOp.Right);
            lhs = binOp.Left;
        }

        expressions.Add(lhs);

        expressions.Reverse();

        var func = node.Type switch
        {
            AstNode.BinaryOperatorType.ConcatSpace => "concat_space",
            AstNode.BinaryOperatorType.Concat => "concat",
            _ => throw new ArgumentOutOfRangeException()
        };

        return WriteGlobalCall(func, ctx, expressions.ToArray());
    }

    private static string WriteThingOf(AstNode.ThingOf thingOf, HandlerContext ctx)
    {
        var helper = thingOf.Type switch
        {
            AstNode.ThingOfType.Item => "itemof_helper",
            AstNode.ThingOfType.Line => "lineof_helper",
            AstNode.ThingOfType.Char => "charof_helper",
            _ => throw new ArgumentOutOfRangeException()
        };

        return WriteGlobalCall(helper, ctx, thingOf.Index, thingOf.Collection);
    }

    private static string WriteTheNumberOfLines(AstNode.TheNumberOfLines node, HandlerContext ctx)
    {
        return WriteGlobalCall("thenumberoflines_helper", ctx, node.Text);
    }

    private static string WriteTheNumberOf(AstNode.TheNumberOf node, HandlerContext ctx)
    {
        return WriteGlobalCall("thenumberof_helper", ctx, node.Expr);
    }

    private static string WriteThe(AstNode.The node, HandlerContext ctx)
    {
        return $"_global.the_{node.Name}";
    }

    private static string WritePropertyList(AstNode.PropertyList node, HandlerContext ctx)
    {
        if (node.Values.Length == 0)
            return "LingoPropertyList()";

        var sb = new StringBuilder();
        sb.Append("LingoPropertyList("); // todo
        var first = true;
        foreach (var (k, v) in node.Values)
        {
            if (!first)
                sb.Append(',');

            first = false;
            var kExpr = WriteExpression(k, ctx);
            var vExpr = WriteExpression(v, ctx);
            //sb.Append('[');
            sb.Append(kExpr);
            //sb.Append("] = ");
            sb.Append(", ");
            sb.Append(vExpr); // todo
        }

        sb.Append(")");

        return sb.ToString();
    }

    private static string WriteVariableName(AstNode.VariableName variableName, HandlerContext ctx)
    {
        return WriteVariableNameCore(variableName.Name, ctx);
    }

    private static string WriteVariableNameCore(string name, HandlerContext ctx)
    {
        var lowered = name.ToLower();

        if (lowered == "me")
            return "self";

        if (ctx.Locals.Contains(lowered))
            return lowered;

        if (IsGlobal(name, ctx, out var casedName))
            return $"{MovieScriptPrefix(ctx)}{casedName}";

        return $"_global.{name}";
    }

    private static bool IsGlobal(string name, HandlerContext ctx, [NotNullWhen(true)] out string? caseName)
    {
        if (!ctx.Parent.AllGlobals.Contains(name) && !ctx.Globals.Contains(name))
        {
            caseName = null;
            return false;
        }

        if (!ctx.Parent.Parent.AllGlobals.TryGetValue(name, out caseName))
            throw new InvalidOperationException("Global declared but not in all globals list?");

        return true;
    }

    private static string WriteUnaryOperator(
        AstNode.UnaryOperator unaryOperator,
        HandlerContext ctx,
        ExpressionParams? exprParams)
    {
        if (unaryOperator.Type == AstNode.UnaryOperatorType.Not)
        {
            var subParams = new ExpressionParams { WantBool = true };
            var expr = WriteExpression(unaryOperator.Expression, ctx, subParams);

            var sb = new StringBuilder();

            sb.Append(expr);

            if (!subParams.BoolGranted)
            {
                sb.Insert(0, "LingoGlobal.ToBool(");
                sb.Append(')');
            }

            sb.Insert(0, "not ");

            if (exprParams is not { WantBool: true })
            {
                sb.Insert(0, "(1 if ");
                sb.Append(" else 0)");
            }
            else
            {
                exprParams.BoolGranted = true;
            }


            return sb.ToString();
        }
        else
        {
            Debug.Assert(unaryOperator.Type == AstNode.UnaryOperatorType.Negate);
            var expr = WriteExpression(unaryOperator.Expression, ctx);

            return $"-{expr}";
        }
    }

    private static string WriteSymbol(AstNode.Symbol node, HandlerContext ctx)
    {
        return $"LingoSymbol(\"{node.Value}\")";
    }

    private static string WriteString(AstNode.String node, HandlerContext ctx)
    {
        return DoWriteString(node.Value);
    }

    private static string DoWriteString(string str)
    {
        var escaped = str.Replace("\"", "\"\"");
        return $"\"{escaped}\""; // todo
    }

    private static string WriteNewScript(AstNode.NewScript node, HandlerContext ctx)
    {
        var wrapListNode = new AstNode.List(node.Args);
        return WriteGlobalCall("new_script", ctx, node.Type, wrapListNode);
    }

    private static string WriteNewCastLib(AstNode.NewCastLib node, HandlerContext ctx)
    {
        return WriteGlobalCall("new_castlib", ctx, node.Type, node.CastLib);
    }

    private static string WriteMemberSlice(AstNode.MemberSlice node, HandlerContext ctx)
    {
        return WriteGlobalCall("slice_helper", ctx, node.Expression, node.Start, node.End);
    }

    private static string WriteMemberProp(AstNode.MemberProp node, HandlerContext ctx)
    {
        if (node.Property == "char")
            return WriteGlobalCall("charmember_helper", ctx, node.Expression);
        if (node.Property == "line")
            return WriteGlobalCall("linemember_helper", ctx, node.Expression);
        if (node.Property == "length")
            return WriteGlobalCall("lengthmember_helper", ctx, node.Expression);

        var child = WriteExpression(node.Expression, ctx);
        string thing = ctx.Properties.Contains(child) ? "self." : "";
        return $"{thing}{child}.{WriteSanitizeIdentifier(node.Property.ToLower())}";
    }

    private static string WriteMemberIndex(AstNode.MemberIndex node, HandlerContext ctx)
    {
        var child = WriteExpression(node.Expression, ctx);
        var idx = WriteExpression(node.Index, ctx);
        string thing = ctx.Properties.Contains(child) ? "self." : "";
        return $"{thing}{child}[{idx}]";
    }

    private static string WriteMemberCall(AstNode.MemberCall node, HandlerContext ctx)
    {
        var child = WriteExpression(node.Expression, ctx);
        var args = node.Parameters.Select(v => WriteExpression(v, ctx));
        var name = WriteSanitizeIdentifier(node.Name.ToLower());
        string thing = ctx.Properties.Contains(child) ? "self." : "";
        return $"{thing}{child}.{name}({string.Join(',', args)})";
    }

    private static string WriteList(AstNode.List node, HandlerContext ctx)
    {
        if (node.Values.Length == 0)
            return "LingoList()";

        var args = node.Values.Select(v => WriteExpression(v, ctx));
        return $"LingoList({string.Join(',', args)})";
    }

    private static string MovieScriptPrefix(HandlerContext ctx)
    {
        return ctx.Parent.IsMovieScript ? "self." : "_movieScript.";
    }

    private static string WriteNumber(AstNode.Number node, HandlerContext ctx)
    {
        return $"LingoNumber({node.Value})";
    }

    private static string WriteConstant(AstNode.Constant node, HandlerContext ctx)
    {
        if (node.Name.Equals("None", StringComparison.InvariantCultureIgnoreCase))
            return "null";

        return $"LingoGlobal.{node.Name.ToUpper()}";
    }

    private static string WriteBinaryOperator(
        AstNode.BinaryOperator node,
        HandlerContext ctx,
        ExpressionParams? param)
    {
        if (param?.WantBool ?? false)
        {
            if (node.Type is AstNode.BinaryOperatorType.Or or AstNode.BinaryOperatorType.And or AstNode
                    .BinaryOperatorType.Sor or AstNode.BinaryOperatorType.Sand)
            {
                return WriteBinaryBoolOp(node, ctx, param);
            }

            if (node.Type is >= AstNode.BinaryOperatorType.LessThan and <= AstNode.BinaryOperatorType
                    .GreaterThanOrEqual)
            {
                return WriteComparisonBoolOp(node, ctx, param);
            }
        }

        // Operators that need to map to special functions.
        var helperOps = node.Type switch
        {
            AstNode.BinaryOperatorType.Contains => "contains",
            AstNode.BinaryOperatorType.Starts => "starts",
            AstNode.BinaryOperatorType.LessThan => "op_lt",
            AstNode.BinaryOperatorType.LessThanOrEqual => "op_le",
            AstNode.BinaryOperatorType.NotEqual => "op_ne",
            AstNode.BinaryOperatorType.Equal => "op_eq",
            AstNode.BinaryOperatorType.GreaterThan => "op_gt",
            AstNode.BinaryOperatorType.GreaterThanOrEqual => "op_ge",
            AstNode.BinaryOperatorType.And => "op_and",
            AstNode.BinaryOperatorType.Or => "op_or",
            AstNode.BinaryOperatorType.Sand => "op_sand",
            AstNode.BinaryOperatorType.Sor => "op_sor",
            AstNode.BinaryOperatorType.Add => "op_add",
            AstNode.BinaryOperatorType.Subtract => "op_sub",
            AstNode.BinaryOperatorType.Multiply => "op_mul",
            AstNode.BinaryOperatorType.Divide => "op_div",
            AstNode.BinaryOperatorType.Mod => "op_mod",
            _ => throw new ArgumentOutOfRangeException()
        };

        return WriteGlobalCall(helperOps, ctx, node.Left, node.Right);
    }

    private static string WriteComparisonBoolOp(
        AstNode.BinaryOperator node,
        HandlerContext ctx,
        ExpressionParams expressionParams)
    {
        var exprLeft = WriteExpression(node.Left, ctx);
        var exprRight = WriteExpression(node.Right, ctx);

        expressionParams.BoolGranted = true;

        return node.Type switch
        {
            // Use non-short-circuiting ops.
            AstNode.BinaryOperatorType.LessThan => $"{exprLeft} < {exprRight}",
            AstNode.BinaryOperatorType.LessThanOrEqual => $"{exprLeft} <= {exprRight}",
            AstNode.BinaryOperatorType.GreaterThanOrEqual => $"{exprLeft} >= {exprRight}",
            AstNode.BinaryOperatorType.GreaterThan => $"{exprLeft} > {exprRight}",
            AstNode.BinaryOperatorType.Equal => $"LingoGlobal.op_eq_b({exprLeft}, {exprRight})",
            AstNode.BinaryOperatorType.NotEqual => $"LingoGlobal.op_ne_b({exprLeft}, {exprRight})",
            _ => throw new ArgumentOutOfRangeException()
        };
    }

    private static string WriteBinaryBoolOp(
        AstNode.BinaryOperator node,
        HandlerContext ctx,
        ExpressionParams expressionParams)
    {
        var exprParamLeft = new ExpressionParams { WantBool = true };
        var exprParamRight = new ExpressionParams { WantBool = true };

        var exprLeft = WriteExpression(node.Left, ctx, exprParamLeft);
        var exprRight = WriteExpression(node.Right, ctx, exprParamRight);

        if (!exprParamLeft.BoolGranted)
            exprLeft = $"LingoGlobal.ToBool({exprLeft})";

        if (!exprParamRight.BoolGranted)
            exprRight = $"LingoGlobal.ToBool({exprRight})";

        var op = node.Type switch
        {
            AstNode.BinaryOperatorType.And => "and",
            AstNode.BinaryOperatorType.Or => "or",
            AstNode.BinaryOperatorType.Sand => "and",
            AstNode.BinaryOperatorType.Sor => "or",
            _ => throw new ArgumentOutOfRangeException()
        };

        expressionParams.BoolGranted = true;

        return $"({exprLeft} {op} {exprRight})";
    }

    private static string WriteGlobalCall(AstNode.GlobalCall node, HandlerContext ctx)
    {
        var args = node.Arguments.Select(a => WriteExpression(a, ctx));
        var lower = node.Name.ToLower();
        if (ctx.Parent.AllHandlers.Contains(lower))
        {
            // Local call
            return $"self.{lower}({string.Join(',', args)})";
        }

        if (ctx.Parent.Parent.MovieHandlers.Contains(node.Name))
        {
            // Movie script call
            return $"{MovieScriptPrefix(ctx)}{lower}({string.Join(',', args)})";
        }

        return WriteGlobalCall(lower, ctx, args);
    }

    private static string WriteGlobalCall(string name, HandlerContext ctx, params AstNode.Base[] args)
    {
        return WriteGlobalCall(name, ctx, args.Select(a => WriteExpression(a, ctx)));
    }

    private static string WriteGlobalCall(string name, HandlerContext ctx, IEnumerable<string> args)
    {
        var method = typeof(LingoGlobal).GetMember(name,
            BindingFlags.IgnoreCase | BindingFlags.Public | BindingFlags.Static | BindingFlags.Instance);

        var isStatic = method.Any(m => m is MethodInfo { IsStatic: true });

        var sb = new StringBuilder();

        sb.Append(isStatic ? "LingoGlobal." : "_global.");
        sb.Append(WriteSanitizeIdentifier(name.ToLower()));
        sb.Append('(');
        sb.Append(string.Join(',', args));
        sb.Append(')');

        return sb.ToString();
    }

    private static readonly HashSet<string> CSharpKeyWords = new HashSet<string>
    {
        "new",
        "str",
        "float"
    };

    private static string WriteSanitizeIdentifier(string identifier)
    {
        return CSharpKeyWords.Contains(identifier) ? $"{identifier}" : identifier; // todo
    }

    private static string MapType(string variable, Dictionary<string, string> types)
    {
        var type = types.GetValueOrDefault(variable, "...");
        return TypeKeywords.GetValueOrDefault(type, type);
    }

    private sealed class GlobalContext
    {
        public GlobalContext(HashSet<string> movieHandlers, string sourcesDest)
        {
            MovieHandlers = movieHandlers;
            SourcesDest = sourcesDest;
        }

        public HashSet<string> AllGlobals { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public Dictionary<string, string> GlobalTypes { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public HashSet<string> MovieHandlers { get; }
        public string SourcesDest { get; }
    }

    private sealed class ScriptContext
    {
        public GlobalContext Parent { get; }
        public HashSet<string> AllGlobals { get; }
        public HashSet<string> AllHandlers { get; }
        public bool IsMovieScript { get; }


        public ScriptContext(
            GlobalContext parent,
            HashSet<string> allGlobals,
            HashSet<string> allHandlers,
            bool isMovieScript)
        {
            Parent = parent;
            AllGlobals = allGlobals;
            AllHandlers = allHandlers;
            IsMovieScript = isMovieScript;
        }
    }

    private sealed class HandlerContext
    {
        public HandlerContext(ScriptContext parent, string name, TextWriter writer, HashSet<string> props)
        {
            Parent = parent;
            Name = name;
            Writer = writer;
            Properties = props;
        }
        public HashSet<string> Properties { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public HashSet<string> Globals { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public HashSet<string> Locals { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public HashSet<string> DeclaredLocals { get; } = new(StringComparer.InvariantCultureIgnoreCase);
        public readonly Dictionary<string, string> Types = new(StringComparer.InvariantCultureIgnoreCase);
        public ScriptContext Parent { get; }
        public string Name { get; }
        public TextWriter Writer { get; }
    }

    private sealed class ScriptQuirks
    {
        public readonly HashSet<string> BlackListHandlers = new(StringComparer.InvariantCultureIgnoreCase);
    }

    private sealed class ExpressionParams
    {
        public bool WantBool;
        public bool BoolGranted;
    }
}
