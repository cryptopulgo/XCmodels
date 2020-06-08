# -*- coding: utf-8 -*-

execfile('model_data.py')
execfile('captionTexts.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
setToDisp= totalSet #impactOnBody #totalSet

displaySettings.FEmeshGraphic(xcSet= setToDisp,caption='Mesh',cameraParameters= vtk_graphic_base.CameraParameters('-X+Y+Z'),defFScale=1.0)


