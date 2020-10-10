def molemass(sequence):
    Elements=["F","K","S","P","O","N","C","H"]
    MW = [18.9984,39.0983,32.0660,30.9738,15.9994,14.0067,12.0107,1.0079]
    Atoms = dict(zip(Elements, MW))
    TotalAtomicMass=0
    for x in range(len(sequence)):
        TotalAtomicMass += Atoms[sequence[x]]
    return TotalAtomicMass