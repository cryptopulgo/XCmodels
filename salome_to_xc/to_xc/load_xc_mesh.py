# -*- coding: utf-8 -*-

import xc_base
import geom
import xc
from model import predefined_spaces


import pickle
import NeutralMeshDescription

fName= "Mesh_1"
meshes= NeutralMeshDescription.loadMeshes(fName)

# Problem type
prueba= xc.FEProblem()
preprocessor= prueba.getPreprocessor
nodos= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodos)

for key in meshes:
  print "Loading mesh: ", key
  mesh= meshes[key]
  for nId in mesh.nodeCoords:
    coords= mesh.nodeCoords[nId].coords
    nodos.newNodeIDXYZ(nId,coords[0],coords[1],coords[2])
