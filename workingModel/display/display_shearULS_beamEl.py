# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import control_var_diagram as cvd

execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile(cfg.verifShearFile)

#  Config
argument= 'CF'      #Available arguments: 'CF', 'N', 'My', 'Mz', 'Mu',
                     #'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'CF'
setsDispRes=[beamY]   #list of linear elements sets for which
                                    #to display results 
setDisp=overallSet   #set of elements (any type) to be displayed
scaleFactor=1     #scale factor for the diagram (can be negative)
fUnitConv=1          #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
#  End config 

diagram= cvd.ControlVarDiagram(scaleFactor=scaleFactor,fUnitConv=fUnitConv,sets=setsDispRes,attributeName=lsd.shearResistance.label,component=argument)
diagram.addDiagram()
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
defDisplay.setupGrid(setDisp)
defDisplay.defineMeshScene(None,defFScale=0.0)
defDisplay.appendDiagram(diagram)
caption= cfg.capTexts[lsd.shearResistance.label] + ', ' + cfg.capTexts[argument] + '. '+ setsDispRes[0].description.capitalize() 
defDisplay.displayScene(caption)
