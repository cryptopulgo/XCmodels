# -*- coding: utf-8 -*-
#from postprocess.reports import graphical_reports

execfile('../model_data.py')
execfile('../loadStateData.py')
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportSimplLCGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportSimplLCFile()  #laTex file where to include the graphics

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1]
cfg.grWidth='120mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(FEproblem=FEcase,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth,capStdTexts=capTexts)

textfl.close()

