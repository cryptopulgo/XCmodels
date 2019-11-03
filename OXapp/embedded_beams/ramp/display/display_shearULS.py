# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler

execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile(cfg.verifShearFile)


#  Config
argument= 'Vy'       #Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy',
                     #'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
setDisp= ramp

cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#rgMinMax=(0,1.0)     #truncate values to be included in the range
                     #(if None -> don't truncate)
rgMinMax=None
#  End config 


oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel=lsd.shearResistance.label,argument=argument,setToDisplay=setDisp,component=None,fileName=None,defFScale=0.0,rgMinMax=rgMinMax)




