ALL_STATS = {'Position Types': {'Td', 'Gp', 'Gu', 'Pos'},
             'Execution Prefix': {'cl', 'n', 'ct', '+', '-', '='},
             'Base Stats': {'GTD', 'FSW', 'SLTD', 'DLTD', 'Th', 'CTD', 'SCT', 'GUP', 'Sd',
                            'GP', 'OB', 'Sw', 'LEE', 'PA', 'PT', 'PE', 'PL', 'Pin', 'Sub',
                            'Pen', 'Warning', 'Rv', 'AlSu', 'fSu', 'Scr', 'Bt'},
             'Execution Suffix': {'ch', 'a', 'ag'}}

TYPES = {'Takedown': ['GTD', 'FSW', 'SLTD', 'DLTD', 'Th', 'CTD'],
         'Standing': ['SCT', 'GUP', 'Sd'],
         'Guard Pass': ['GP'],
         'Guard': ['OB', 'Sw'],
         'Leg Entanglement': ['LEE'],
         'Position': ['PA', 'PT', 'PE', 'PL', 'Pin'],
         'Submission': ['Sub'],
         'Penalty/Warning': ['Pen', 'Warning'],
         'Reversal': ['Rv'],
         'Stand-ups': ['AlSu', 'fSu'],
         'Scramble': ['Scr'],
         'Back Take': ['Bt']
         }

# Stats that do not have an easy opposite statistic
# ex: PL -> cPE or PR vise versa
# ex: +Scr -> -Scr
SPECIAL_STATS = {'PL': {'cPE', 'PR'},
                 '+Scr': '-Scr', '-Scr': '+Scr', '=Scr': '=Scr'}


# STATS WITH NO (L), (M), (R)
NO_DIRECTION = {'PA', 'PT', 'PE', 'PL', 'Pin', 'Pen', 'AlSu',
                'fSu', 'Scr', 'Bt', 'SCT', 'P', 'Warning'}  # P is Depreciated

CHANGE_DIRECTION = {'DLTD', 'SLTD', 'GP', 'OB', 'Sw'}

DIRECTION_WARNING = {'FSW', 'Sw', 'OB', 'CTD', 'Th'}



# Some stats are linked with other stats
# ex: Bt [PA, PT]
LINKED_STATS = {'Bt': ['PT, PA'], }