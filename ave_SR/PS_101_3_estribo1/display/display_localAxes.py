# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../../PSs/captionTexts.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

    # display_local_axes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #    viewDef:        camera parameters (position, orientation,...)
    #                   options: "XYZPos","XYZNeg", "XPos", "XNeg","YPos","YNeg"
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")

    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

qg.display_local_axes(prep=prep,setToDisplay=zap,vectorScale=0.15,viewDef= vtk_graphic_base.CameraParameters('XYZPos',2.0),caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
qg.display_local_axes(prep=prep,setToDisplay=murestr,vectorScale=0.15,viewDef= vtk_graphic_base.CameraParameters('XYZPos',2.0),caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
qg.display_local_axes(prep=prep,setToDisplay=aleti,vectorScale=0.15,vtk_graphic_base.CameraParameters('XYZPos'),caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
qg.display_local_axes(prep=prep,setToDisplay=aletd,vectorScale=0.15,vtk_graphic_base.CameraParameters('XYZPos'),caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)



