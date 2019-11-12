# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

preprocessor=prep

#Load properties to display:
fName=  cfg.projectDirTree.getVerifCrackFreqFile()
execfile(fName)



limitStateLabel= lsd.freqLoadsCrackControl.label
#Possible arguments: 'getMaxSteelStress', 'getCF'
argument= 'getMaxSteelStress'

setDisp= losCim
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None,defFScale=0.0)



