# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../captionTexts.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
import vtk

    # display_local_axes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   viewDef:        camera parameters (position, orientation,...)
    #                   options: "XYZPos", "XPos", "XNeg","YPos", "YNeg",
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")
    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

stDisp=beamSet  #set to display


model.display_local_axes(setToDisplay=stDisp.elSet,vectorScale=0.3,viewDef= vtk_graphic_base.CameraParameters('YPos'),caption= stDisp.genDescr.capitalize() + ', '+ capTexts['LocalAxes'])



