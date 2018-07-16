# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

execfile('../model_data.py')
execfile('../loadStateData.py')

pathGrph='res_PI_PF_OD_104_41/graphics/loads/'   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile='res_PI_PF_OD_104_41/report_loads.tex'  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2a,G2b,G2c,G3,Q1a,Q1a_1via,Q1b,Q1c,Q2b,A1a,A1b,C1]
grWidth='110mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,grWdt=grWidth)

textfl.close()
  
