from molemass import *
mols=["CHHCHH","COHF","KNOOO"]
for mol in mols:
    print("%s MW= %f"%(mol,molemass(mol)))