#Armatures type
A08_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,8e-3,0.15,cover)
A10_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,10e-3,0.15,cover)
A12_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,12e-3,0.15,cover)
A14_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,14e-3,0.15,cover)
A16_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,16e-3,0.15,cover)
A18_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,18e-3,0.15,cover)
A20_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,20e-3,0.15,cover)
A22_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,22e-3,0.15,cover)
A26_15= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,26e-3,0.15,cover)

A08_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,8e-3,0.30,cover)
A10_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,10e-3,0.30,cover)
A12_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,12e-3,0.30,cover)
A14_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,14e-3,0.30,cover)
A16_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,16e-3,0.30,cover)
A18_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,18e-3,0.30,cover)
A20_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,20e-3,0.30,cover)
A22_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,22e-3,0.30,cover)
A26_30= ACI_limit_state_checking.ACIRebarFamily(reinfSteel,26e-3,0.30,cover)

D0810_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A08_30,A10_30)
D1012_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A10_30,A12_30)
D1214_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A12_30,A14_30)
D1416_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A14_30,A16_30)
D1618_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A16_30,A18_30)
D1820_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A18_30,A20_30)
D2022_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A20_30,A22_30)
D2226_15= ACI_limit_state_checking.ACIDoubleRebarFamily(A22_30,A26_30)
