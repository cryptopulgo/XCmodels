# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

    # displayLocalAxes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   viewNm:         name of the view  that contains the renderer (possible
    #                   options: "XYZPos","XYZNeg", "XPos", "XNeg","YPos","YNeg"
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")

    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

setToDisp=overallSet    
qg.displayLocalAxes(prep=prep,setToDisplay=setToDisp,vectorScale=0.15,viewDef= vtk_graphic_base.CameraParameters('XYZPos',2.0),caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)



