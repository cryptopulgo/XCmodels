# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import control_var_diagram as cvd

execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile(cfg.verifNormStrFile)

#  Config
argument= 'My'       #Possible arguments: 'CF', 'N', 'My', 'Mz'
setsDispRes=[beamX,beamY,columnZ]   #list of linear elements sets for which
                                    #to display results 
setDisp=overallSet   #set of elements (any type) to be displayed
scaleFactor=0.01        #scale factor for the diagram (can be negative)
fUnitConv=1          #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
#  End config 

diagram= cvd.ControlVarDiagram(scaleFactor=scaleFactor,fUnitConv=fUnitConv,sets=setsDispRes,attributeName= lsd.normalStressesResistance.label,component= argument)
diagram.addDiagram()
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.setupGrid(setDisp)
defDisplay.defineMeshScene(None,defFScale=0.0)
defDisplay.appendDiagram(diagram) 
caption= cfg.capTexts[lsd.normalStressesResistance.label] + ', ' + cfg.capTexts[argument] + '. '+ setsDispRes[0].description.capitalize() + ', ' 
defDisplay.displayScene(caption)



