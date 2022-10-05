import pandas as pd
import sqlite3

DB_PATH = "heart_disease.db"


def transform_data(filename: str):
    """

    :param filename:
    :return:
    """
    data = pd.read_csv(filename)
    data.reset_index(inplace=True)

    data.rename(columns={'index': 'patient_id', 'Age': 'age', 'Sex': 'gender', 'ChestPainType': 'chest_pain_type',
                         'RestingBP': 'resting_bp',
                         'Cholesterol': 'cholesterol', 'FastingBS': 'fasting_bs', 'RestingECG': 'resting_ecg',
                         'MaxHR': 'max_hr', 'ExerciseAngina': 'exercise_angina', 'Oldpeak': 'old_peak',
                         'ST_Slope': 'st_slope', 'HeartDisease': 'heart_disease'}, inplace=True)

    # print(data.info())
    return data


def create_connection():
    """

    :return:
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor


def load_data(filename: str):
    connection, cursor = create_connection()
    print('connection_created')
    cleaned_df = transform_data(filename)
    lst = cleaned_df.values.tolist()
    print((lst))
    query = "INSERT INTO main_table(patient_id, age, gender, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, " \
            "max_hr, exercise_angina, old_peak, st_slope, heart_disease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
    try:
        cursor.executemany(query, lst)
        connection.commit()
        print('data_inserted')
    except Exception as e:
        print(str(e))
    connection.close()


if __name__ == '__main__':
    load_data('ETL_pipeline/data/heart-1.csv')
