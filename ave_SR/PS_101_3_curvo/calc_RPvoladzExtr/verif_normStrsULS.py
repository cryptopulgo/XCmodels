# -*- coding: utf-8 -*-


import os

#Project directory structure
execfile('./directs.py')

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
#reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcement.pkl'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= SIA262_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(reinfConcreteSections)



