import sqlite3
from typing import List

# Declare the DB name
DB_NAME = "heart_disease.db"


# The main table contains our input training data
main_table = """CREATE TABLE IF NOT EXISTS main_table ([patient_id] VARCHAR PRIMARY KEY NOT NULL,
                                                        [age] INTEGER NULL,
                                                        [gender] VARCHAR NULL,
                                                        [chest_pain_type] VARCHAR NULL, 
                                                        [resting_bp] INTEGER NULL, 
                                                        [cholestrol] INTEGER NULL, 
                                                        [fasting_bs] BOOL NULL, 
                                                        [resting_ecg] VARCHAR NULL, 
                                                        [max_hr] INTEGER NULL,
                                                        [exercise_angina] VARCHAR NULL, 
                                                        [old_peak] FLOAT NULL, 
                                                        [st_slope] VARCHAR NULL, 
                                                        [heart_disease] BOOL NULL);"""

table_lst = [main_table]


def create_tables(list_of_tables: List[str]):
    """
    :param list_of_tables: list of tables created with SQL command
    """
    sqlite_connection = sqlite3.connect(DB_NAME)
    cursor = sqlite_connection.cursor()
    print("Connected to the database")
    for table in list_of_tables:
        cursor.execute(table)
    sqlite_connection.commit()
    sqlite_connection.close()
    print("created_tables")


if __name__ == '__main__':
    # first drop tables if required or else keep it commented
    sqlite_connection = sqlite3.connect(DB_NAME)
    cursor = sqlite_connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS main_table;''')
    sqlite_connection.close()

    # create tables in the db
    create_tables(list_of_tables=table_lst)