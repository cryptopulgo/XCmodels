# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
fName= model_path+check_results_directory+'verifRsl_fatigueULS.py'
execfile(fName)


pathGrph='res_a_rasante/graphics/fatigueStrsULS/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.fatigueResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[deck,found]
# Ordered list of arguments to be included in the report
#Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'
argsShEl= ['getAbsSteelStressIncrement','concreteBendingCF','concreteShearCF']
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
setsBmElView=[[beamX,'XYZPos']]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'
argsBmElScale=[['Mu',1],['Mu',1]]


texReportFile='res_a_rasante/report_fatigueStrsULS.tex'  #laTex file where to include the graphics 
grWidth='110mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts=fatg_capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt=grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

