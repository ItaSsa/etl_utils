import pandas as pd

class CsvProcessor:
    def __init__(self,file_path:str):
        self.file_path = file_path
        self.df = None
        self.df_filtered = pd.DataFrame()
    
    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df 
    
    def filter_as(self,column:str, attribute:str):
        self.df_filtered = self.df[ self.df[column] == attribute] #applying filter collumn for attribute
        return self.df_filtered
    
    def sub_filter(self, column:str, attribute:str):
        return self.df_filtered[ self.df_filtered[column] == attribute] 
    
    def recursive_filter_as(self,columns:list[str], attribute:list[str]):

        if len(columns) != len(attribute):
            raise ValueError("You should inform the same number of columns and attributes")

        if len(columns) == 0: 
            return self.df
        
        current_column = columns[0]
        current_attribute = attribute[0]
        
        if self.df_filtered.empty:
            df_filtered = self.df[ self.df[current_column] == current_attribute]
            self.df_filtered = df_filtered
        else:
            df_filtered = self.df_filtered[ self.df_filtered[current_column] == current_attribute]

        if len(columns) == 1: #break condition
            return df_filtered 
        else:
            return self.recursive_filter_as(columns[1:], attribute[1:])# The rest of columns