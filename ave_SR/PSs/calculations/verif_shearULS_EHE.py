# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../project_directories.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution


lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory
lsd.LimitStateData.check_results_directory= '../'+check_results_directory

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for shear limit state according to SIA262
#from materials.sia262 import SIA262_limit_state_checking
#limitStateLabel= lsd.shearResistance.label
#lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
#meanFCs= lsd.shearResistance.check(reinfConcreteSections)

#Checking material for shear limit state according to EHE08
from materials.ehe import EHE_limit_state_checking
lsd.shearResistance.controller= EHE_limit_state_checking.ShearController(limitStateLabel= lsd.shearResistance.label)
#from solution import predefined_solutions
#lsd.shearResistance.controller.analysisToPerform= predefined_solutions.simple_newton_raphson
#(FEcheckedModel,meanFCs)= reinfConcreteSections.runChecking(lsd.shearResistance,outputFileName='/tmp/resVerif', matDiagType="d",threeDim= True)  
meanFCs= lsd.shearResistance.check(reinfConcreteSections)





