import os
import pandas as pd
import sqlite3
import re

# 获取指定目录下的所有csv
dir_path = '/item'
files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]


conn = sqlite3.connect('items.db')
c = conn.cursor()

for file in files:
    try:
        # 提取store_code并校验其格式
        store_code = re.search(r'JD_(\d+)', file).group(1)
        if not re.match(r'\d+', store_code):
            raise ValueError('Invalid store_code format')

        # 读取column_mapping.propties文件，获取所有的列名
        with open(os.path.join(dir_path, 'column_mapping.propties'), 'r') as f:
            columns = f.read().splitlines()

        # 检查csv文件中是否包含所有的列名，如果没有，打印缺少的列名
        df = pd.read_csv(os.path.join(dir_path, file))
        missing_columns = set(columns) - set(df.columns)
        if missing_columns:
            print(f'Missing columns in {file}: {missing_columns}')
            continue

        df['store_code'] = store_code
        df.to_sql('items', conn, if_exists='append', index=False)


        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, f'{file}.COMPLETED'))
    except Exception as e:

        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, f'{file}.FAILED'))
        print(f'Error processing {file}: {e}')

# 关闭数据库连接
conn.close()
