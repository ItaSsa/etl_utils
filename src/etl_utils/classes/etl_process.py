import pandas as pd

class ETLProcess:
    def __init__(self, data_source):
        self.data_source = data_source

    def extract_data(self):
        raise NotImplementedError("Method extract_data should be implemented in the child classes.")

    def transform_data (self, data):
        raise NotImplementedError("Method transform_data  should be implemented in the child classes.")

    def load_data(self, transformed_data):
        raise NotImplementedError("Method load_data should be implemented in the child classes.")

    def run_etl(self,file_path):
        extract_data = self.extract_data()
        transformed_data = self.transform_data (extract_data)
        self.load_data(transformed_data,file_path)


class EtlCsv(ETLProcess):
    def extract_data(self):
        return pd.read_csv(self.data_source)

    def transform_data (self, data):
        # Simple transformation: converting all uppercase letters
        return data.applymap(lambda x: x.upper() if isinstance(x, str) else x)

    def load_data(self, transformed_data, file_path):
        transformed_data.to_parquet(file_path,engine="pyarrow" , index=False)
        print("Transformed data:")
        print(transformed_data)


# Exemplo de uso
if __name__ == "__main__":
    csv_source = 'src/etl_utils/data/csv_file_test.csv'  # Substitua 'dados.csv' pelo caminho do seu arquivo CSV
    etl_csv = EtlCsv(csv_source)
    etl_csv.run_etl("src/etl_utils/data/dados.parquet")