import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib

# Load the model
clf_model = joblib.load("rfc_model.pkl")


# prepare the input data according to the processing of training data


def predict_hd(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,
               RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope):
    if Sex == 'F':
        Sex = '0'
    else:
        Sex = '1'

    if ChestPainType == 'ASY':
        ChestPainType = 0
    elif ChestPainType == 'ATA':
        ChestPainType = 1
    elif ChestPainType == 'NAP':
        ChestPainType = 2
    elif ChestPainType == 'TA':
        ChestPainType = 3

    if RestingECG == 'LVH':
        RestingECG = 0
    elif RestingECG == 'Normal':
        RestingECG = 1
    elif RestingECG == 'ST':
        RestingECG = 2

    if ExerciseAngina == 'N':
        ExerciseAngina = 0
    elif ExerciseAngina == 'Y':
        ExerciseAngina = 1

    if ST_Slope == 'Down':
        ST_Slope = 0
    elif ST_Slope == 'Flat':
        ST_Slope = 1
    elif ST_Slope == 'Up':
        ST_Slope = 2

    # Perform the prediction
    test_df = pd.DataFrame([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG,
                       MaxHR, ExerciseAngina, Oldpeak, ST_Slope]],
                     columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG',
                              'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])
    predict_output = clf_model.predict(test_df )
    probability = clf_model.predict_proba(test_df).tolist()


    fe = clf_model.feature_importances_.argsort()
    fig, ax = plt.subplots()
    ax.barh(test_df.columns[fe], clf_model.feature_importances_[fe])
    ax.set_xlabel("Feature Importance")
    ax.set_title('Feature Importance chart')

    return predict_output, probability, fig




st.title('Heart Disease Prediction')

st.header('Enter the mandatory categorical fields')

Sex = st.selectbox('Sex:', ['F', 'M'])
ChestPainType = st.selectbox('ChestPainType:', ['ASY', 'ATA', 'NAP', 'TA'])
RestingECG = st.selectbox('RestingECG:', ['LVH', 'Normal', 'ST'])
ExerciseAngina = st.selectbox('ExerciseAngina:', ['N', 'Y'])
ST_Slope = st.selectbox('ST_Slope:', ['Down', 'Flat', 'Up'])

st.header('Enter the mandatory readings fields')
Age = st.number_input('Age:', min_value=0, max_value=100, value=1)
RestingBP = st.number_input('RestingBP:', min_value=0, max_value=1000, value=1)
Cholesterol = st.number_input('Cholesterol:', min_value=0, max_value=1000, value=1)
FastingBS = st.number_input('FastingBS:', min_value=0, max_value=100, value=1)
MaxHR = st.number_input('MaxHR:', min_value=0, max_value=1000, value=1)
Oldpeak = st.number_input('Oldpeak:', min_value=0, max_value=100, value=1)


if st.button('Predict Heart Disease'):
    hd, proba, fig = predict_hd(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG,
                       MaxHR, ExerciseAngina, Oldpeak, ST_Slope)
    # print(hd, proba, fig)
    st.success(f'The overall prediction is {hd[0]}')
    st.success(f'The patient has around {round(proba[0][1],2)*100} chances of having a heart disease')

    st.header('Legend')
    col1, col2 = st.columns(2)
    col1.metric("No heart disease", "0")
    col2.metric("Yes heart disease", "1")


    st.header('Factors affecting the prediction in decreasing order')
    st.pyplot(fig=fig)

    st.header('For more information check below')

    st.text("Age: age of the patient [years]")
    st.text("Sex: gender of the patient [M: Male, F: Female]")
    st.text("ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]")
    st.text("RestingBP: resting blood pressure [mm Hg]")
    st.text("Cholesterol: serum cholesterol [mm/dl]")
    st.text("FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]")
    st.text("RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions "
                "and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular "
                "hypertrophy by Estes' criteria]")
    st.text("MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]")
    st.text("ExerciseAngina: exercise-induced angina [Y: Yes, N: No]")
    st.text("Oldpeak: oldpeak = ST [Numeric value measured in depression]")
    st.text("ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]")








