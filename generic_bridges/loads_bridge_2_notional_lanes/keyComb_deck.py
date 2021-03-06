# -*- coding: utf-8 -*-
from actions import combinations as cc
#Combinaciones determinantes en el diseño de armaduras (para tanteo rápido)

combContainer= cc.CombContainer()
#Tablero (tensiones normales)
combContainer.ULS.perm.add("ELU007" , "1.00*G12 + 1.00*G3 + 1.35*Q1a1 + 0.90*Q33") 
combContainer.ULS.perm.add("ELU010" , "1.00*G12 + 1.00*G3 + 1.35*Q1a1 + 0.90*Q22") 
combContainer.ULS.perm.add("ELU034" , "1.00*G12 + 1.00*G3 + 1.35*Q1c + 0.90*Q22") 
combContainer.ULS.perm.add("ELU076" , "1.00*G12 + 1.00*G3 + 0.6*Q1e + 1.50*Q33")
combContainer.ULS.perm.add("ELU120" , "1.00*G12 + 1.35*G3 + 1.35*Q1c + 0.90*Q22") 
combContainer.ULS.perm.add("ELU179" , "1.35*G12 + 1.00*G3 + 1.35*Q1a1 + 0.90*Q33") 
combContainer.ULS.perm.add("ELU182" , "1.35*G12 + 1.00*G3 + 1.35*Q1a1 + 0.90*Q22") 
combContainer.ULS.perm.add("ELU190" , "1.35*G12 + 1.00*G3 + 1.35*Q1b1 + 0.90*Q34") 
combContainer.ULS.perm.add("ELU192" , "1.35*G12 + 1.00*G3 + 1.35*Q1b1 + 0.90*Q32") 
combContainer.ULS.perm.add("ELU198" , "1.35*G12 + 1.00*G3 + 1.35*Q1b2 + 0.90*Q32") 
combContainer.ULS.perm.add("ELU215" , "1.35*G12 + 1.00*G3 + 1.35*Q1e + 0.90*Q33") 
combContainer.ULS.perm.add("ELU268" , "1.35*G12 + 1.35*G3 + 1.35*Q1a1 + 0.90*Q22") 
combContainer.ULS.perm.add("ELU286" , "1.35*G12 + 1.35*G3 + 1.35*Q1b2 + 0.90*Q22") 
combContainer.ULS.perm.add("ELU291" , "1.35*G12 + 1.35*G3 + 1.35*Q1c + 0.90*Q31") 
combContainer.ULS.perm.add("ELU292" , "1.35*G12 + 1.35*G3 + 1.35*Q1c + 0.90*Q22") 
combContainer.ULS.perm.add("ELU298" , "1.35*G12 + 1.35*G3 + 1.35*Q1d + 0.90*Q22") 
combContainer.ULS.perm.add("ELU305" , "1.35*G12 + 1.35*G3 + 1.35*Q1bFren") 
#Pilas (tensiones normales)(además de "ELU305")
combContainer.ULS.perm.add("ELU220" , "1.35*G12 + 1.00*G3 + 1.35*Q1dFren") 
combContainer.ULS.perm.add("ELU306" , "1.35*G12 + 1.35*G3 + 1.35*Q1dFren") 
combContainer.ULS.perm.add("ELU308" , "1.35*G12 + 1.35*G3 + 1.50*Q21") 
#Pilas (cortante)(además de "ELU305")
combContainer.ULS.perm.add("ELU047" , "1.00*G12 + 1.00*G3 + 1.35*Q1bFren") 
combContainer.ULS.perm.add("ELU133" , "1.00*G12 + 1.35*G3 + 1.35*Q1bFren") 
combContainer.ULS.perm.add("ELU135" , "1.00*G12 + 1.35*G3 + 1.35*Q1eFren") 
#Tablero (cortante)(además de ELU305,ELU182)
combContainer.ULS.perm.add("ELU210" , "1.00*G12 + 1.00*G3 + 1.50*G4 + 0.60*Q1a1 + 1.50*Q4") 
combContainer.ULS.perm.add("ELU214" , "1.00*G12 + 1.35*G3 + 1.00*G4 + 1.35*Q1a1 + 0.90*Q33") 
combContainer.ULS.perm.add("ELU218" , "1.00*G12 + 1.35*G3 + 1.00*G4 + 1.35*Q1a2") 
combContainer.ULS.perm.add("ELU297" , "1.00*G12 + 1.35*G3 + 1.00*G4 + 0.60*Q1e + 1.50*Q34") 
combContainer.ULS.perm.add("ELU304" , "1.00*G12 + 1.35*G3 + 1.00*G4 + 1.50*Q4") 

