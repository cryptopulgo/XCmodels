# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_normStrsULS.py'
execfile(fName)
execfile('../captionTexts.py')

pathGrph='text/graphics/normStrsULS/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.normalStressesResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[]
# Ordered list of arguments to be included in the report
# Possible arguments: 'CF', 'N', 'My', 'Mz'
argsShEl= []
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
setsBmElView=[[colsSet,'YPos']]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'CF', 'N', 'My', 'Mz'
argsBmElScale=[['CF',2.0]]

texReportFile='text/report_normStrsULS.tex'  #laTex file where to include the graphics 
grWidth='120mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts=capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt=grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)


