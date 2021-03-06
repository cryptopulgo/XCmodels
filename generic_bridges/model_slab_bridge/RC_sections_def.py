# -*- coding: utf-8 -*-

#import os
# import xc_base
# import geom
# import xc
from materials.sections.fiber_section import def_simple_RC_section as rcs
from postprocess import element_section_map
#from materials.ehe import EHE_materials
from materials.ec2 import EC2_materials
import math

#Armaduras
execfile('../arm_def.py')

rnom=35 #recubrimiento nominal 

#instances of element_section_map.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element
#losa [losaZonaArm1,losaZonaArm2, ...]
losaRCSects=[]
for st in  sets_arm_losa:
    losaRCSects.append(element_section_map.RCSlabBeamSection(name=st.name+'RCSects',sectionDescr='losa, zona de armado '+st.name[-2:],concrType=concrete, reinfSteelType=reinfSteel,depth=cantoLosa,elemSet=st))
#cartabón derecho interno [CartIntZonaArm1,CartIntZonaArm2, ...]
cartIntRCSects=[]
for st in  sets_arm_cartInt:
    cartIntRCSects.append(element_section_map.RCSlabBeamSection(name=st.name+'RCSects',sectionDescr='cartabón interno, zona de armado '+st.name[-2:],concrType=concrete, reinfSteelType=reinfSteel,depth=eCartInt,elemSet=st))
#cartabón derecho externo [CartExtZonaArm1,CartExtZonaArm2, ...]
cartExtRCSects=[]
for st in  sets_arm_cartExt:
    cartExtRCSects.append(element_section_map.RCSlabBeamSection(name=st.name+'RCSects',sectionDescr='cartabón externo, zona de armado '+st.name[-2:],concrType=concrete, reinfSteelType=reinfSteel,depth=eCartExt,elemSet=st))
#voladizo derecho interno [VolIntZonaArm1,VolIntZonaArm2, ...]
volIntRCSects=[]
for st in  sets_arm_volInt:
    volIntRCSects.append(element_section_map.RCSlabBeamSection(name=st.name+'RCSects',sectionDescr='voladizo interno, zona de armado '+st.name[-2:],concrType=concrete, reinfSteelType=reinfSteel,depth=eVolInt,elemSet=st))
#voladizo derecho externo [VolExtZonaArm1,VolExtZonaArm2, ...]
volExtRCSects=[]
for st in  sets_arm_volExt:
    volExtRCSects.append(element_section_map.RCSlabBeamSection(name=st.name+'RCSects',sectionDescr='voladizo externo, zona de armado '+st.name[-2:],concrType=concrete, reinfSteelType=reinfSteel,depth=eVolExt,elemSet=st))
#Riostra estribo
RestrRCSects=element_section_map.RCSlabBeamSection(name='RestrRCSects',sectionDescr='riostra estribo',concrType=concrete, reinfSteelType=reinfSteel,depth=cantoRiostrEstr,elemSet=setArmREstr)
#Pilas
pilasRCSects=element_section_map.RCSlabBeamSection(name='pilasRCSects',sectionDescr='pilas',concrType=concrete, reinfSteelType=reinfSteel,width=lRectEqPila,depth=lRectEqPila,elemSet=setArmPil)


def armaduraLosa(RCSet,recNom,arm1,arm2,arm4,arm5,arm6a,arm6b,arm7,arm8,arm9a,arm9b,arm10,ref1Inf,ref2Sup,ref3Mid,cercosRef,cercos):
    '''armaduras losa o riostra estribo. Diámetros armadura y separación en mm.
    arm1: losa, trasv inf. [diam,sep]
    arm2: cartabón, trasv inf. [diam,sep]
    arm4: voladizo, trasv inf. [diam,sep]
    arm5: losa, trasv sup. [diam,sep]
    arm6a: losa, long.inf. [diam,sep]
    arm6b: losa, long.inf.(2ª capa) [diam,sep]. Si=None, no aplica
    arm7: cartabón, long. inf. [diam,sep]
    arm8: voladizo, long. inf. [diam,sep]
    arm9a: losa, long. sup. [diam,sep]
    arm9b: losa, long. sup.(2ª capa) [diam,sep]. Si=None, no aplica
    arm10: voladizo, long. sup. [diam,sep]
    ref1Inf: refuerzo transversal inferior. Si=None, no aplica
    ref2Sup: refuerzo transversal superior. Si=None, no aplica
    ref3Mid: refuerzo transversal medio canto. Si=None, no aplica
    cercosRef: refuerzo cercos
    cercos: armadura de cortante en losa
    '''
    RCSet.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm5[0],arm5[1],rnom)]) #transv. sup.
    RCSet.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm1[0],arm1[1],rnom)]) #transv. inf.
    RCSet.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm9a[0],arm9a[1],rnom+arm5[0])]) #long. sup.
    RCSet.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm6a[0],arm6a[1],rnom+arm1[0])]) #long. inf.
    recNomTrSup=rnom+arm5[0]+arm9a[0]
    if arm9b:
        RCSet.dir2PositvRebarRows.append(rcs.rebLayer_mm(arm9b[0],arm9b[1],recNomTrSup)) #long. sup. 2a. capa
        recNomTrSup+=arm9b[0]
    if arm6b:
        RCSet.dir2NegatvRebarRows.append(rcs.rebLayer_mm(arm6b[0],arm6b[1],rnom+arm1[0]+arm6a[0])) #long. inf. 2a. capa
    if ref2Sup:
        RCSet.dir1PositvRebarRows.append(rcs.rebLayer_mm(ref2Sup[0],ref2Sup[1],recNomTrSup))  #refuerzo armadura transversal superior
    if ref1Inf:
        RCSet.dir1NegatvRebarRows.append(rcs.rebLayer_mm(ref1Inf[0],ref1Inf[1],rnom+arm1[0]+arm6a[0])) #refuerzo armadura transversal inferior
    if ref3Mid:
        RCSet.dir1NegatvRebarRows.append(rcs.rebLayer_mm(ref3Mid[0],ref3Mid[1],RCSet.depth/2.))
    if cercosRef:
        RCSet.dir2PositvRebarRows.append(rcs.rebLayer_mm(cercosRef[0],cercosRef[2],recNomTrSup)) #long. sup. 2a. capa
        RCSet.dir2NegatvRebarRows.append(rcs.rebLayer_mm(cercosRef[0],cercosRef[2],rnom+arm1[0]+arm6a[0])) #long. inf. 2a. capa
    # armadura de cortante
    if len(cercos)>0:
        areaCercos=math.pi*(cercos[0]*1e-3)**2/4.
        nRamas=cercos[1]
        separ=cercos[2]*1e-3
        if cercosRef:
            areaCercosRef=math.pi*(cercosRef[0]*1e-3)**2/4.
            nRamasRef=cercosRef[1]
            separRef=cercosRef[2]*1e-3
            areaCercoEquiv=(nRamas*areaCercos/separ+nRamasRef*areaCercosRef/separRef)/nRamas*separ
            areaCercos=areaCercoEquiv
        RCSet.dir1ShReinfY=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=nRamas,areaShReinfBranch=areaCercos,shReinfSpacing=separ,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
        RCSet.dir2ShReinfY=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=cercos[1],areaShReinfBranch= math.pi*(cercos[0]*1e-3)**2/4.,shReinfSpacing=separ,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
     
def armaduraZonas(nZona,recNom,losaRC,cartIntRC,cartExtRC,volIntRC,volExtRC,arm1,arm2,arm4,arm5,arm6a,arm6b,arm7,arm8,arm9a,arm9b,arm10,arm1P,arm2P,arm3P,arm4P,cercos):
    '''armaduras definidas para una zona de armado. Diámetros armadura y separación en mm.

    nZona: nº zona armado
    recNom: recubrimiento
    arm1: losa, trasv inf. [diam,sep]
    arm2: cartabón, trasv inf. [diam,sep]
    arm4: voladizo, trasv inf. [diam,sep]
    arm5: losa, trasv sup. [diam,sep]
    arm6a: losa, long.inf. [diam,sep]
    arm6b: losa, long.inf.(2ª capa) [diam,sep]. Si=None, no aplica
    arm7: cartabón, long. inf. [diam,sep]
    arm8: voladizo, long. inf. [diam,sep]
    arm9a: losa, long. sup. [diam,sep]
    arm9b: losa, long. sup.(2ª capa) [diam,sep]. Si=None, no aplica
    arm10: voladizo, long. sup. [diam,sep]
    arm1P: refuerzo transversal inferior en riostra pila. Si=None, no aplica
    arm2P: refuerzo transversal superior en riostra pila. Si=None, no aplica
    arm3P: refuerzo transversal medio canto en riostra pila. Si=None, no aplica
    arm4P: cercos refuerzo cortante en riostra pila. Si=None, no aplica
    cercos: armadura de cortante en losa
    '''
    #armaduras losa
    RCSet=losaRC[nZona-1]
    armaduraLosa(RCSet,recNom,arm1,arm2,arm4,arm5,arm6a,arm6b,arm7,arm8,arm9a,arm9b,arm10,arm1P,arm2P,arm3P,arm4P,cercos)
    #armaduras cartabón
    RCSets=[cartIntRC[nZona-1],cartExtRC[nZona-1]]
    for RCSet in RCSets:
        RCSet.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm5[0],arm5[1],rnom)]) #transv. sup.
        RCSet.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm2[0],arm2[1],rnom)]) #transv. inf.
        RCSet.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm9a[0],arm9a[1],rnom+arm5[0])]) #long. sup.
        RCSet.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm7[0],arm7[1],rnom+arm2[0])]) #long. inf.
        if arm9b:
            RCSet.dir2PositvRebarRows.append(rcs.rebLayer_mm(arm9b[0],arm9b[1],rnom+arm5[0]+arm9a[0])) #long. sup. 2a. capa
    #armaduras voladizo
    RCSets=[volIntRC[nZona-1],volExtRC[nZona-1]]
    for RCSet in RCSets:
        RCSet.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm5[0],arm5[1],rnom)]) #transv. sup.
        RCSet.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm4[0],arm4[1],rnom)]) #transv. inf.
        RCSet.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm10[0],arm10[1],rnom+arm5[0])]) #long. sup.
        RCSet.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(arm8[0],arm8[1],rnom+arm4[0])]) #long. inf.


#Armaduras riostra estribo 1
armaduraLosa(RCSet=RestrRCSects,recNom=rnom,
              arm1=trInf_los_020L1,
              arm2=trInf_cart_020L1,
              arm4=trInf_vol_020L1,
              arm5=trSup_020L1,
              arm6a=lnInf_base_los_L1,
              arm6b=None,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L1,
              arm9a=lnSup_base_loscart_L1,
              arm9b=None,
              arm10=lnSup_vol_L1,
              ref1Inf=trInf_ref_Restr,
              ref2Sup=trSup_ref_Restr,
              ref3Mid=trMid_ref_Restr,
              cercosRef=cercos_Ref,
              cercos=cercos_020L1)

#Armaduras zona 1 (0.2*Lvano1)
armaduraZonas(nZona=1,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los_020L1,
              arm2=trInf_cart_020L1,
              arm4=trInf_vol_020L1,
              arm5=trSup_020L1,
              arm6a=lnInf_base_los_L1,
              arm6b=None,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L1,
              arm9a=lnSup_base_loscart_L1,
              arm9b=None,
              arm10=lnSup_vol_L1,
              arm1P=None,
              arm2P=None,
              arm3P=None,
              arm4P=None,
              cercos=cercos_020L1)
    
#Armaduras zona 2 (vano 1 centro: 0.2*Lvano1 -> 0.2*Lvano2)
armaduraZonas(nZona=2,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los,
              arm2=trInf_cart_L1cent,
              arm4=trInf_vol_L1cent,
              arm5=trSup_L1cent,
              arm6a=lnInf_base_los_L1,
              arm6b=lnInf_ref_los_L1,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L1,
              arm9a=lnSup_base_loscart_L1,
              arm9b=None,
              arm10=lnSup_vol_L1,
              arm1P=None,
              arm2P=None,
              arm3P=None,
              arm4P=None,
              cercos=cercos_L1)
    
#Armaduras zona 3 (0.2*Lvano2 -> riostra pila)
armaduraZonas(nZona=3,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los,
              arm2=trInf_cart_L1cent,
              arm4=trInf_vol_020L2,
              arm5=trSup_020L2,
              arm6a=lnInf_base_los_L1,
              arm6b=None,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L1,
              arm9a=lnSup_base_loscart_Rpil,
              arm9b=lnSup_ref_loscart_020L2,
              arm10=lnSup_vol_020L2,
              arm1P=None,
              arm2P=None,
              arm3P=None,
              arm4P=None,
              cercos=cercos_020L2)
    
#Armaduras zona 4 (riostra pila)
armaduraZonas(nZona=4,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los,
              arm2=trInf_cart_Rpil,
              arm4=trInf_vol_020L2,
              arm5=trSup_Rpil,
              arm6a=lnInf_base_los_L2,
              arm6b=None,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L2,
              arm9a=lnSup_base_loscart_Rpil,
              arm9b=lnSup_ref_loscart_Rpil,
              arm10=lnSup_vol_020L2,
              arm1P=trInf_ref_Rpil,
              arm2P=trSup_ref_RPil,
              arm3P=trMid_ref_RPil,
              arm4P=cercos_Ref,
              cercos=cercos_Rpil)
    
#Armaduras zona 5 (riostra pila -> 0.2*Lvano2)
armaduraZonas(nZona=5,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los,
              arm2=trInf_cart_L2cent,
              arm4=trInf_vol_020L2,
              arm5=trSup_020L2,
              arm6a=lnInf_base_los_L2,
              arm6b=None,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L2,
              arm9a=lnSup_base_loscart_Rpil,
              arm9b=lnSup_ref_loscart_020L2,
              arm10=lnSup_vol_020L2,
              arm1P=None,
              arm2P=None,
              arm3P=None,
              arm4P=None,
              cercos=cercos_020L2)
    
#Armaduras zona 6 (vano 2 centro: 0.2*Lvano2 -> 0.5*Lvano2)
armaduraZonas(nZona=6,recNom=rnom,losaRC=losaRCSects,cartIntRC=cartIntRCSects,cartExtRC=cartExtRCSects,volIntRC=volIntRCSects,volExtRC=volExtRCSects,
              arm1=trInf_los,
              arm2=trInf_cart_L2cent,
              arm4=trInf_vol_L2,
              arm5=trSup_L2cent,
              arm6a=lnInf_base_los_L2,
              arm6b=lnInf_ref_los_L2,
              arm7=lnInf_cart,
              arm8=lnInf_vol_L2,
              arm9a=lnSup_base_loscart_L2,
              arm9b=None,
              arm10=lnSup_vol_L2,
              arm1P=None,
              arm2P=None,
              arm3P=None,
              arm4P=None,
              cercos=cercos_L2)
    

#armadura pilas
pilasRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(lnPil[0],lnPil[1],rnom)])
pilasRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(lnPil[0],lnPil[1],rnom)])
pilasRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(lnPil[0],lnPil[1],rnom)])
pilasRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(lnPil[0],lnPil[1],rnom)])

pilasRCSects.dir1ShReinfZ=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=cercosPil[1],areaShReinfBranch= math.pi*(cercosPil[0]*1e-3)**2/4.,shReinfSpacing=cercosPil[2]*1e-3,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
pilasRCSects.dir2ShReinfZ=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=cercosPil[1],areaShReinfBranch= math.pi*(cercosPil[0]*1e-3)**2/4.,shReinfSpacing=cercosPil[2]*1e-3,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)

pilasRCSects.dir1ShReinfY=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=cercosPil[1],areaShReinfBranch= math.pi*(cercosPil[0]*1e-3)**2/4.,shReinfSpacing=cercosPil[2]*1e-3,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
pilasRCSects.dir2ShReinfY=rcs.ShearReinforcement(familyName= "sh",nShReinfBranches=cercosPil[1],areaShReinfBranch= math.pi*(cercosPil[0]*1e-3)**2/4.,shReinfSpacing=cercosPil[2]*1e-3,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)


