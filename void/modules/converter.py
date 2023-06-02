# MODULES
from .statics import CHANGE_DIRECTION, DIRECTION_WARNING, ALL_STATS
from .Errors.error_types import ErrorTypes


# @property
class Converter():    

    def __init__(self, stat_obj_list, converted_stats = None):
        self.stat_obj_list = stat_obj_list
        if converted_stats is None:
            self.converted_stats = []
        


    #Changes the direction of stats
        # ex: (L)GPa -> (R)GPaag

    @staticmethod
    def __direction__( stat_obj) -> None:
        if stat_obj.direction:
            if stat_obj.stat in CHANGE_DIRECTION:
                case = stat_obj.direction
                match case:
                    case 'L':
                        stat_obj.direction = 'R'
                    case 'R':
                        stat_obj.direction = 'L'
        
        if stat_obj.stat in DIRECTION_WARNING:
            ErrorTypes.WARNING(stat_obj.full_stat, 20)

    @staticmethod
    def __postion__(stat_obj):
        case = stat_obj.position
        match case:
            case 'Gp':
                stat_obj.position = 'Gu'
            case 'Gu':
                stat_obj.position = 'Gp'


    #Adds an ag(against) or removes ag for all appropriate stats
    @staticmethod
    def __suffix__(stat_obj) -> None:
        if 'ag' in stat_obj.suffixes:
            stat_obj.suffixes.remove('ag')
        if stat_obj.stat in ALL_STATS['Base Stats'] and stat_obj.stat != 'Scr':
            stat_obj.suffixes.append('ag')


    def convert(self):
        for stat in self.stat_obj_list:
            Converter.__direction__(stat)
            Converter.__postion__(stat)
            Converter.__suffix__(stat)

    def merge(self):
        for stat in self.stat_obj_list:
            suffixes = ''.join(stat.suffixes)
            new_stat = f'({stat.direction}){stat.position}{stat.prefixes}{stat.stat}{suffixes}'
            print(stat.full_stat, new_stat)
            self.converted_stats.append(new_stat)
        return self.converted_stats
        
    
if __name__ == '__main__':

    stat_list = ['(L)FSWa',
                 '(R)FSWa',
                 '(R)FSWag',
                 'GUPag',
                 '(R)GpSubaag',
                 '(R)GPa',
                 'GPcha',
                 '(R)GPch',
                 'PL',
                 'Pin',
                 '(L)GpLEEaag',
                 'GPcha',
                 '(L)GPch',
                 'PosnBt',
                 'PL',
                 'Pin',
                 '(M)GPa',
                 '(M)GPa',
                 '(M)GPa',
                 '(M)GP',
                 '(R)PosSuba',
                 'Pin',
                 'PosfSuaag',
                 'PosfSuag',
                 'Sd',
                 '(M)GTDa',
                 '(M)GTD',
                 'GPcha',
                 '(L)GPa',
                 '(R)OBag',
                 '(R)GPa',
                 '(R)OBag',
                 '(R) GpLEEaag',
                 '(R)GpLEEag',
                 '(R)GpSuba',
                 '(M)GPaag',
                 '(M)OB',
                 'GufSua',
                 '(L)GSubaag]']

    conv = Converter(stat_obj_list=stat_list)

    conv.convert()

    