# -*- coding: utf-8 -*-
import os
from postprocess import RC_material_distribution
from postprocess import element_section_map

# Reinforced concrete material distribution over the elements of the FE model.
# Concrete of type concrete02 with tension stiffening branch

execfile("../model_gen.py") #FE model generation

#RC-sections definition file.
execfile(path_model_slab_bridge+"RC_sections_def.py")

#list of RC sections (from those whose attributes (materials, geometry, refinforcement, set of elements to which apply, ... are defined in the file 'RC_sections_def.py') that we want to process in order to run different limit-state checkings.
lstOfSectRecords=[deckRCSects,footRCSects,wallRCSects,beamXRCsect,beamYRCsect,columnZRCsect]

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()

sections= reinfConcreteSectionDistribution.sectionDefinition #sections container

#Generation of 2 fiber sections (1 and 2 direction) for each record in list
#lstOfSectRecords. Inclusion of these section-groups in the sections container
for secRec in lstOfSectRecords:
    secRec.concrType.initTensStiff='Y' #tension stiffening initialized in
                                       #concrete material diagram
    secRec.creaTwoSections()    
    sections.append(secRec)

#Generation of the distribution of material extended to the elements of the
#FE model, assigning to each element the section-group that corresponds to it
for secRec in lstOfSectRecords:
    elset=prep.getSets.getSet(secRec.elemSetName)
    reinfConcreteSectionDistribution.assign(elemSet=elset.getElements,setRCSects=secRec)
reinfConcreteSectionDistribution.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
reinfConcreteSectionDistribution.dump()
