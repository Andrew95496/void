# MODULES
from .statics import CHANGE_DIRECTION, DIRECTION_WARNING, SPECIAL_STATS, LINKED_STATS
from .Errors.error_types import ErrorTypes
from .color_code import bcolors as bc
from .logger import LOGGER


# @property
class Converter(): 

    __slots__: tuple[str] = ('stat_obj_list', 'converted_stats')   

    def __init__(self, stat_obj_list: list[object], converted_stats: list[object] = None):
        self.stat_obj_list = stat_obj_list
        if converted_stats is None:
            self.converted_stats = []
        


    #Changes the direction of stats
        # ex: (L)GPa -> (R)GPaag

    @staticmethod
    def __direction__(stat_obj: object, athlete: str, opponent: str) -> None:
        if stat_obj.direction:
            if stat_obj.stat in CHANGE_DIRECTION:
                case = stat_obj.direction
                match case:
                    case 'L':
                        stat_obj.direction = 'R'
                    case 'R':
                        stat_obj.direction = 'L'
        
        if stat_obj.stat in DIRECTION_WARNING:
            log = ErrorTypes.WARNING(stat_obj.full_stat, 20, opponent)
            logger = LOGGER(athlete)
            logger.log(log)


    @staticmethod
    def __postion__(stat_obj: object):
        case = stat_obj.position
        match case:
            case 'Gp':
                stat_obj.position = 'Gu'
            case 'Gu':
                stat_obj.position = 'Gp'


    #Adds an ag(against) or removes ag for all appropriate stats
    @staticmethod
    def __suffix__(stat_obj: object) -> None:
        if 'ag' in stat_obj.suffixes:
            # print(stat_obj.full_stat, stat_obj.suffixes)
            stat_obj.suffixes.remove('ag')
        elif 'ag' not in stat_obj.suffixes and stat_obj.stat != 'Scr':
            stat_obj.suffixes.append('ag')

    @staticmethod
    def __links__(stat_obj: object, athlete: str, opponent: str):
        if stat_obj.stat in LINKED_STATS:
            log = ErrorTypes.WARNING(stat_obj.full_stat, 21, opponent)
            logger = LOGGER(athlete)
            logger.log(log, msg=LINKED_STATS[stat_obj.stat])

    @staticmethod
    def __special__(stat_obj: object, athlete: str, opponent: str):
           

        case = stat_obj.prefixes
        match case:
            case '+':
                stat_obj.prefixes = '-'
            case '-':
                stat_obj.prefixes = '+'
        
        

    def convert(self, athlete: str, opponent: str) -> None:
        for stat in self.stat_obj_list:
            Converter.__links__(stat, athlete, opponent)
            if stat.stat in SPECIAL_STATS:
                Converter.__special__(stat, athlete,opponent)
            else:
                Converter.__direction__(stat, athlete,opponent)
                Converter.__postion__(stat)
                Converter.__suffix__(stat)

    def merge(self) -> list:
        for stat in self.stat_obj_list:
            if stat.full_stat in ('Warning', 'Pen', 'NOT VALID'):
                self.converted_stats.append(stat.stat)
                # print(f'{bc.FAIL}{stat.full_stat}{bc.ENDC}', '->', f'{bc.OKBLUE}{stat.full_stat}{bc.ENDC}')
            elif stat.stat == 'NOT VALID':
                self.converted_stats.append(f'({stat.full_stat}){stat.stat}')
                # print(f'{bc.FAIL}{stat.full_stat}{bc.ENDC}', '->', f'{bc.BOLD}{bc.UNDERLINE}{bc.OKCYAN}{stat.stat}{bc.ENDC}{bc.ENDC}{bc.ENDC}')
            else:
                if stat.direction == '':
                    suffixes = ''.join(stat.suffixes)
                    new_stat = f'{stat.position}{stat.prefixes}{stat.stat}{suffixes}'
                    # print(f'{bc.FAIL}{stat.full_stat}{bc.ENDC}', '->', f'{bc.OKBLUE}{new_stat}{bc.ENDC}')
                    self.converted_stats.append(new_stat)
                else:
                    suffixes = ''.join(stat.suffixes)
                    new_stat = f'({stat.direction}){stat.position}{stat.prefixes}{stat.stat}{suffixes}'
                    # print(f'{bc.FAIL}{stat.full_stat}{bc.ENDC}','->', f'{bc.OKBLUE}{new_stat}{bc.ENDC}')
                    self.converted_stats.append(new_stat)
        return self.converted_stats
        


    