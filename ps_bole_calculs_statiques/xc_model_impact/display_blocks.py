execfile('model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

setToDisp= totalSet
displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
displaySettings.displayBlocks(setToDisplay=setToDisp,caption= 'Model grid')


