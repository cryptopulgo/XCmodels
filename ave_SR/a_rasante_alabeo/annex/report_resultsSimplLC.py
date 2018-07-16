# -*- coding: utf-8 -*-
#from postprocess.reports import graphical_reports

execfile('../model_data.py')
execfile('../loadStateData.py')


pathGrph='res_alabeo/graphics/resSimplLC/'   #directory to place the figures
                                        #(do not use ./text/....)'
texReportFile='res_alabeo/report_resSimplLC.tex'  #laTex file where to include the graphics

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1a,Q1a1via,Q1a_alabTot,Q1a1via_alabTot]
grWidth='110mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(FEproblem=FEcase,pathGr=pathGrph,texFile=textfl,grWdt=grWidth,capStdTexts=cfg.capTexts)

textfl.close()

