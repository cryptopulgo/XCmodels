#             *** GEOMETRIC model (points, lines, surfaces) - SETS***0
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
sty=outSty.OutputStyle() 
out=outHndl.OutputHandler(modelSpace,sty)

# grid model definition (tablero)
gridTabl= gm.GridModel(prep,xListTabl,yListTabl,zListTabl)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridTabl.generatePoints()

#   Surfaces generation (tablero)
#Riostra estribo 1
x=xRiostrEstr[0]
y=yRiostrEstr[0]
z=zLosa[0]
riostrEstr1=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),setName='riostrEstr1')
#Riostra estribo 2
x=xRiostrEstr[1]
y=yRiostrEstr[1]
z=zLosa[0]
riostrEstr2=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),setName='riostrEstr2')
#Losa
x=xLosa
y=yLosa
z=zLosa[0]
losa=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),setName='losa')
#Cartabones
x=xCartab
y=yLosa
z=zLosa[0]
cartabInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], setName='cartabInt')
cartabExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], setName='cartabExt')
#Voladizos
x=xVoladz
y=yLosa
z=zLosa[0]
voladzInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], setName='voladzInt')
voladzExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], setName='voladzExt')



#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
# Isotropic elastic section-material appropiate for plate and shell analysis
riostrEstr_mat=tm.DeckMaterialData(name='riostrEstr_mat',thickness= cantoRiostrEstr,material=concrProp)
riostrEstr_mat.setupElasticSection(preprocessor=prep) 
losa_mat=tm.DeckMaterialData(name='losa_mat',thickness= cantoLosa,material=concrProp)
losa_mat.setupElasticSection(preprocessor=prep) 
cartabInt_mat=tm.DeckMaterialData(name='cartabInt_mat',thickness=eCartInt,material=concrProp)
cartabInt_mat.setupElasticSection(preprocessor=prep) 
cartabExt_mat=tm.DeckMaterialData(name='cartabExt_mat',thickness=eCartExt,material=concrProp)
cartabExt_mat.setupElasticSection(preprocessor=prep) 
voladzInt_mat=tm.DeckMaterialData(name='voladzInt_mat',thickness=eVolInt,material=concrProp)
voladzInt_mat.setupElasticSection(preprocessor=prep) 
voladzExt_mat=tm.DeckMaterialData(name='voladzExt_mat',thickness=eVolExt,material=concrProp)
voladzExt_mat.setupElasticSection(preprocessor=prep) 


#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them
riostrEstr1_mesh=fem.SurfSetToMesh(surfSet=riostrEstr1,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
riostrEstr2_mesh=fem.SurfSetToMesh(surfSet=riostrEstr2,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
losa_mesh=fem.SurfSetToMesh(surfSet=losa,matSect=losa_mat,elemSize=eSize,elemType='ShellMITC4')
cartabInt_mesh=fem.SurfSetToMesh(surfSet=cartabInt,matSect=cartabInt_mat,elemSize=eSize,elemType='ShellMITC4')
cartabExt_mesh=fem.SurfSetToMesh(surfSet=cartabExt,matSect=cartabExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExt_mesh=fem.SurfSetToMesh(surfSet=voladzExt,matSect=voladzExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzInt_mesh=fem.SurfSetToMesh(surfSet=voladzInt,matSect=voladzInt_mat,elemSize=eSize,elemType='ShellMITC4')

allmesh=[riostrEstr1_mesh,riostrEstr2_mesh,losa_mesh,cartabInt_mesh,cartabExt_mesh,voladzInt_mesh,voladzExt_mesh]
fem.multi_mesh(preprocessor=prep,lstMeshSets=allmesh)

