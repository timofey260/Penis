from Drizzle.Runtime import *## Movie script: fiffigt#class MovieScript:     def __init__(self):         super().__init__()            def diag(self, point1, point2):         rectheight = None        rectwidth = None        diagonal = None        rectheight = LingoGlobal.abs(LingoGlobal.op_sub(point1.locv,point2.locv))        rectwidth = LingoGlobal.abs(LingoGlobal.op_sub(point1.loch,point2.loch))        diagonal = LingoGlobal.sqrt(LingoGlobal.op_add(LingoGlobal.op_mul(rectheight,rectheight),LingoGlobal.op_mul(rectwidth,rectwidth)))        return diagonal                    def diagwi(self, point1, point2, dig):         rectheight = None        rectwidth = None        rectheight = LingoGlobal.abs(LingoGlobal.op_sub(point1.locv,point2.locv))        rectwidth = LingoGlobal.abs(LingoGlobal.op_sub(point1.loch,point2.loch))        return LingoGlobal.op_lt(LingoGlobal.op_add(LingoGlobal.op_mul(rectheight,rectheight),LingoGlobal.op_mul(rectwidth,rectwidth)),LingoGlobal.op_mul(dig,dig))                    def diagnosqrt(self, point1, point2):         rectheight = None        rectwidth = None        diagonal = None        rectheight = LingoGlobal.abs(LingoGlobal.op_sub(point1.locv,point2.locv))        rectwidth = LingoGlobal.abs(LingoGlobal.op_sub(point1.loch,point2.loch))        diagonal = LingoGlobal.op_add(LingoGlobal.op_mul(rectheight,rectheight),LingoGlobal.op_mul(rectwidth,rectwidth))        return diagonal                    def vertfliprect(self, rct):         return LingoList(LingoGlobal.point(rct.right,rct.top),LingoGlobal.point(rct.left,rct.top),LingoGlobal.point(rct.left,rct.bottom),LingoGlobal.point(rct.right,rct.bottom))                    def movetopoint(self, pointa, pointb, themovement):         diagonal = None        dirvec = None        pointb = LingoGlobal.op_sub(pointb,pointa)        diagonal = self.diag(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),pointb)        if diagonal > LingoNumber(0):             dirvec = LingoGlobal.op_div(pointb,diagonal)                    else:            dirvec = LingoGlobal.point(LingoNumber(0),LingoNumber(1))                    return LingoGlobal.op_mul(dirvec,themovement)                    def returnrelativepoint(self, p1, p2):         newx = None        newy = None        newx = LingoGlobal.op_mul(-LingoNumber(1),LingoGlobal.op_sub(p1.loch,p2.loch))        newy = LingoGlobal.op_sub(p1.locv,p2.locv)        return LingoGlobal.point(newx,newy)                    def returnabsolutepoint(self, p1, p2):         realx = None        realy = None        realx = LingoGlobal.op_add(p1.loch,p2.loch)        realy = LingoGlobal.op_sub(p1.locv,p2.locv)        return LingoGlobal.point(realx,realy)                    def lerp(self, a, b, val):         sv = None        val = self.restrict(val,LingoNumber(0),LingoNumber(1))        if b < a:             sv = a            a = b            b = sv            val = LingoGlobal.op_sub(LingoNumber(1.0000),val)                    return self.restrict(LingoGlobal.op_add(a,LingoGlobal.op_mul(LingoGlobal.op_sub(b,a),val)),a,b)                    def givecrosspoint(self, line1pnta, line1pntb, line2pnta, line2pntb):         x1 = None        y1 = None        x2 = None        y2 = None        x3 = None        y3 = None        x4 = None        y4 = None        crosspointx = None        crosspointy = None        x1 = line1pnta.loch.float        y1 = line1pnta.locv.float        x2 = line1pntb.loch.float        y2 = line1pntb.locv.float        x3 = line2pnta.loch.float        y3 = line2pnta.locv.float        x4 = line2pntb.loch.float        y4 = line2pntb.locv.float        if (LingoGlobal.op_ne_b(x2, x1) and LingoGlobal.op_ne_b(x4, x3)):             if LingoGlobal.op_ne_b(LingoGlobal.op_sub(LingoGlobal.op_div(LingoGlobal.op_sub(y4,y3),LingoGlobal.op_sub(x4,x3)),LingoGlobal.op_div(LingoGlobal.op_sub(y2,y1),LingoGlobal.op_sub(x2,x1))), LingoNumber(0)):                 crosspointx = LingoGlobal.op_div(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(y1,LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y2,y1),LingoGlobal.op_sub(x2,x1)),x1)),LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y4,y3),LingoGlobal.op_sub(x4,x3)),x3)),y3),LingoGlobal.op_sub(LingoGlobal.op_div(LingoGlobal.op_sub(y4,y3),LingoGlobal.op_sub(x4,x3)),LingoGlobal.op_div(LingoGlobal.op_sub(y2,y1),LingoGlobal.op_sub(x2,x1))))                crosspointy = LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y2,y1),LingoGlobal.op_sub(x2,x1)),crosspointx),LingoGlobal.op_sub(y1,LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y2,y1),LingoGlobal.op_sub(x2,x1)),x1)))                                    elif LingoGlobal.op_ne_b(x4, x3):             crosspointx = x1            crosspointy = LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y4,y3),LingoGlobal.op_sub(x4,x3)),crosspointx),y3),LingoGlobal.op_mul(LingoGlobal.op_div(LingoGlobal.op_sub(y4,y3),LingoGlobal.op_sub(x4,x3)),x3))                    else:            crosspointx = x3            crosspointy = y1                    return LingoGlobal.point(crosspointx,crosspointy)                    def lookatpoint(self, pos, lookatpoint):         y_diff = None        x_diff = None        rotationanglerad = None        fuckedupanglefix_parameter = None        y_diff = LingoGlobal.op_sub(lookatpoint.locv.float,pos.locv.float)        x_diff = LingoGlobal.op_sub(pos.loch.float,lookatpoint.loch.float)        if LingoGlobal.op_ne_b(x_diff, LingoNumber(0)):             rotationanglerad = LingoGlobal.atan(LingoGlobal.op_div(y_diff,x_diff))                    else:            rotationanglerad = LingoGlobal.op_mul(LingoNumber(1.5000),LingoGlobal.PI)                    if lookatpoint.loch > pos.loch:             fuckedupanglefix_parameter = LingoNumber(0)                    else:            fuckedupanglefix_parameter = LingoGlobal.PI                    rotationanglerad = LingoGlobal.op_sub(fuckedupanglefix_parameter,rotationanglerad)        return LingoGlobal.op_add(LingoGlobal.op_div(LingoGlobal.op_mul(rotationanglerad,LingoNumber(180)),LingoGlobal.PI),LingoNumber(90))                    def degtovec(self, deg):         rad = None        deg = LingoGlobal.op_add(deg,LingoNumber(90))        deg = -deg        rad = LingoGlobal.op_mul(LingoGlobal.op_mul(LingoGlobal.op_div(deg,LingoNumber(360.0000)).float,LingoGlobal.PI),LingoNumber(2))        return LingoGlobal.point(-LingoGlobal.cos(rad),LingoGlobal.sin(rad))                    def degtovecfac2(self, deg, fach, facv):         rad = None        deg = LingoGlobal.op_add(deg,LingoNumber(90))        deg = -deg        rad = LingoGlobal.op_mul(LingoGlobal.op_mul(LingoGlobal.op_div(deg,LingoNumber(360.0000)).float,LingoGlobal.PI),LingoNumber(2))        return LingoGlobal.point(LingoGlobal.op_mul(-LingoGlobal.cos(rad),fach),LingoGlobal.op_mul(LingoGlobal.sin(rad),facv))                    def closestpointonline(self, pnt, a, b):         return self.givecrosspoint(pnt,LingoGlobal.op_add(pnt,self.givedirfor90degrtoline(a,b)),a,b)                    def givedirfor90degrtoline(self, pnt1, pnt2):         x1 = None        y1 = None        x2 = None        y2 = None        ydiff = None        xdiff = None        dir = None        newdir = None        newpnt = None        fac = None        x1 = pnt1.loch        y1 = pnt1.locv        x2 = pnt2.loch        y2 = pnt2.locv        ydiff = LingoGlobal.op_sub(y1,y2)        xdiff = LingoGlobal.op_sub(x1,x2)        if LingoGlobal.op_ne_b(xdiff, LingoNumber(0)):             dir = LingoGlobal.op_div(ydiff,xdiff)                    else:            dir = LingoNumber(1)                    if LingoGlobal.op_ne_b(dir, LingoNumber(0)):             newdir = LingoGlobal.op_div(-LingoNumber(1.0000),dir)                    else:            newdir = LingoNumber(1)                    newpnt = LingoGlobal.point(LingoNumber(1),newdir)        fac = LingoNumber(1)        if x2 < x1:             if y2 < y1:                 fac = LingoNumber(1)                            else:                fac = -LingoNumber(1)                                    elif y2 < y1:             fac = LingoNumber(1)                    else:            fac = -LingoNumber(1)                    newpnt = LingoGlobal.op_mul(newpnt,fac)        newpnt = LingoGlobal.op_div(newpnt,self.diag(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),newpnt))        return newpnt                    def lnpntdist(self, pnt, linea, lineb):         return self.diag(pnt,self.givecrosspoint(pnt,LingoGlobal.op_add(pnt,self.givedirfor90degrtoline(linea,lineb)),linea,lineb))                    def givecirclecolltime(self, pos1, r1, vel1, pos2, r2, vel2):         x1 = None        y1 = None        x2 = None        y2 = None        vx1 = None        vy1 = None        vx2 = None        vy2 = None        a = None        b = None        c = None        d = None        e = None        t = None        x1 = pos1.loch        y1 = pos1.locv        x2 = pos2.loch        y2 = pos2.locv        vx1 = vel1.loch        vy1 = vel1.locv        vx2 = vel2.loch        vy2 = vel2.locv        a = LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_mul(-x1,vx1),LingoGlobal.op_mul(y1,vy1)),LingoGlobal.op_mul(vx1,x2)),LingoGlobal.op_mul(vy1,y2)),LingoGlobal.op_mul(x1,vx2)),LingoGlobal.op_mul(x2,vx2)),LingoGlobal.op_mul(y1,vy2)),LingoGlobal.op_mul(y2,vy2))        b = LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_mul(-x1,vx1),LingoGlobal.op_mul(y1,vy1)),LingoGlobal.op_mul(vx1,x2)),LingoGlobal.op_mul(vy1,y2)),LingoGlobal.op_mul(x1,vx2)),LingoGlobal.op_mul(x2,vx2)),LingoGlobal.op_mul(y1,vy2)),LingoGlobal.op_mul(y2,vy2))        c = LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.power(vx1,LingoNumber(2)),LingoGlobal.power(vy1,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),vx1),vx2)),LingoGlobal.power(vx2,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),vy1),vy2)),LingoGlobal.power(vy2,LingoNumber(2)))        d = LingoGlobal.op_sub(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.power(x1,LingoNumber(2)),LingoGlobal.power(y1,LingoNumber(2))),LingoGlobal.power(r1,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),x1),x2)),LingoGlobal.power(x2,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),y1),y2)),LingoGlobal.power(y2,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),r1),r2)),LingoGlobal.power(r2,LingoNumber(2)))        e = LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_add(LingoGlobal.power(vx1,LingoNumber(2)),LingoGlobal.power(vy1,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),vx1),vx2)),LingoGlobal.power(vx2,LingoNumber(2))),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(2),vy1),vy2)),LingoGlobal.power(vy2,LingoNumber(2)))        t = LingoGlobal.op_div(LingoGlobal.op_sub(LingoGlobal.op_mul(LingoNumber(2.0000),a),LingoGlobal.sqrt(LingoGlobal.op_sub(LingoGlobal.power(LingoGlobal.op_mul(-LingoNumber(2.0000),b),LingoNumber(2)),LingoGlobal.op_mul(LingoGlobal.op_mul(LingoNumber(4.0000),c),d)))),LingoGlobal.op_mul(LingoNumber(2.0000),e))        return t                    def lnpntdistnonabs(self, pnt, lnpnt1, lnpnt2):         k = None        m = None        y1 = None        x1 = None        k2 = None        d = None        e = None        f = None        if LingoGlobal.op_ne_b(LingoGlobal.op_sub(lnpnt1.loch,lnpnt2.loch), LingoNumber(0)):             k = LingoGlobal.op_div(LingoGlobal.op_sub(lnpnt1.locv,lnpnt2.locv),LingoGlobal.op_sub(lnpnt1.loch,lnpnt2.loch))                    else:            k = LingoNumber(0)                    m = LingoGlobal.op_sub(lnpnt1.locv,LingoGlobal.op_mul(k,lnpnt1.loch))        y1 = pnt.locv        x1 = pnt.loch        if LingoGlobal.op_ne_b(x1, LingoNumber(0)):             k2 = LingoGlobal.op_div(LingoGlobal.op_sub(y1,m),x1)            d = LingoGlobal.sqrt(LingoGlobal.op_add(LingoGlobal.power(LingoGlobal.abs(LingoGlobal.op_sub(y1,m)),LingoNumber(2)),LingoGlobal.power(x1,LingoNumber(2))))            e = LingoGlobal.sin(LingoGlobal.atan(LingoGlobal.op_div(LingoGlobal.op_sub(k2,k),LingoGlobal.op_add(LingoNumber(1),LingoGlobal.op_mul(k2,k)))))            f = LingoNumber(1)            if k < LingoNumber(0):                 f = -LingoNumber(1)                            return LingoGlobal.op_mul(LingoGlobal.op_mul(d,e),f)                    else:            return LingoGlobal.point(LingoNumber(0),LingoNumber(0))                            return None            def closestpntinrect(self, rct, pnt):         respnt = None        respnt = LingoGlobal.point(LingoNumber(0),LingoNumber(0))        if pnt.loch < rct.left:             if pnt.locv < rct.top:                 respnt = LingoGlobal.point(rct.left,rct.top)                            elif pnt.locv > rct.bottom:                 respnt = LingoGlobal.point(rct.left,rct.bottom)                            else:                respnt = LingoGlobal.point(rct.left,pnt.locv)                                    elif pnt.loch > rct.right:             if pnt.locv < rct.top:                 respnt = LingoGlobal.point(rct.right,rct.top)                            elif pnt.locv > rct.bottom:                 respnt = LingoGlobal.point(rct.right,rct.bottom)                            else:                respnt = LingoGlobal.point(rct.right,pnt.locv)                                    elif pnt.locv < rct.top:             respnt = LingoGlobal.point(pnt.loch,rct.top)                    elif pnt.locv > rct.bottom:             respnt = LingoGlobal.point(pnt.loch,rct.bottom)                    else:            respnt = pnt                    return respnt                    def anglebetweenlines(self, pnt1, pnt2, pnt3, pnt4):         return LingoGlobal.op_sub(self.lookatpoint(pnt1,pnt2),self.lookatpoint(pnt3,pnt4))                    def compareangles(self, origo, pnt1, pnt2):         ang = None        pnt1 = LingoGlobal.op_sub(pnt1,origo)        pnt2 = LingoGlobal.op_sub(pnt2,origo)        pnt2 = self.rotatepntfromorigo(pnt2,LingoGlobal.point(LingoNumber(0),LingoNumber(0)),self.lookatpoint(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),pnt1))        ang = self.lookatpoint(LingoGlobal.point(LingoNumber(0),LingoNumber(0)),pnt2)        if ang > LingoNumber(180):             ang = LingoGlobal.abs(LingoGlobal.op_sub(ang,LingoNumber(360)))                    return ang                    def rotatepntfromorigo(self, pnt, org, rotat):         realdir = None        diagonal = None        newdir = None        vec = None        rotatedpnt = None        realdir = self.lookatpoint(org,pnt)        diagonal = self.diag(org,pnt)        newdir = LingoGlobal.op_sub(realdir,rotat)        vec = self.degtovec(newdir)        rotatedpnt = LingoGlobal.op_add(org,LingoGlobal.op_mul(vec,diagonal))        return rotatedpnt                    def customadd(self, l, val):         l.add(val)
        return l                    def customsort(self, l):         l.sort()
        return l                    def insideline(self, pnt, a, b, rad):         retrn = None        dist = None        hyp1 = None        hyp2 = None        maxdiag = None        retrn = LingoGlobal.FALSE        if self.diag(pnt,a) < rad:             retrn = LingoGlobal.TRUE                    elif self.diag(pnt,b) < rad:             retrn = LingoGlobal.TRUE                    if LingoGlobal.op_eq_b(retrn, LingoGlobal.FALSE):             dist = LingoGlobal.abs(self.lnpntdistnonabs(pnt,a,b))            if dist < rad:                 hyp1 = self.diag(a,b)                hyp2 = self.diag(a,LingoGlobal.op_add(a,LingoGlobal.op_mul(self.givedirfor90degrtoline(a,b),rad)))                maxdiag = LingoGlobal.sqrt(LingoGlobal.op_add(LingoGlobal.power(hyp1,LingoNumber(2)),LingoGlobal.power(hyp2,LingoNumber(2))))                if (self.diag(pnt,a) < maxdiag and self.diag(pnt,b) < maxdiag):                     retrn = LingoGlobal.TRUE                                                        return retrn                    def newmakelevel(self, lvlname):         sz = None        pos = None        lightangle = None        txt = None        q = None        mtrx = None        c = None        e = None        foundfile = None        i = None        n = None        filedeleter = None        objfileio = None        fileopener = None        self._global.put(LingoGlobal.concat_space("saving:",lvlname,"..."))
        sz = LingoGlobal.op_mul(self.gLOprops.size,LingoNumber(20))        pos = LingoGlobal.point(LingoNumber(0),LingoNumber(0))        lightangle = LingoGlobal.op_mul(self.degtovec(self.gLightEProps.lightangle),self.gLightEProps.flatness)        txt = ""        txt = LingoGlobal.concat(txt,lvlname)        txt += str(LingoGlobal.RETURN)        txt = LingoGlobal.concat(txt,LingoGlobal.op_sub(LingoGlobal.op_sub(self.gLOprops.size.loch,self.gLOprops.extratiles[LingoNumber(1)]),self.gLOprops.extratiles[LingoNumber(3)]),"*",LingoGlobal.op_sub(LingoGlobal.op_sub(self.gLOprops.size.locv,self.gLOprops.extratiles[LingoNumber(2)]),self.gLOprops.extratiles[LingoNumber(4)]))        if self.gEnvEditorProps.waterlevel > -LingoNumber(1):             txt = LingoGlobal.concat(txt,"|",self.gEnvEditorProps.waterlevel,"|",self.gEnvEditorProps.waterinfront)                    txt += str(LingoGlobal.RETURN)        txt = LingoGlobal.concat(txt,lightangle.loch,"*",lightangle.locv,"|0|0")        txt += str(LingoGlobal.RETURN)        tmp_q=int(LingoNumber(1))        while tmp_q < self.gCameraProps.cameras.count:             q = tmp_q            txt += str(LingoGlobal.concat(LingoGlobal.op_sub(self.gCameraProps.cameras[q].loch.integer,LingoGlobal.op_mul(self.gLOprops.extratiles[LingoNumber(1)],LingoNumber(20))),",",LingoGlobal.op_sub(self.gCameraProps.cameras[q].locv.integer,LingoGlobal.op_mul(self.gLOprops.extratiles[LingoNumber(2)],LingoNumber(20)))))            if q < self.gCameraProps.cameras.count:                 txt += str("|")                            tmp_q = q            tmp_q += 1                    mtrx = self._global.script("saveFile").changetoplaymatrix()        txt += str(LingoGlobal.RETURN)        if LingoGlobal.op_eq_b(self.gLevel.defaultterrain, LingoNumber(1)):             txt = LingoGlobal.concat(txt,"Border: Solid")                    else:            txt = LingoGlobal.concat(txt,"Border: Passable")                    txt += str(LingoGlobal.RETURN)        tmp_q=int(LingoGlobal.op_add(LingoNumber(1),self.gLOprops.extratiles[LingoNumber(1)]))        while tmp_q < LingoGlobal.op_sub(self.gLOprops.size.loch,self.gLOprops.extratiles[LingoNumber(3)]):             q = tmp_q            tmp_c=int(LingoGlobal.op_add(LingoNumber(1),self.gLOprops.extratiles[LingoNumber(2)]))            while tmp_c < LingoGlobal.op_sub(self.gLOprops.size.locv,self.gLOprops.extratiles[LingoNumber(4)]):                 c = tmp_c                if mtrx[q][c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(9)) > LingoNumber(0):                     txt = LingoGlobal.concat(txt,"0,",LingoGlobal.op_sub(q,self.gLOprops.extratiles[LingoNumber(1)]),",",LingoGlobal.op_sub(c,self.gLOprops.extratiles[LingoNumber(2)]),"|")                                    if mtrx[q][c][LingoNumber(1)][LingoNumber(2)].getpos(LingoNumber(10)) > LingoNumber(0):                     txt = LingoGlobal.concat(txt,"1,",LingoGlobal.op_sub(q,self.gLOprops.extratiles[LingoNumber(1)]),",",LingoGlobal.op_sub(c,self.gLOprops.extratiles[LingoNumber(2)]),"|")                                    tmp_c = c                tmp_c += 1                            tmp_q = q            tmp_q += 1                    txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        txt += str("0")        txt += str(LingoGlobal.RETURN)        txt += str(LingoGlobal.RETURN)        tmp_q=int(LingoGlobal.op_add(LingoNumber(1),self.gLOprops.extratiles[LingoNumber(1)]))        while tmp_q < LingoGlobal.op_sub(self.gLOprops.size.loch,self.gLOprops.extratiles[LingoNumber(3)]):             q = tmp_q            tmp_c=int(LingoGlobal.op_add(LingoNumber(1),self.gLOprops.extratiles[LingoNumber(2)]))            while tmp_c < LingoGlobal.op_sub(self.gLOprops.size.locv,self.gLOprops.extratiles[LingoNumber(4)]):                 c = tmp_c                match mtrx[q][c][LingoNumber(1)][LingoNumber(1)] if value is not None else 9999999999:                     case 1:                        txt = LingoGlobal.concat(txt,"1")                                            case 2 | 3 | 4 | 5:                        txt = LingoGlobal.concat(txt,"2")                                            case 6:                        txt = LingoGlobal.concat(txt,"3")                                            case 7:                        txt = LingoGlobal.concat(txt,"4,3")                                            case _:                         txt = LingoGlobal.concat(txt,"0")                                                            tmp_e=int(LingoNumber(1))                while tmp_e < mtrx[q][c][LingoNumber(1)][LingoNumber(2)].count:                     e = tmp_e                    match mtrx[q][c][LingoNumber(1)][LingoNumber(2)][e] if value is not None else 9999999999:                         case 2:                            if LingoGlobal.op_ne_b(mtrx[q][c][LingoNumber(1)][LingoNumber(1)], LingoNumber(1)):                                 txt = LingoGlobal.concat(txt,",1")                                                                                    case 1:                            if LingoGlobal.op_ne_b(mtrx[q][c][LingoNumber(1)][LingoNumber(1)], LingoNumber(1)):                                 txt = LingoGlobal.concat(txt,",2")                                                                                    case 5:                            txt = LingoGlobal.concat(txt,",3")                                                    case 6:                            txt = LingoGlobal.concat(txt,",4")                                                    case 7:                            txt = LingoGlobal.concat(txt,",5")                                                    case 19:                            txt = LingoGlobal.concat(txt,",9")                                                    case 21:                            txt = LingoGlobal.concat(txt,",12")                                                    case 3:                            if (LingoGlobal.op_eq_b(self.afamvlvledit(LingoGlobal.point(q,c),LingoNumber(1)), LingoNumber(0)) and LingoGlobal.op_eq_b(self.afamvlvledit(LingoGlobal.point(q,LingoGlobal.op_add(c,LingoNumber(1))),LingoNumber(1)), LingoNumber(1))):                                 txt = LingoGlobal.concat(txt,",7")                                                                                    case 18:                            txt = LingoGlobal.concat(txt,",8")                                                    case 13:                            txt = LingoGlobal.concat(txt,",10")                                                    case 20:                            txt = LingoGlobal.concat(txt,",11")                                                                        tmp_e = e                    tmp_e += 1                                    if (LingoGlobal.op_ne_b(mtrx[q][c][LingoNumber(1)][LingoNumber(1)], LingoNumber(1)) and LingoGlobal.op_eq_b(mtrx[q][c][LingoNumber(2)][LingoNumber(1)], LingoNumber(1))):                     txt = LingoGlobal.concat(txt,",6")                                    txt = LingoGlobal.concat(txt,"|")                tmp_c = c                tmp_c += 1                            tmp_q = q            tmp_q += 1                    foundfile = LingoNumber(0)        tmp_i=int(LingoNumber(1))        while tmp_i < LingoNumber(1000):             i = tmp_i            n = self._global.getnthfilenameinfolder(LingoGlobal.concat(self._global.the_moviePath,"Levels"),i)            if LingoGlobal.op_eq_b(n, LingoGlobal.EMPTY):                 break                            if LingoGlobal.op_eq_b(n, LingoGlobal.concat(lvlname,".txt")):                 foundfile = LingoNumber(1)                break                            tmp_i = i            tmp_i += 1                    self._global.put(LingoGlobal.op_add("Found file: ",foundfile))
        if LingoGlobal.op_eq_b(foundfile, LingoNumber(1)):             filedeleter = self._global.new(self._global.xtra("fileio"))            filedeleter.openfile(LingoGlobal.concat(self._global.the_moviePath,"Levels/",lvlname,".txt"),LingoNumber(0))
            filedeleter.delete()
            self._global.put("FILE DELETED!")        objfileio = self._global.new(self._global.xtra("fileio"))        objfileio.createfile(LingoGlobal.concat(self._global.the_moviePath,"Levels/",lvlname,".txt"))
        objfileio.closefile()
        fileopener = self._global.new(self._global.xtra("fileio"))        fileopener.openfile(LingoGlobal.concat(self._global.the_moviePath,"Levels/",lvlname,".txt"),LingoNumber(0))
        tmp_q=int(LingoNumber(1))        while tmp_q < LingoGlobal.thenumberoflines_helper(txt):             q = tmp_q            fileopener.writestr(LingoGlobal.lineof_helper(q,txt))
            fileopener.writereturn(windows)
            tmp_q = q            tmp_q += 1                    fileopener.closefile()
        fileopener = LingoGlobal.VOID        self._global.put(LingoGlobal.concat_space("saved22:",lvlname))        return None            def lerpvector(self, a, b, l):         return LingoGlobal.point(self.lerp(a.loch,b.loch,l),self.lerp(a.locv,b.locv,l))                    def seedoftile(self, tile):         return LingoGlobal.op_add(LingoGlobal.op_add(self.gLOprops.tileseed,LingoGlobal.op_mul(tile.locv,self.gLOprops.size.loch)),tile.loch)                    def bezier(self, a, ca, b, cb, f):         middlecontrol = None        middlecontrol = self.lerpvector(ca,cb,f)        ca = self.lerpvector(a,ca,f)        cb = self.lerpvector(cb,b,f)        ca = self.lerpvector(ca,middlecontrol,f)        cb = self.lerpvector(middlecontrol,cb,f)        return self.lerpvector(ca,cb,f)                    