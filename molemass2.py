def molemass2(sequence):
    TotalAtomicMass=0
    Sym=["F","K","S","P","O","N","C","H"]
    MW=[18.998,39.098,32.066,30.973,15.999,14.006,12.010,1.007]
    Atoms_dict=dict(zip(Sym,MW))
    for i in range(len(sequence)):
        if sequence[i].isdigit()==True:
            TotalAtomicMass+=Atoms_dict[sequence[i-1]]*(int(sequence[i])-1)
        else:
            TotalAtomicMass+=Atoms_dict[sequence[i]]
    return TotalAtomicMass