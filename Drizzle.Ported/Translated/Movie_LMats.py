from Drizzle.Runtime import *## Movie script: LMats#class MovieScript:     def __init__(self):         super().__init__()            def lcheckifatileissolidandsamematerial(self, tl, lr, matname):         rtrn = None        mattile = None        tl = LingoGlobal.point(self.restrict(tl.loch,LingoNumber(1),self.gLOprops.size.loch),self.restrict(tl.locv,LingoNumber(1),self.gLOprops.size.locv))        rtrn = LingoNumber(0)        if LingoGlobal.op_eq_b(self.gLEProps.matrix[tl.loch][tl.locv][lr][LingoNumber(1)], LingoNumber(1)):             mattile = self.gTEprops.tlmatrix[tl.loch][tl.locv][lr]            if (LingoGlobal.op_eq_b(mattile.tp, "material") and LingoGlobal.op_eq_b(mattile.data, matname)):                 rtrn = LingoNumber(1)                            elif (LingoGlobal.op_eq_b(mattile.tp, "default") and LingoGlobal.op_eq_b(self.gTEprops.defaultmaterial, matname)):                 rtrn = LingoNumber(1)                                    return rtrn                    def lismytilesetopentothistile(self, matname, tl, l):         rtrn = None        tile = None        rtrn = LingoNumber(0)        if LingoGlobal.ToBool(tl.inside(LingoGlobal.rect(LingoNumber(1),LingoNumber(1),LingoGlobal.op_add(self.gLOprops.size.loch,LingoNumber(1)),LingoGlobal.op_add(self.gLOprops.size.locv,LingoNumber(1))))):             if LingoList(LingoNumber(1),LingoNumber(2),LingoNumber(3),LingoNumber(4),LingoNumber(5)).getpos(self.gLEProps.matrix[tl.loch][tl.locv][l][LingoNumber(1)]) > LingoNumber(0):                 tile = self.gTEprops.tlmatrix[tl.loch][tl.locv][l]                if (LingoGlobal.op_eq_b(tile.tp, "material") and LingoGlobal.op_eq_b(tile.data, matname)):                     rtrn = LingoNumber(1)                                    elif (LingoGlobal.op_eq_b(tile.tp, "default") and LingoGlobal.op_eq_b(self.gTEprops.defaultmaterial, matname)):                     rtrn = LingoNumber(1)                                                        elif LingoGlobal.op_eq_b(self.gTEprops.defaultmaterial, matname):             rtrn = LingoNumber(1)                    return rtrn                    def ldrawatilematerial(self, q, c, l, nm):         mattl = None        inti = None        dp = None        qcp = None        lematrixt = None        mtext = None        matfile = None        matimg = None        colored = None        effectcolora = None        effectcolorb = None        size = None        bsrect = None        gradrect = None        pstrect = None        d = None        ps = None        gtrect = None        ps2 = None        lstr = None        rct = None        pxli = None        pxlr = None        wh = None        lri = None        fl = None        rct2 = None        tlrnd = None        rnd = None        f = None        profl = None        gtatv = None        id = None        dr = None        gtath = None        slp = None        askdirs = None        myaskdirs = None        ad = None        vbf = None        bfcal = None        if self.DRCustomMatList.count >= LingoNumber(1):             mattl = self.DRCustomMatList[self.DRLastTL]            if LingoGlobal.op_ne_b(mattl.nm, nm):                 for tmp_inti in LingoGlobal.pyrange(LingoNumber(1), self.DRCustomMatList.count):                     inti = tmp_inti                    if LingoGlobal.op_eq_b(self.DRCustomMatList[inti].nm, nm):                         mattl = self.DRCustomMatList[inti]                        self.DRLastTL = inti                        break                                            tmp_inti = inti                                                if LingoGlobal.op_eq_b(mattl.nm, nm):                 match l if value is not None else 9999999999:                     case 1:                        dp = LingoNumber(0)                                            case 2:                        dp = LingoNumber(10)                                            case _:                         dp = LingoNumber(20)                                                            qcp = LingoGlobal.point(q,c)                lematrixt = self.gLEProps.matrix[q][c][l][LingoNumber(1)]                if LingoGlobal.op_ne_b(mattl.findpos(texture), LingoGlobal.VOID):                     mtext = mattl.texture                    matfile = _global.member("MatTexImport")                    if LingoGlobal.op_ne_b(self.DRLastTexImp, nm):                         _global.member("MatTexImport").importfileinto(LingoGlobal.concat("Materials",_global.the_dirSeparator,nm,"Texture.png"))
                        matfile.name = "MatTexImport"                        self.DRLastTexImp = nm                                            matimg = matfile.image                    colored = LingoGlobal.op_gt(mtext.tags.getpos("colored"),LingoNumber(0))                    if LingoGlobal.ToBool(colored):                         self.gAnyDecals = LingoNumber(1)                                            effectcolora = LingoGlobal.op_gt(mtext.tags.getpos("effectColorA"),LingoNumber(0))                    effectcolorb = LingoGlobal.op_gt(mtext.tags.getpos("effectColorB"),LingoNumber(0))                    size = mtext.sz                    bsrect = LingoGlobal.rect(LingoGlobal.op_mul(LingoGlobal.op_mod(q,size.loch),LingoNumber(20)),LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_mod(c,size.locv),LingoNumber(20)),LingoNumber(1)),LingoGlobal.op_mul(LingoGlobal.op_add(LingoGlobal.op_mod(q,size.loch),LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_add(LingoGlobal.op_mod(c,size.locv),LingoNumber(1)),LingoNumber(20)),LingoNumber(1)))                    if ((LingoGlobal.ToBool(colored) or LingoGlobal.ToBool(effectcolora)) or LingoGlobal.ToBool(effectcolorb)):                         gradrect = LingoGlobal.rect(LingoGlobal.op_mul(size.loch,LingoNumber(20)),LingoNumber(0),LingoGlobal.op_mul(size.loch,LingoNumber(20)),LingoNumber(0))                                            pstrect = LingoGlobal.op_sub(LingoGlobal.rect(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_mul(q,LingoNumber(20)),LingoGlobal.op_mul(c,LingoNumber(20))),LingoGlobal.op_mul(LingoGlobal.rect(self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                    match lematrixt if value is not None else 9999999999:                         case 1:                            d = -LingoNumber(1)                            for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl.count):                                 ps = tmp_ps                                gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1)))))                                for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl[ps]):                                     ps2 = tmp_ps2                                    d = LingoGlobal.op_add(d,LingoNumber(1))                                    if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                         break                                                                            else:                                        lstr = _global.str(LingoGlobal.op_add(d,dp))                                        _global.member(LingoGlobal.concat("layer",lstr)).image.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                        if LingoGlobal.ToBool(colored):                                             if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                 _global.member(LingoGlobal.concat("layer",lstr,"dc")).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))                                                                                    if LingoGlobal.ToBool(effectcolora):                                             _global.member(LingoGlobal.concat("gradientA",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                        if LingoGlobal.ToBool(effectcolorb):                                             _global.member(LingoGlobal.concat("gradientB",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                                                            tmp_ps2 = ps2                                                                    tmp_ps = ps                                                                                    case 2 | 3 | 4 | 5:                            rct = LingoGlobal.rect(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_mul(q,LingoNumber(20)),LingoGlobal.op_mul(c,LingoNumber(20)))                            match lematrixt if value is not None else 9999999999:                                 case 5:                                    rct = LingoList(LingoGlobal.point(rct.left,rct.top),LingoGlobal.point(rct.left,rct.top),LingoGlobal.point(rct.right,rct.bottom),LingoGlobal.point(rct.left,rct.bottom))                                                                    case 4:                                    rct = LingoList(LingoGlobal.point(rct.right,rct.top),LingoGlobal.point(rct.right,rct.top),LingoGlobal.point(rct.left,rct.bottom),LingoGlobal.point(rct.right,rct.bottom))                                                                    case 3:                                    rct = LingoList(LingoGlobal.point(rct.left,rct.bottom),LingoGlobal.point(rct.left,rct.bottom),LingoGlobal.point(rct.right,rct.top),LingoGlobal.point(rct.left,rct.top))                                                                    case 2:                                    rct = LingoList(LingoGlobal.point(rct.right,rct.bottom),LingoGlobal.point(rct.right,rct.bottom),LingoGlobal.point(rct.left,rct.top),LingoGlobal.point(rct.right,rct.top))                                                                                                rct = LingoGlobal.op_sub(rct,LingoGlobal.op_mul(LingoList(self.gRenderCameraTilePos,self.gRenderCameraTilePos,self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                            pxli = LingoImage.Pxl                            pxlr = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1))                            wh = _global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))                            d = -LingoNumber(1)                            for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl.count):                                 ps = tmp_ps                                gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1)))))                                for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl[ps]):                                     ps2 = tmp_ps2                                    d = LingoGlobal.op_add(d,LingoNumber(1))                                    if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                         break                                                                            else:                                        lstr = _global.str(LingoGlobal.op_add(d,dp))                                        lri = _global.member(LingoGlobal.concat("layer",lstr)).image                                        lri.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                        lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))
                                        if LingoGlobal.ToBool(colored):                                             if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                 lri = _global.member(LingoGlobal.concat("layer",lstr,"dc")).image                                                lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))
                                                lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                                                                    if LingoGlobal.ToBool(effectcolora):                                             lri = _global.member(LingoGlobal.concat("gradientA",lstr)).image                                            lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))
                                            lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                        if LingoGlobal.ToBool(effectcolorb):                                             lri = _global.member(LingoGlobal.concat("gradientB",lstr)).image                                            lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))
                                            lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                                                            tmp_ps2 = ps2                                                                    tmp_ps = ps                                                                                    case 6:                            if mtext.tags.getpos("textureOnFloor") > LingoNumber(0):                                 rct = LingoGlobal.op_sub(LingoGlobal.rect(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),LingoGlobal.op_add(LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),LingoNumber(10)),LingoGlobal.op_mul(q,LingoNumber(20)),LingoGlobal.op_mul(c,LingoNumber(20))),LingoGlobal.op_mul(LingoGlobal.rect(self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                                pxli = LingoImage.Pxl                                pxlr = LingoGlobal.rect(LingoNumber(0),LingoNumber(0),LingoNumber(1),LingoNumber(1))                                wh = _global.color(LingoNumber(255),LingoNumber(255),LingoNumber(255))                                d = -LingoNumber(1)                                for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl.count):                                     ps = tmp_ps                                    gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(LingoGlobal.op_mul(size.locv,LingoNumber(20)),LingoGlobal.op_sub(ps,LingoNumber(1)))))                                    for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), mtext.repeatl[ps]):                                         ps2 = tmp_ps2                                        d = LingoGlobal.op_add(d,LingoNumber(1))                                        if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                             break                                                                                    else:                                            lstr = _global.str(LingoGlobal.op_add(d,dp))                                            lri = _global.member(LingoGlobal.concat("layer",lstr)).image                                            lri.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                            lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))
                                            if LingoGlobal.ToBool(colored):                                                 if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                     lri = _global.member(LingoGlobal.concat("layer",lstr,"dc")).image                                                    lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))
                                                    lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                                                                            if LingoGlobal.ToBool(effectcolora):                                                 lri = _global.member(LingoGlobal.concat("gradientA",lstr)).image                                                lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))
                                                lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                            if LingoGlobal.ToBool(effectcolorb):                                                 lri = _global.member(LingoGlobal.concat("gradientB",lstr)).image                                                lri.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))
                                                lri.copypixels(pxli,rct,pxlr,LingoPropertyList(color=wh))                                                                                    tmp_ps2 = ps2                                                                            tmp_ps = ps                                                                                                                                                            match lematrixt if value is not None else 9999999999:                     case 1:                        if LingoGlobal.op_ne_b(mattl.findpos(block), LingoGlobal.VOID):                             fl = mattl.block                            rct2 = LingoGlobal.op_sub(LingoGlobal.rect(LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_add(LingoGlobal.op_mul(q,LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_add(LingoGlobal.op_mul(c,LingoNumber(20)),LingoNumber(5))),LingoGlobal.op_mul(LingoGlobal.rect(self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                            colored = LingoGlobal.op_gt(fl.tags.getpos("colored"),LingoNumber(0))                            if LingoGlobal.ToBool(colored):                                 self.gAnyDecals = LingoNumber(1)                                                            effectcolora = LingoGlobal.op_gt(fl.tags.getpos("effectColorA"),LingoNumber(0))                            effectcolorb = LingoGlobal.op_gt(fl.tags.getpos("effectColorB"),LingoNumber(0))                            tlrnd = fl.rnd                            rnd = LingoGlobal.op_sub(_global.random(tlrnd),LingoNumber(1))                            matfile = _global.member("MatImport")                            if LingoGlobal.op_ne_b(self.DRLastMatImp, nm):                                 _global.member("MatImport").importfileinto(LingoGlobal.concat("Materials",_global.the_dirSeparator,nm,".png"))
                                matfile.name = "MatImport"                                self.DRLastMatImp = nm                                                            matimg = matfile.image                            for tmp_f in LingoGlobal.pyrange(LingoNumber(1), LingoNumber(4)):                                 f = tmp_f                                match f if value is not None else 9999999999:                                     case 1:                                        profl = LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)))                                        gtatv = LingoNumber(2)                                        pstrect = LingoGlobal.op_add(rct2,LingoGlobal.rect(LingoNumber(0),LingoNumber(0),-LingoNumber(10),-LingoNumber(10)))                                                                            case 2:                                        profl = LingoList(LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1)))                                        gtatv = LingoNumber(4)                                        pstrect = LingoGlobal.op_add(rct2,LingoGlobal.rect(LingoNumber(10),LingoNumber(0),LingoNumber(0),-LingoNumber(10)))                                                                            case 3:                                        profl = LingoList(LingoGlobal.point(LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)))                                        gtatv = LingoNumber(6)                                        pstrect = LingoGlobal.op_add(rct2,LingoGlobal.rect(LingoNumber(10),LingoNumber(10),LingoNumber(0),LingoNumber(0)))                                                                            case _:                                         profl = LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1)))                                        gtatv = LingoNumber(8)                                        pstrect = LingoGlobal.op_add(rct2,LingoGlobal.rect(LingoNumber(0),LingoNumber(10),-LingoNumber(10),LingoNumber(0)))                                                                                                            id = ""                                for tmp_dr in profl:                                     dr = tmp_dr                                    id = LingoGlobal.concat(id,_global.str(self.lismytilesetopentothistile(nm,LingoGlobal.op_add(qcp,dr),l)))                                                                    if LingoGlobal.op_eq_b(id, "11"):                                     if LingoList(LingoNumber(1),LingoNumber(2),LingoNumber(3),LingoNumber(4),LingoNumber(5)).getpos(self.lismytilesetopentothistile(nm,LingoGlobal.op_add(LingoGlobal.op_add(qcp,profl[LingoNumber(1)]),profl[LingoNumber(2)]),l)) > LingoNumber(0):                                         gtath = LingoNumber(10)                                        gtatv = LingoNumber(2)                                                                            else:                                        gtath = LingoNumber(8)                                                                                                            else:                                    gtath = LingoList(LingoNumber(0),"00",LingoNumber(0),"01",LingoNumber(0),"10").getpos(id)                                                                    if LingoGlobal.op_eq_b(gtath, LingoNumber(4)):                                     if LingoGlobal.op_eq_b(gtatv, LingoNumber(6)):                                         gtatv = LingoNumber(4)                                                                            elif LingoGlobal.op_eq_b(gtatv, LingoNumber(8)):                                         gtatv = LingoNumber(2)                                                                                                            elif LingoGlobal.op_eq_b(gtath, LingoNumber(6)):                                     if (LingoGlobal.op_eq_b(gtatv, LingoNumber(4)) or LingoGlobal.op_eq_b(gtatv, LingoNumber(8))):                                         gtatv = LingoGlobal.op_sub(gtatv,LingoNumber(2))                                                                                                            bsrect = LingoGlobal.rect(LingoGlobal.op_add(LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(gtath,LingoNumber(1)),LingoNumber(10)),LingoNumber(5)),LingoGlobal.op_mul(LingoNumber(100),rnd)),LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(gtatv,LingoNumber(1)),LingoNumber(10)),LingoNumber(5)),LingoGlobal.op_add(LingoGlobal.op_add(LingoGlobal.op_mul(gtath,LingoNumber(10)),LingoNumber(5)),LingoGlobal.op_mul(LingoNumber(100),rnd)),LingoGlobal.op_add(LingoGlobal.op_mul(gtatv,LingoNumber(10)),LingoNumber(5)))                                if ((LingoGlobal.ToBool(colored) or LingoGlobal.ToBool(effectcolora)) or LingoGlobal.ToBool(effectcolorb)):                                     gradrect = LingoGlobal.rect(LingoGlobal.op_mul(LingoNumber(100),tlrnd),LingoNumber(0),LingoGlobal.op_mul(LingoNumber(100),tlrnd),LingoNumber(0))                                                                    d = -LingoNumber(1)                                for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl.count):                                     ps = tmp_ps                                    gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(LingoNumber(80),LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(LingoNumber(80),LingoGlobal.op_sub(ps,LingoNumber(1)))))                                    for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl[ps]):                                         ps2 = tmp_ps2                                        d = LingoGlobal.op_add(d,LingoNumber(1))                                        if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                             break                                                                                    else:                                            lstr = _global.str(LingoGlobal.op_add(d,dp))                                            _global.member(LingoGlobal.concat("layer",lstr)).image.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                            if LingoGlobal.ToBool(colored):                                                 if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                     _global.member(LingoGlobal.concat("layer",lstr,"dc")).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))                                                                                            if LingoGlobal.ToBool(effectcolora):                                                 _global.member(LingoGlobal.concat("gradientA",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                            if LingoGlobal.ToBool(effectcolorb):                                                 _global.member(LingoGlobal.concat("gradientB",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                                                                    tmp_ps2 = ps2                                                                            tmp_ps = ps                                                                    tmp_f = f                                                                                                        case 2 | 3 | 4 | 5:                        if LingoGlobal.op_ne_b(mattl.findpos(slope), LingoGlobal.VOID):                             matfile = _global.member("MatSlpImport")                            if LingoGlobal.op_ne_b(self.DRLastSlpImp, nm):                                 _global.member("MatSlpImport").importfileinto(LingoGlobal.concat("Materials",_global.the_dirSeparator,nm,"Slopes.png"))
                                matfile.name = "MatSlpImport"                                self.DRLastSlpImp = nm                                                            fl = mattl.slope                            matimg = matfile.image                            tlrnd = fl.rnd                            rnd = LingoGlobal.op_sub(_global.random(tlrnd),LingoNumber(1))                            colored = LingoGlobal.op_gt(fl.tags.getpos("colored"),LingoNumber(0))                            if LingoGlobal.ToBool(colored):                                 self.gAnyDecals = LingoNumber(1)                                                            effectcolora = LingoGlobal.op_gt(fl.tags.getpos("effectColorA"),LingoNumber(0))                            effectcolorb = LingoGlobal.op_gt(fl.tags.getpos("effectColorB"),LingoNumber(0))                            slp = self.gLEProps.matrix[q][c][l][LingoNumber(1)]                            askdirs = LingoList(LingoNumber(0),LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),LingoNumber(1))),LingoList(LingoGlobal.point(LingoNumber(0),LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0))),LingoList(LingoGlobal.point(-LingoNumber(1),LingoNumber(0)),LingoGlobal.point(LingoNumber(0),-LingoNumber(1))),LingoList(LingoGlobal.point(LingoNumber(0),-LingoNumber(1)),LingoGlobal.point(LingoNumber(1),LingoNumber(0))))                            myaskdirs = askdirs[slp]                            pstrect = LingoGlobal.op_sub(LingoGlobal.rect(LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_add(LingoGlobal.op_mul(q,LingoNumber(20)),LingoNumber(5)),LingoGlobal.op_add(LingoGlobal.op_mul(c,LingoNumber(20)),LingoNumber(5))),LingoGlobal.op_mul(LingoGlobal.rect(self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                            if ((LingoGlobal.ToBool(colored) or LingoGlobal.ToBool(effectcolora)) or LingoGlobal.ToBool(effectcolorb)):                                 gradrect = LingoGlobal.rect(LingoGlobal.op_mul(LingoNumber(120),tlrnd),LingoNumber(0),LingoGlobal.op_mul(LingoNumber(120),tlrnd),LingoNumber(0))                                                            for tmp_ad in LingoGlobal.pyrange(LingoNumber(1), myaskdirs.count):                                 ad = tmp_ad                                bsrect = LingoGlobal.rect(LingoGlobal.op_add(LingoGlobal.op_add(LingoNumber(5),LingoGlobal.op_mul(LingoNumber(60),LingoGlobal.op_eq(ad,LingoNumber(2)))),LingoGlobal.op_mul(LingoNumber(120),rnd)),LingoGlobal.op_add(LingoNumber(5),LingoGlobal.op_mul(LingoNumber(30),LingoGlobal.op_sub(slp,LingoNumber(2)))),LingoGlobal.op_add(LingoGlobal.op_add(LingoNumber(35),LingoGlobal.op_mul(LingoNumber(60),LingoGlobal.op_eq(ad,LingoNumber(2)))),LingoGlobal.op_mul(LingoNumber(120),rnd)),LingoGlobal.op_add(LingoNumber(35),LingoGlobal.op_mul(LingoNumber(30),LingoGlobal.op_sub(slp,LingoNumber(2)))))                                if LingoGlobal.ToBool(self.lismytilesetopentothistile(nm,LingoGlobal.op_add(qcp,myaskdirs[ad]),l)):                                     bsrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(30),LingoNumber(0),LingoNumber(30),LingoNumber(0)))                                                                    d = -LingoNumber(1)                                for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl.count):                                     ps = tmp_ps                                    gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(LingoNumber(130),LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(LingoNumber(130),LingoGlobal.op_sub(ps,LingoNumber(1)))))                                    for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl[ps]):                                         ps2 = tmp_ps2                                        d = LingoGlobal.op_add(d,LingoNumber(1))                                        if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                             break                                                                                    else:                                            lstr = _global.str(LingoGlobal.op_add(d,dp))                                            _global.member(LingoGlobal.concat("layer",lstr)).image.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                            if LingoGlobal.ToBool(colored):                                                 if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                     _global.member(LingoGlobal.concat("layer",lstr,"dc")).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))                                                                                            if LingoGlobal.ToBool(effectcolora):                                                 _global.member(LingoGlobal.concat("gradientA",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                            if LingoGlobal.ToBool(effectcolorb):                                                 _global.member(LingoGlobal.concat("gradientB",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                                                                    tmp_ps2 = ps2                                                                            tmp_ps = ps                                                                    tmp_ad = ad                                                                                                        case 6:                        if LingoGlobal.op_ne_b(mattl.findpos(floor), LingoGlobal.VOID):                             matfile = _global.member("MatFlrImport")                            if LingoGlobal.op_ne_b(self.DRLastFlrImP, nm):                                 _global.member("MatFlrImport").importfileinto(LingoGlobal.concat("Materials",_global.the_dirSeparator,nm,"Floor.png"))
                                matfile.name = "MatFlrImport"                                self.DRLastFlrImP = nm                                                            fl = mattl.floor                            matimg = matfile.image                            tlrnd = fl.rnd                            rnd = LingoGlobal.op_sub(_global.random(tlrnd),LingoNumber(1))                            colored = LingoGlobal.op_gt(fl.tags.getpos("colored"),LingoNumber(0))                            if LingoGlobal.ToBool(colored):                                 self.gAnyDecals = LingoNumber(1)                                                            effectcolora = LingoGlobal.op_gt(fl.tags.getpos("effectColorA"),LingoNumber(0))                            effectcolorb = LingoGlobal.op_gt(fl.tags.getpos("effectColorB"),LingoNumber(0))                            vbf = LingoGlobal.op_mul(LingoNumber(20),fl.bftiles)                            pstrect = LingoGlobal.op_sub(LingoGlobal.rect(LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(q,LingoNumber(1)),LingoNumber(20)),vbf),LingoGlobal.op_sub(LingoGlobal.op_mul(LingoGlobal.op_sub(c,LingoNumber(1)),LingoNumber(20)),vbf),LingoGlobal.op_add(LingoGlobal.op_mul(q,LingoNumber(20)),vbf),LingoGlobal.op_add(LingoGlobal.op_mul(c,LingoNumber(20)),vbf)),LingoGlobal.op_mul(LingoGlobal.rect(self.gRenderCameraTilePos,self.gRenderCameraTilePos),LingoNumber(20)))                            bfcal = LingoGlobal.op_add(LingoNumber(20),LingoGlobal.op_mul(LingoNumber(40),fl.bftiles))                            bsrect = LingoGlobal.rect(LingoNumber(0),LingoNumber(1),bfcal,LingoGlobal.op_add(bfcal,LingoNumber(1)))                            bsrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoGlobal.op_mul(bsrect.width,rnd),LingoNumber(0),LingoGlobal.op_mul(bsrect.width,rnd),LingoNumber(0)))                            if ((LingoGlobal.ToBool(colored) or LingoGlobal.ToBool(effectcolora)) or LingoGlobal.ToBool(effectcolorb)):                                 gradrect = LingoGlobal.rect(LingoGlobal.op_mul(bfcal,tlrnd),LingoNumber(0),LingoGlobal.op_mul(bfcal,tlrnd),LingoNumber(0))                                                            d = -LingoNumber(1)                            for tmp_ps in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl.count):                                 ps = tmp_ps                                gtrect = LingoGlobal.op_add(bsrect,LingoGlobal.rect(LingoNumber(0),LingoGlobal.op_mul(bfcal,LingoGlobal.op_sub(ps,LingoNumber(1))),LingoNumber(0),LingoGlobal.op_mul(bfcal,LingoGlobal.op_sub(ps,LingoNumber(1)))))                                for tmp_ps2 in LingoGlobal.pyrange(LingoNumber(1), fl.repeatl[ps]):                                     ps2 = tmp_ps2                                    d = LingoGlobal.op_add(d,LingoNumber(1))                                    if LingoGlobal.op_add(d,dp) > LingoNumber(29):                                         break                                                                            else:                                        lstr = _global.str(LingoGlobal.op_add(d,dp))                                        _global.member(LingoGlobal.concat("layer",lstr)).image.copypixels(matimg,pstrect,gtrect,LingoPropertyList(ink=LingoNumber(36)))
                                        if LingoGlobal.ToBool(colored):                                             if (LingoGlobal.op_eq_b(effectcolora, LingoNumber(0)) and LingoGlobal.op_eq_b(effectcolorb, LingoNumber(0))):                                                 _global.member(LingoGlobal.concat("layer",lstr,"dc")).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(36)))                                                                                    if LingoGlobal.ToBool(effectcolora):                                             _global.member(LingoGlobal.concat("gradientA",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                        if LingoGlobal.ToBool(effectcolorb):                                             _global.member(LingoGlobal.concat("gradientB",lstr)).image.copypixels(matimg,pstrect,LingoGlobal.op_add(gtrect,gradrect),LingoPropertyList(ink=LingoNumber(39)))                                                                            tmp_ps2 = ps2                                                                    tmp_ps = ps                                                                                                                                                    return None            