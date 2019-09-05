# -*- coding: utf-8 -*-
from actions import combinations as cc
#Combinaciones determinantes en el diseño de armaduras (para tanteo rápido)
 
combContainer= cc.CombContainer()
#Muro estribo (combinaciones determinantes)
combContainer.ULS.perm.add("ELU355" , "1.00*G12 + 1.35*G3 + 1.50*G4 + 1.35*Q1e + 1.05*Q4") 
combContainer.ULS.perm.add("ELU406" , "1.00*G12 + 1.35*G3 + 1.50*G4 + 0.60*Q1e + 1.50*Q4") 
combContainer.ULS.perm.add("ELU560" , "1.35*G12 + 1.00*G3 + 1.50*G4 + 1.35*Q1e + 0.90*Q32") 
combContainer.ULS.perm.add("ELU562" , "1.35*G12 + 1.00*G3 + 1.50*G4 + 1.35*Q1e + 0.90*Q22")
#Aleta (combinaciones determinantes: "ELU406", "ELU405")
combContainer.ULS.perm.add("ELU405" , "1.00*G12 + 1.35*G3 + 1.50*G4 + 1.50*Q4") 
#Zapata (combinaciones determinantes: "ELU203", "ELU607","ELU759")
combContainer.ULS.perm.add("ELU203" , "1.00*G12 + 1.00*G3 + 1.50*G4 + 1.50*Q4") 
combContainer.ULS.perm.add("ELU607" , "1.35*G12 + 1.00*G3 + 1.50*G4 + 1.50*Q4") 
combContainer.ULS.perm.add("ELU759" , "1.35*G12 + 1.35*G3 + 1.50*G4 + 1.35*Q1e + 1.05*Q4") 
