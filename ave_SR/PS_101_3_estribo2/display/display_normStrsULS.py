# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


modelDataInputFile="../model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName= '../results/verifications/verifRsl_normStrsULS.py'
execfile(fName)
execfile('../../PSs/captionTexts.py')

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.elements,attributeName,1,2)

#Set of shell elements to display
#setDisp= shellsToCheck
setDisp= zap
#setDisp= murestr
#setDisp= aletd
#setDisp= aletiZ1+aletiZ2+aletiZ3
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None,defFScale=0.0)




