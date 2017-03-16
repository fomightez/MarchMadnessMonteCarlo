"""
This is March Madness Monte Carlo code, originally written by Michael Lerner
and described on his [blog](http://www.mglerner.com/blog/?p=16), then modified
by Daniel Smith and posted to
[github](https://github.com/Daniel-B-Smith/MarchMadnessMonteCarlo) and forked
back by Michael Lerner on his own
[github](https://github.com/mglerner/MarchMadnessMonteCarlo) project.

Check out the blog post for a nice summary.
"""

__date__ = 2017
__version__ = 0.2

from collections import namedtuple
SimulationResults = namedtuple('SimulationResults','brackets unique_brackets lowest_bracket lowest_bracket_count most_common_bracket most_common_bracket_count')

from numpy.random import random #import only one function from somewhere
#from Brackets import *
#from Stats import *
#from JeffSagarin import *
#from KenPomeroy import *
#from Stats import *
#from MonteCarloBrackets import simulate
#from RankingsAndStrength import *
#from RankingsAndStrength import teams

def set_energy_function(ef):
    import Brackets as B
    if ef == 'default':
        B.energy_game = B.default_energy_game
    else:
        B.energy_game = ef

        
# Could be St. Mary's instead of Middle Tennessee
# Could be Liberty instead of North Carolina A&T.
teams = {}
if __date__ == 2013:
    teams['midwest'] = ['Louisville','North Carolina A&T','Colorado St.','Missouri',
                        'Oklahoma St.','Oregon','St. Louis','New Mexico St.',
                        'Memphis',"St. Mary's",'Michigan St.','Valparaiso',
                        'Creighton','Cincinnati','Duke','Albany']

    #Could be La Salle instead of Boise St.
    teams['west'] = ['Gonzaga','Southern','Pittsburgh','Wichita St.',
                     'Wisconsin','Mississippi','Kansas St.','La Salle',
                     'Arizona','Belmont','New Mexico','Harvard',
                     'Notre Dame','Iowa St.','Ohio St.','Iona']

    teams['south'] = ['Kansas','Western Kentucky','North Carolina','Villanova',
                      'Virginia Commonwealth','Akron','Michigan','South Dakota St.',
                      'UCLA','Minnesota','Florida','Northwestern St.',
                      'San Diego St.','Oklahoma','Georgetown','Florida Gulf Coast']

    # Could be Long Island instead of James Madison
    teams['east'] = ['Indiana','James Madison','North Carolina St.','Temple',
                     'Nevada Las Vegas','California','Syracuse','Montana',
                     'Butler','Bucknell','Marquette','Davidson',
                     'Illinois','Colorado','Miami FL','Pacific']
elif __date__ == 2015:
    teams['midwest'] = ['Kentucky','Hampton','Cincinnati','Purdue',
                        'West Virginia','Buffalo','Maryland','Valparaiso',
                        'Butler','Texas','Notre Dame','Northeastern',
                        'Wichita St.','Indiana','Kansas','New Mexico St.']
    # Could be MISS instead of BYU
    teams['west'] = ['Wisconsin','Coastal Carolina','Oregon','Oklahoma St.',
                     'Arkansas','Wofford','North Carolina','Harvard',
                     'Xavier','Mississippi','Baylor','Georgia St.',
                     'VCU','Ohio St.','Arizona','Texas Southern',
                     ]
    # Could be Boise State instead of Dayton
    teams['east'] = ['Villanova','Lafayette','North Carolina St.','LSU',
                     'Northern Iowa','Wyoming','Louisville','UC Irvine',
                     'Providence','Dayton','Oklahoma','Albany',
                     'Michigan St.','Georgia','Virginia','Belmont']
    # Could be University of North Florida instead of Robert Morris
    teams['south'] = ['Duke','Robert Morris','San Diego St.',"St. John's",
                      'Utah','Stephen F. Austin','Georgetown','Eastern Washington',
                      'SMU','UCLA','Iowa St.','UAB',
                      'Iowa','Davidson','Gonzaga','North Dakota St.']
elif __date__ == 2017:
    teams['midwest'] = ['Kansas','N.C. Cent','Miami FL','Michigan St.',
                        'Iowa St.','Nevada','Purdue','Vermont',
                        'Creighton','Rhode Island','Oregon','Iona',
                        'Michigan','Oklahoma St.','Louisville','Jax. State']
    teams['south'] = ['N. Carolina','Texas So.','Arkansas','Seton Hall',
                      'Minnesota','Middle Tenn.','Butler','Winthrop',
                      'Cincinnati','Kansas St.','UCLA','Kent St.',
                      'Dayton','Wichita St.','Kentucky','N. Kentucky']
    teams['east'] = ['Villanova',"Mt St Mary's",'Wisconsin','Va. Tech',
                     'Virginia','UNC Wilm.','Florida','ETSU',
                     'SMU','Providence','Baylor','New Mex. St.',
                     'S. Carolina','Marquette','Duke','Troy']
    teams['west'] = ['Gonzaga','S. Dak. St.','Northwestern','Vanderbilt',
                     'Notre Dame','Princeton','W. Virginia','Bucknell',
                     'Maryland','Xavier','Florida St.','FGCU',
                     "St. Mary's", "VCU", "Arizona", 'North Dakota']
else:
    raise ImportError('Unknown bracket date: {v}'.format(v=__date__))

# These are all listed in the same order:
_rankings = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
regional_rankings = {}
for region in teams:
    for (team,rank) in zip(teams[region],_rankings):
        # We use a random number here so that the south's number 2
        # seed won't come out exactly the same rank as the west's.
        regional_rankings[team] = rank + random()/10

regions = {}
for region in teams:
    for team in teams[region]:
        regions[team] = region

all_teams = teams['midwest'] + teams['south'] + teams['west'] + teams['east']

teams['all'] = all_teams


from Brackets import Bracket, simulate, runbracket1, runbracket2, playgame, maketable
from Visualization import showstats
