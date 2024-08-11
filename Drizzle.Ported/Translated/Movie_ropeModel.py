from Drizzle.Runtime import *## Movie script: ropeModel#class MovieScript:     def __init__(self):         super().__init__()            def resetropemodel(self, pa, pb, prop, lengthfac, lr, rel):         numberofsegments = None        step = None        i = None        self.ropeModel = LingoPropertyList(dict(posa = pa,posb = pb,segmentlength = prop.segmentlength,grav = prop.grav,stiff = prop.stiff,release = rel,segments = LingoList(),friction = prop.friction,airfric = prop.airfric,layer = lr,segrad = prop.segrad,rigid = prop.rigid,edgedirection = prop.edgedirection,selfpush = prop.selfpush,sourcePush = prop.sourcepush))        numberofsegments = LingoGlobal.op_mul(LingoGlobal.op_div(self.diag(pa,pb),prop.segmentlength),lengthfac)        if numberofsegments < LingoNumber(3):             numberofsegments = LingoNumber(3)                    step = LingoGlobal.op_div(self.diag(pa,pb),numberofsegments)        for tmp_i in LingoGlobal.pyrange(LingoNumber(1), numberofsegments):             i = tmp_i            self.ropeModel.segments.add(LingoPropertyList(dict(pos = LingoGlobal.op_add(pa,self.movetopoint(pa,pb,LingoGlobal.op_mul(LingoGlobal.op_sub(i,LingoNumber(0.5000)),step))),lastpos = LingoGlobal.op_add(pa,self.movetopoint(pa,pb,LingoGlobal.op_mul(LingoGlobal.op_sub(i,LingoNumber(0.5000)),step))),vel = LingoGlobal.point(LingoNumber(0),LingoNumber(0)))))
            tmp_i = i                            return None            def modelropeupdate(self, preview, camerapos, previewscale):         dir = None        a = None        fac = None        idealfirstpos = None        a1 = None        i = None        b = None        dist = None        mov = None        adaptedpos = None        if self.ropeModel.edgedirection > LingoNumber(0):             dir = self.movetopoint(self.ropeModel.posa,self.ropeModel.posb,LingoNumber(1.0000))            if self.ropeModel.release > -LingoNumber(1):                 for tmp_A in LingoGlobal.pyrange(LingoNumber(1), LingoGlobal.op_div(self.ropeModel.segments.count,LingoNumber(2))):                     a = tmp_A                    fac = LingoGlobal.power(LingoGlobal.op_sub(LingoNumber(1.0000),LingoGlobal.op_div(LingoGlobal.op_sub(a.float,LingoNumber(1.0000)),LingoGlobal.op_div(self.ropeModel.segments.count,LingoNumber(2)))),LingoNumber(2))                    self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(LingoGlobal.op_mul(dir,fac),self.ropeModel.edgedirection))                    tmp_A = a                                    idealfirstpos = LingoGlobal.op_add(self.ropeModel.posa,LingoGlobal.op_mul(dir,self.ropeModel.segmentlength))                self.ropeModel.segments[LingoNumber(1)].pos = LingoGlobal.point(self.lerp(self.ropeModel.segments[LingoNumber(1)].pos.loch,idealfirstpos.loch,self.ropeModel.edgedirection),self.lerp(self.ropeModel.segments[LingoNumber(1)].pos.locv,idealfirstpos.locv,self.ropeModel.edgedirection))                            if self.ropeModel.release < LingoNumber(1):                 for tmp_A1 in LingoGlobal.pyrange(LingoNumber(1), LingoGlobal.op_div(self.ropeModel.segments.count,LingoNumber(2))):                     a1 = tmp_A1                    fac = LingoGlobal.power(LingoGlobal.op_sub(LingoNumber(1.0000),LingoGlobal.op_div(LingoGlobal.op_sub(a1.float,LingoNumber(1.0000)),LingoGlobal.op_div(self.ropeModel.segments.count,LingoNumber(2)))),LingoNumber(2))                    a = LingoGlobal.op_sub(LingoGlobal.op_add(self.ropeModel.segments.count,LingoNumber(1)),a1)                    self.ropeModel.segments[a].vel = LingoGlobal.op_sub(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(LingoGlobal.op_mul(dir,fac),self.ropeModel.edgedirection))                    tmp_A1 = a1                                    idealfirstpos = LingoGlobal.op_sub(self.ropeModel.posb,LingoGlobal.op_mul(dir,self.ropeModel.segmentlength))                self.ropeModel.segments[self.ropeModel.segments.count].pos = LingoGlobal.point(self.lerp(self.ropeModel.segments[self.ropeModel.segments.count].pos.loch,idealfirstpos.loch,self.ropeModel.edgedirection),self.lerp(self.ropeModel.segments[self.ropeModel.segments.count].pos.locv,idealfirstpos.locv,self.ropeModel.edgedirection))                                    if self.ropeModel.release > -LingoNumber(1):             self.ropeModel.segments[LingoNumber(1)].pos = self.ropeModel.posa            self.ropeModel.segments[LingoNumber(1)].vel = LingoGlobal.point(LingoNumber(0),LingoNumber(0))                    if self.ropeModel.release < LingoNumber(1):             self.ropeModel.segments[self.ropeModel.segments.count].pos = self.ropeModel.posb            self.ropeModel.segments[self.ropeModel.segments.count].vel = LingoGlobal.point(LingoNumber(0),LingoNumber(0))                    for tmp_i in LingoGlobal.pyrange(LingoNumber(1), self.ropeModel.segments.count):             i = tmp_i            self.ropeModel.segments[i].lastpos = self.ropeModel.segments[i].pos            self.ropeModel.segments[i].pos = LingoGlobal.op_add(self.ropeModel.segments[i].pos,self.ropeModel.segments[i].vel)            self.ropeModel.segments[i].vel = LingoGlobal.op_mul(self.ropeModel.segments[i].vel,self.ropeModel.airfric)            self.ropeModel.segments[i].vel.locv = LingoGlobal.op_add(self.ropeModel.segments[i].vel.locv,self.ropeModel.grav)            tmp_i = i                    for tmp_i in LingoGlobal.pyrange(LingoNumber(2), self.ropeModel.segments.count):             i = tmp_i            self.connectropepoints(i,LingoGlobal.op_sub(i,LingoNumber(1)))
            if self.ropeModel.rigid > LingoNumber(0):                 self.applyrigidity(i)            tmp_i = i                    for tmp_i in LingoGlobal.pyrange(LingoNumber(2), self.ropeModel.segments.count):             i = tmp_i            a = LingoGlobal.op_add(LingoGlobal.op_sub(self.ropeModel.segments.count,i),LingoNumber(1))            self.connectropepoints(a,LingoGlobal.op_add(a,LingoNumber(1)))
            if self.ropeModel.rigid > LingoNumber(0):                 self.applyrigidity(a)            tmp_i = i                    if self.ropeModel.selfpush > LingoNumber(0):             for tmp_A in LingoGlobal.pyrange(LingoNumber(1), self.ropeModel.segments.count):                 a = tmp_A                for tmp_B in LingoGlobal.pyrange(LingoNumber(1), self.ropeModel.segments.count):                     b = tmp_B                    if (LingoGlobal.op_ne_b(a, b) and LingoGlobal.ToBool(self.diagwi(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos,self.ropeModel.selfpush))):                         dir = self.movetopoint(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos,LingoNumber(1.0000))                        dist = self.diag(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos)                        mov = LingoGlobal.op_mul(dir,LingoGlobal.op_sub(dist,self.ropeModel.selfpush))                        self.ropeModel.segments[a].pos = LingoGlobal.op_add(self.ropeModel.segments[a].pos,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))                        self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))                        self.ropeModel.segments[b].pos = LingoGlobal.op_sub(self.ropeModel.segments[b].pos,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))                        self.ropeModel.segments[b].vel = LingoGlobal.op_sub(self.ropeModel.segments[b].vel,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))                                            tmp_B = b                                    tmp_A = a                                    if self.ropeModel.sourcepush > LingoNumber(0):             for tmp_A in LingoGlobal.pyrange(LingoNumber(1), self.ropeModel.segments.count):                 a = tmp_A                self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(self.movetopoint(self.ropeModel.posa,self.ropeModel.segments[a].pos,self.ropeModel.sourcepush),self.restrict(LingoGlobal.op_sub(LingoGlobal.op_div(LingoGlobal.op_sub(a,LingoNumber(1.0000)),LingoGlobal.op_sub(self.ropeModel.segments.count,LingoNumber(1.0000))),LingoNumber(0.7000)),LingoNumber(0),LingoNumber(1))))                self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(self.movetopoint(self.ropeModel.posb,self.ropeModel.segments[a].pos,self.ropeModel.sourcepush),self.restrict(LingoGlobal.op_sub(LingoGlobal.op_sub(LingoNumber(1.0000),LingoGlobal.op_div(LingoGlobal.op_sub(a,LingoNumber(1.0000)),LingoGlobal.op_sub(self.ropeModel.segments.count,LingoNumber(1.0000)))),LingoNumber(0.7000)),LingoNumber(0),LingoNumber(1))))                tmp_A = a                                    for tmp_i in LingoGlobal.pyrange(LingoGlobal.op_add(LingoNumber(1),LingoGlobal.op_gt(self.ropeModel.release,-LingoNumber(1))), LingoGlobal.op_sub(self.ropeModel.segments.count,LingoGlobal.op_lt(self.ropeModel.release,LingoNumber(1)))):             i = tmp_i            self.pushropepointoutofterrain(i)
            tmp_i = i                    if LingoGlobal.ToBool(preview):             _global.member("ropePreview").image.copypixels(LingoImage.Pxl,_global.member("ropePreview").image.rect,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(dict(color = _global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255)))))
            for tmp_i in LingoGlobal.pyrange(LingoNumber(1), self.ropeModel.segments.count):                 i = tmp_i                adaptedpos = self.smoothedpos(i)                adaptedpos = LingoGlobal.op_sub(adaptedpos,LingoGlobal.op_mul(camerapos,LingoNumber(20.0000)))                adaptedpos = LingoGlobal.op_mul(adaptedpos,previewscale)                _global.member("ropePreview").image.copypixels(LingoImage.Pxl,LingoGlobal.rect(LingoGlobal.op_sub(adaptedpos,LingoGlobal.point(LingoNumber(1),LingoNumber(1))),LingoGlobal.op_add(adaptedpos,LingoGlobal.point(LingoNumber(2),LingoNumber(2)))),LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1)),LingoPropertyList(dict(color = _global.color(LingoNumber(0),LingoNumber(0),LingoNumber(0)))))
                tmp_i = i                                            return None            def connectropepoints(self, a, b):         dir = None        dist = None        mov = None        dir = self.movetopoint(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos,LingoNumber(1.0000))        dist = self.diag(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos)        if (LingoGlobal.op_eq_b(self.ropeModel.stiff, LingoNumber(1)) or dist > self.ropeModel.segmentlength):             mov = LingoGlobal.op_mul(dir,LingoGlobal.op_sub(dist,self.ropeModel.segmentlength))            self.ropeModel.segments[a].pos = LingoGlobal.op_add(self.ropeModel.segments[a].pos,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))            self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))            self.ropeModel.segments[b].pos = LingoGlobal.op_sub(self.ropeModel.segments[b].pos,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))            self.ropeModel.segments[b].vel = LingoGlobal.op_sub(self.ropeModel.segments[b].vel,LingoGlobal.op_mul(mov,LingoNumber(0.5000)))                            return None            def applyrigidity(self, a):         b2 = None        b = None        dir = None        for tmp_B2 in LingoList(-LingoNumber(2),LingoNumber(2),-LingoNumber(3),LingoNumber(3),-LingoNumber(4),LingoNumber(4)):             b2 = tmp_B2            b = LingoGlobal.op_add(a,b2)            if (b > LingoNumber(0) and b <= self.ropeModel.segments.count):                 dir = self.movetopoint(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos,LingoNumber(1.0000))                self.ropeModel.segments[a].vel = LingoGlobal.op_sub(self.ropeModel.segments[a].vel,LingoGlobal.op_div(LingoGlobal.op_mul(LingoGlobal.op_mul(dir,self.ropeModel.rigid),self.ropeModel.segmentlength),LingoGlobal.op_add(LingoGlobal.op_add(self.diag(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos),LingoNumber(0.1000)),LingoGlobal.abs(b2))))                self.ropeModel.segments[b].vel = LingoGlobal.op_add(self.ropeModel.segments[b].vel,LingoGlobal.op_div(LingoGlobal.op_mul(LingoGlobal.op_mul(dir,self.ropeModel.rigid),self.ropeModel.segmentlength),LingoGlobal.op_add(LingoGlobal.op_add(self.diag(self.ropeModel.segments[a].pos,self.ropeModel.segments[b].pos),LingoNumber(0.1000)),LingoGlobal.abs(b2))))                                            return None            def smoothedpos(self, a):         smoothpos = None        if LingoGlobal.op_eq_b(a, LingoNumber(1)):             if self.ropeModel.release > -LingoNumber(1):                 return self.ropeModel.posa                            else:                return self.ropeModel.segments[a].pos                                    elif LingoGlobal.op_eq_b(a, self.ropeModel.segments.count):             if self.ropeModel.release < LingoNumber(1):                 return self.ropeModel.posb                            else:                return self.ropeModel.segments[a].pos                                    else:            smoothpos = LingoGlobal.op_div(LingoGlobal.op_add(self.ropeModel.segments[LingoGlobal.op_sub(a,LingoNumber(1))].pos,self.ropeModel.segments[LingoGlobal.op_add(a,LingoNumber(1))].pos),LingoNumber(2.0000))            return LingoGlobal.op_div(LingoGlobal.op_add(self.ropeModel.segments[a].pos,smoothpos),LingoNumber(2.0000))                            return None            def pushropepointoutofterrain(self, a):         p = None        gridpos = None        dir = None        midpos = None        terrainpos = None        dist = None        mov = None        p = LingoPropertyList(dict(loc = self.ropeModel.segments[a].pos,lastloc = self.ropeModel.segments[a].lastpos,frc = self.ropeModel.segments[a].vel,sizepnt = LingoGlobal.point(self.ropeModel.segrad,self.ropeModel.segrad)))        p = self.sharedcheckvcollision(p,self.ropeModel.friction,self.ropeModel.layer)        self.ropeModel.segments[a].pos = p.loc        self.ropeModel.segments[a].vel = p.frc        gridpos = self.givegridpos(self.ropeModel.segments[a].pos)        for tmp_dir in LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(-LingoNumber(1),-LingoNumber(1)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(1),LingoNumber(1)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)),LingoGlobal.point(-LingoNumber(1),LingoNumber(1))):             dir = tmp_dir            if LingoGlobal.op_eq_b(self.afamvlvledit(LingoGlobal.op_add(gridpos,dir),self.ropeModel.layer), LingoNumber(1)):                 midpos = self.givemiddleoftile(LingoGlobal.op_add(gridpos,dir))                terrainpos = LingoGlobal.point(self.restrict(self.ropeModel.segments[a].pos.loch,LingoGlobal.op_sub(midpos.loch,LingoNumber(10)),LingoGlobal.op_add(midpos.loch,LingoNumber(10))),self.restrict(self.ropeModel.segments[a].pos.locv,LingoGlobal.op_sub(midpos.locv,LingoNumber(10)),LingoGlobal.op_add(midpos.locv,LingoNumber(10))))                terrainpos = LingoGlobal.op_div(LingoGlobal.op_add(LingoGlobal.op_mul(terrainpos,LingoNumber(10.0000)),midpos),LingoNumber(11.0000))                dir = self.movetopoint(self.ropeModel.segments[a].pos,terrainpos,LingoNumber(1.0000))                dist = self.diag(self.ropeModel.segments[a].pos,terrainpos)                if dist < self.ropeModel.segrad:                     mov = LingoGlobal.op_mul(dir,LingoGlobal.op_sub(dist,self.ropeModel.segrad))                    self.ropeModel.segments[a].pos = LingoGlobal.op_add(self.ropeModel.segments[a].pos,mov)                    self.ropeModel.segments[a].vel = LingoGlobal.op_add(self.ropeModel.segments[a].vel,mov)                                                                return None            def sharedcheckvcollision(self, p, friction, layer):         bounce = None        lastgridpos = None        feetpos = None        lastfeetpos = None        leftpos = None        rightpos = None        q = None        c = None        headpos = None        lastheadpos = None        d = None        bounce = LingoNumber(0)        if p.frc.locv > LingoNumber(0):             lastgridpos = self.givegridpos(p.lastloc)            feetpos = self.givegridpos(LingoGlobal.op_add(p.loc,LingoGlobal.point(LingoNumber(0),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            lastfeetpos = self.givegridpos(LingoGlobal.op_add(p.lastloc,LingoGlobal.point(LingoNumber(0),p.sizepnt.locv)))            leftpos = self.givegridpos(LingoGlobal.op_add(p.loc,LingoGlobal.point(LingoGlobal.op_add(-p.sizepnt.loch,LingoNumber(1)),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            rightpos = self.givegridpos(LingoGlobal.op_add(p.loc,LingoGlobal.point(LingoGlobal.op_sub(p.sizepnt.loch,LingoNumber(1)),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            for tmp_q in LingoGlobal.pyrange(lastfeetpos.locv, feetpos.locv):                 q = tmp_q                for tmp_c in LingoGlobal.pyrange(leftpos.loch, rightpos.loch):                     c = tmp_c                    if (LingoGlobal.op_eq_b(self.afamvlvledit(LingoGlobal.point(c,q),layer), LingoNumber(1)) and LingoGlobal.op_ne_b(self.afamvlvledit(LingoGlobal.point(c,LingoGlobal.op_sub(q,LingoNumber(1))),layer), LingoNumber(1))):                         if (lastgridpos.locv >= q and LingoGlobal.op_eq_b(self.afamvlvledit(lastgridpos,layer), LingoNumber(1))):                             pass                                                    else:                            p.loc.locv = LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20.0000)),p.sizepnt.locv)                            p.frc.loch = LingoGlobal.op_mul(p.frc.loch,friction)                            p.frc.locv = LingoGlobal.op_mul(-p.frc.locv,bounce)                            return p                            return None                                                                        tmp_c = c                                    tmp_q = q                                    elif p.frc.locv < LingoNumber(0):             lastgridpos = self.givegridpos(p.lastloc)            headpos = self.givegridpos(LingoGlobal.op_sub(p.loc,LingoGlobal.point(LingoNumber(0),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            lastheadpos = self.givegridpos(LingoGlobal.op_sub(p.lastloc,LingoGlobal.point(LingoNumber(0),p.sizepnt.locv)))            leftpos = self.givegridpos(LingoGlobal.op_add(p.loc,LingoGlobal.point(LingoGlobal.op_add(-p.sizepnt.loch,LingoNumber(1)),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            rightpos = self.givegridpos(LingoGlobal.op_add(p.loc,LingoGlobal.point(LingoGlobal.op_sub(p.sizepnt.loch,LingoNumber(1)),LingoGlobal.op_add(p.sizepnt.locv,LingoNumber(0.0100)))))            for tmp_d in LingoGlobal.pyrange(headpos.locv, lastheadpos.locv):                 d = tmp_d                q = LingoGlobal.op_sub(lastheadpos.locv,LingoGlobal.op_sub(d,headpos.locv))                for tmp_c in LingoGlobal.pyrange(leftpos.loch, rightpos.loch):                     c = tmp_c                    if (LingoGlobal.op_eq_b(self.afamvlvledit(LingoGlobal.point(c,q),layer), LingoNumber(1)) and LingoGlobal.op_ne_b(self.afamvlvledit(LingoGlobal.point(c,LingoGlobal.op_add(q,LingoNumber(1))),layer), LingoNumber(1))):                         if (lastgridpos.locv <= q and LingoGlobal.op_ne_b(self.afamvlvledit(lastgridpos,layer), LingoNumber(1))):                             pass                                                    else:                            p.loc.locv = LingoGlobal.op_add(LingoGlobal.op_mul(q,LingoNumber(20.0000)),p.sizepnt.locv)                            p.frc.loch = LingoGlobal.op_mul(p.frc.loch,friction)                            p.frc.locv = LingoGlobal.op_mul(-p.frc.locv,bounce)                            return p                            return None                                                                        tmp_c = c                                    tmp_d = d                                    return p                    