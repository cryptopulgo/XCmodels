# -*- coding: utf-8 -*-
# AISC checking convenience functions.
from __future__ import division
from __future__ import print_function

def uls_check(profile, combinations, setToCheck, analysis):
    ''' Ad-hoc ultimate limit state checking routine.'''
    preprocessor= setToCheck.getPreprocessor
    nodes= preprocessor.getNodeHandler
    for comb in combinations:
        preprocessor.resetLoadCase()
        preprocessor.getLoadHandler.addToDomain(comb)
        result= analysis.analyze(1)
        nodes.calculateNodalReactions(True,1e-7)
        VMax= -1e23
        VMin= -VMax
        MMax= -1e23
        MMin= -MMax
        for e in setToCheck.elements:
          VMax= max(VMax,max(e.getV1, e.getV2))
          VMin= min(VMin,min(e.getV1, e.getV2))
          MMax= max(MMax,max(e.getM1, e.getM2))
          MMin= min(MMin,min(e.getM1, e.getM2))
        Vmax= max(VMax,abs(VMin))
        Mmax= max(MMax,abs(MMin))
        Phi_b= 0.90 # LRFD
        Mu= Phi_b*profile.getWz()*profile.steelType.fy
        if(Mmax<Mu):
            print('    '+comb, 'Mmax= ', Mmax/1e3, 'kN m < ',  Mu/1e3, 'kN m => OK')
        else:
            print('    '+comb, 'Mmax= ', Mmax/1e3, 'kN m > ',  Mu/1e3, 'kN m => KO')
        Phi_v= 1.0 # LRFD AISC Specification section G2.1a
        Vu= Phi_v*profile.getNominalShearStrengthWithoutTensionFieldAction()
        if(Vmax<Vu):
            print('    '+comb, 'Vmax= ', Vmax/1e3, 'kN < ',  Vu/1e3, 'kN => OK')
        else:
            print('    '+comb, 'Vmax= ', Vmax/1e3, 'kN > ',  Vu/1e3, 'kN => KO')

