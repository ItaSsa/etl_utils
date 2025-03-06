import pandas as pd

class CsvProcessor:
    def __init__(self,file_path:str):
        self.file_path = file_path
        self.df = None
        self.df_filtered = None
    
    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df 
    
    def filter_as(self,column:str, attribute:str):
        self.df_filtered = self.df[ self.df[column] == attribute] #applying filter collumn for attribute
        return self.df_filtered
    
    def sub_filter(self, column:str, attribute:str):
        return self.df_filtered[ self.df_filtered[column] == attribute] 