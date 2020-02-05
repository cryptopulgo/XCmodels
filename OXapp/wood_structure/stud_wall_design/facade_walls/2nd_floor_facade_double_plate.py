# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

import math
import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.awc_nds import AWCNDS_materials as mat
from materials.awc_nds import dimensional_lumber
from postprocess import output_handler
import plates_model
import check

inchToMeter= 0.0254
title= '2nd floor facade double plate.'
studSpacing= 16.0*inchToMeter
trussSpacing= 24.0*inchToMeter
# Materials
# Spruce-pine-fir No. 2 
wood= dimensional_lumber.SprucePineFirWood(grade= 'no_2')
#wood= dimensional_lumber.SprucePineFirWood(grade= 'stud')
xc_material= wood.defXCMaterial()
plateSection= mat.DimensionLumber(name= '2x6',b= 5.5*inchToMeter, h= 1.5*inchToMeter, woodMaterial= wood)


# Reduction in uniform live loads.
AT= 2*15.0*5.0 # Tributary area
KLL= 2 # Live load element factor (ASCE-7 Table 4-2)
liveLoadReductionFactor= (0.25+4.57/math.sqrt(KLL*AT)) # ASCE-7 Eq. 4.7-1 (SI)
liveLoadReductionFactor= max(0.4,liveLoadReductionFactor) # Two or more floors
print('Live load reduction factor: ', liveLoadReductionFactor)


# Actions
## Load definition (values from truss_CD_reactions.ods)
deadLoad= 6.03e3 # kN/truss
liveLoad= liveLoadReductionFactor*8.78e3 # kN/truss
snowLoad= 6.13e3 # kN/truss
windLoad= -3.87e3 # kN/truss

doublePlate= plates_model.DoublePlate(title, plateSection, studSpacing, trussSpacing, pointLoadFactor= 1.0/2.0);

doublePlate.check( deadLoad, liveLoad, snowLoad, windLoad)
