# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
preprocessor= model.getPreprocessor()
fName= cfg.projectDirTree.getVerifShearFile()
execfile(fName)
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportShearGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.shearResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsToReport=[deckSet]
# Ordered list of arguments to be included in the report
# Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argsToReport= ['CF','N', 'My', 'Mz','Vu'] 
texReportFile= cfg.projectDirTree.getReportShearFile()  #laTex file where to include the graphics 
cfg.grWidth='120mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsToReport=setsToReport,argsToReport=argsToReport,capTexts=capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth)

