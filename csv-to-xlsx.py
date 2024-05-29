import os;
import pandas as pd;

input_folder = '/path/to/csv' # Path to the folder containing the CSV files (f.e.: r'C:\Users\user\Documents\csv')
output_folder = '/path/to/xlsx' # Path to the folder where the XLSX files will be saved (f.e.: r'C:\Users\user\Documents\xlsx')

os.makedirs(output_folder, exist_ok=True)

separator ='\t'

for file in os.listdir(input_folder):
    if file.endswith('.csv'):
        csv_path = os.path.join(input_folder, file)

        try:
            df = pd.read_csv(csv_path, encoding='utf-16', sep=separator)
        except Exception as e:
            print(f'Error reading {file}: {e}')
            continue
        
        xlsx_filename  = file.replace('.csv', '.xlsx')
        xls_path = os.path.join(output_folder, xlsx_filename)

        try:
            df.to_excel(xls_path, index=False, engine='openpyxl')
            print(f'{file} converted to {xlsx_filename}')
        except Exception as e:
            print(f'Error writing {file}: {e}')