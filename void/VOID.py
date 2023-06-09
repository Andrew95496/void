import modules
import configs

import os
import pandas as pd

# * Home directory path
# print(os.path.expanduser('~'))

# load_dir = config['DEFAULTS']['LOAD_DIR']
# athletes = ast.literal_eval(config['DEFAULTS']['ATHLETES'])
# sheet_name = config['DEFAULTS']['SHEET_NAME']


# athlete: str | None = None, opponent: str | None = None, time: list[str] = None
class VOID():

    def __init__(self, dataframe: None | object = None, import_dir: str = configs.Config.IMPORT_DIR, export_dir: str = configs.Config.EXPORT_DIR, sheet_name: str = configs.Config.SHEET_NAME, athletes: list[str] = configs.Config.ATHLETES, tables: list[dict] | None = None, parsed_stats: list[dict] | None = None) -> None:
        self.dataframe = dataframe
        self.import_dir = import_dir
        self.export_dir = export_dir
        self.sheet_name = sheet_name
        self.athletes = athletes
        if tables is None:
            self.tables = {}
        if parsed_stats is None:
            self.parsed_stats = {}
        os.system(f'bash saves.sh {configs.Config.EXPORT_DIR} {modules.LOGGER.LOG_DIR}')


    def __tables__(self, athlete: str):
        dataframe = modules.File(athlete, f'{athlete}{self.sheet_name}', f'{self.import_dir}{athlete}.xlsx')
        dataframe = dataframe.import_excel()
        self.tables[athlete] = (dataframe)
        return self.tables
    
    def __parse__(self, athlete: str, dataframe: pd.DataFrame, opponent: str):
        _athlete = athlete.replace('_', ' ')
        stats = modules.stat_type.StatType()
        stat_col = stats.assign_type(dataframe['Stats'], athlete, opponent)
        self.parsed_stats[_athlete] = stat_col
        return self.parsed_stats.values()


    def __convert__(self, stat_col: list, dataframe: pd.DataFrame, athlete: str, opponent: str):
        convert = modules.converter.Converter(stat_col)
        convert.convert(athlete, opponent)
        new_stat_col = convert.merge()
        dataframe['Stats '] = new_stat_col
        dataframe.fillna("",inplace=True)
        # print('\n', dataframe.iloc[0:, [2, 7, 0, 3, 4, 5, 6]], '\n')
        new_dataframe = dataframe.iloc[0:, [2, 7, 0, 3, 4, 5, 6]]
        return new_dataframe
      
    def __export__(self, df: pd.DataFrame, export_dir: str, opponent_name: str):
        df.to_excel(f'{export_dir}/{opponent_name}.xlsx')

    def void(self):
        for athlete in void.athletes:
            try:
                tables = self.__tables__(athlete)
            except FileNotFoundError:
                print(f'{athlete} file not found')
                continue
            for dataframes in tables.values():
                for dataframe in dataframes:
                    opponent = dataframe.iloc[1][2]
                    parsed = self.__parse__(athlete, dataframe, opponent)
                    for stat_col in parsed:
                        new_dataframe = self.__convert__(stat_col, dataframe, athlete, opponent)
                        self.__export__(
                            new_dataframe, self.export_dir, opponent)

            void.parsed_stats.clear()  # Empties the dictionary for the next athlete



if __name__ == '__main__':
    void = VOID()

    void.void()


# TODO: parse and convert the 'Other Stats' column
