# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph
from postprocess.xcVtk.FE_model import vtk_FE_graphic


execfile('../model_gen.py')

execfile(path_loads_def+'load_state_data.py')

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=LSD_disp
#loadCasesToDisplay=[Q31,Q32,Q33,Q34]
#loadCasesToDisplay=[G4]
#End data
for lc in loadCasesToDisplay:
#    lc.setsToDispBeamIntForc=[struts,ties]
    lc.setsToDispBeamIntForc=[setArmPil]
    lc.listBeamIntForc=['N','Vy','Vz']
for lc in loadCasesToDisplay:
    lcs=QGrph.QuickGraphics(FEcase)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            if arg[0]=='u':
                fcUn=lc.unitsScaleDispl
                unDesc=lc.unitsDispl
            else:
                fcUn=1.0
                unDesc=''
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fConvUnits=fcUn,unitDescription=unDesc,viewDef= lc.cameraParameters,fileName=None,defFScale=1)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc

            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fConvUnits= fcUn,unitDescription=unDesc,viewDef= lc.cameraParameters,fileName=None,defFScale=1)
    #Internal forces displays on sets of «beam» elements
    for st in lc.setsToDispBeamIntForc:
        for arg in lc.listBeamIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
                scaleFact=lc.scaleDispBeamIntForc[2]
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc
                if arg[0]=='N':
                  scaleFact=lc.scaleDispBeamIntForc[0]
                else:
                  scaleFact=lc.scaleDispBeamIntForc[1]
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st,fConvUnits= fcUn,scaleFactor=scaleFact,unitDescription=unDesc,viewDef= lc.cameraParametersBeams,fileName=None,defFScale=1)
    if abutment.lower()[0]=='y': 
        defDisplay= vtk_FE_graphic.RecordDefDisplayEF() 
        found_wink.displayPressures(defDisplay,lc.loadCaseName +'Ground pressures',fUnitConv= 1e-6,unitDescription= '[MPa]')


            
