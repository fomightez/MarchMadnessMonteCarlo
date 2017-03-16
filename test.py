#!/usr/bin/env python

import imp
from MarchMadnessMonteCarlo import KenPomeroy
imp.reload(KenPomeroy)
import MarchMadnessMonteCarlo as MMMC
imp.reload(MMMC)
teams = MMMC.teams['west']
from MarchMadnessMonteCarlo import student2017
ef = student2017.alex_energy_game
MMMC.set_energy_function(ef)

#print(student2017.anmol_map)
#print(student2017.rank_arr2)
#print(student2017.rank_arr2[41])
#print(student2017.rank_arr2[2])


print(ef('Vermont','Kansas'))
print(ef('Kansas','Vermont'))


#b = MMMC.Bracket(teams=teams,T=0.5)
#print (b)
