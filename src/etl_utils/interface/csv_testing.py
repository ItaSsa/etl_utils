from etl_utils.classes.csv_class import CsvProcessor

v_file = "etl_utils/data/csv_file_test.csv"
v_filter_column = "state"
v_filter_attribute = 'SP'

v_csv_file = CsvProcessor(v_file)
v_csv_file.load_csv() #load csv
# # Filtering once
# v_df_filtered = v_csv_file.filter_as(v_filter_column,v_filter_attribute)
# print(v_df_filtered)

# #Filtering again
# v_df_filtered = v_csv_file.sub_filter('price',5.6)
# print(v_df_filtered)

v_df_filtered = v_csv_file.recursive_filter_as(['state','date'],['BA','21/01/2024'])
print(v_df_filtered)