import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Date, Float, Integer
import config

def load_data(path):
    df = pd.read_csv(path)

    df['Date'] = df['Date'].map(lambda x: pd.to_datetime(x, format='%m/%d/%Y'))
    df['CustomerNo'] = df['CustomerNo'].astype(int, errors='ignore')

    conn_str = f"mssql+pyodbc://{config.DB_SERVER}/{config.DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
    engine = create_engine(conn_str)

    schema = {
        'TransactionNo': String,
        'Date': Date,
        'ProductNo': String,
        'ProductName': String,
        'Price': Float,
        'Quantity': Integer,
        'CustomerNo': Integer,
        'Country': String
    }

    df.to_sql('sales', con=engine, if_exists='replace', dtype=schema, index=False)

if __name__ == '__main__':
    path = '..\data\Sales Transaction v.4a.csv'
    load_data(path)
    print('Table created successfully!')