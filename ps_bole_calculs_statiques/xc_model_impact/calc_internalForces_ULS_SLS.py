# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from solution import predefined_solutions


execfile("model_data.py")
lsd.LimitStateData.internal_forces_results_directory= './results/internalForces/'

#RC sections definition.
execfile("sectionsDef.py")

#Define section names for each element.

preprocessor= FEcase.getPreprocessor
reinfConcreteSectionDistribution.assign(elemSet=deckSet.getElements,setRCSects=deckRCSects)
reinfConcreteSectionDistribution.assign(elemSet=parapetBodySet.getElements,setRCSects=parapetBodyRCSects)
reinfConcreteSectionDistribution.assign(elemSet=parapetHeadSet.getElements,setRCSects=parapetHeadRCSects)

reinfConcreteSectionDistribution.dump()

#Set of entities for which checking is going to be performed.
#setCalc= shellElements.elSet
setCalc= shells

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
#lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 


# solution= predefined_solutions.SolutionProcedure()
# solution.convergenceTestTol= 1.0e-2
# solution.maxNumIter= 100
# solution.printFlag= 1

def customAnalysis(feProb,steps= 1):
  '''Default analysis procedure for saveAll method.'''
  #analysis= solution.penaltyNewtonRaphson(feProb)
  analysis= predefined_solutions.simple_static_linear(feProb)
  result= analysis.analyze(steps) #Same with the number of steps.
  return result

for ls in limitStates:
  ls.saveAll(FEcase,combContainer,setCalc,analysisToPerform= customAnalysis)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


