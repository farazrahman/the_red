# the_red
ML based web app for predicting heart diseases

## About the Project:
This project is about developing a live demo of a software application that uses Machine Learning to build a prediction system that will help healthcare professionals detect heart disease early for their patients.

## Stakeholders:
- Healthcare professionals- who can get prediction using the application and back up their decision. They can accept or reject the prediction provided by the app if it doesn't align with their domain knowledge. This is where human-in-the-loop behind the AI systems comes into play. 
- Patients- Can monitor their heart health condition using this application. (This feature is currently in the acklog)

## About the Training Data:
The training data is taken from Kaggle from the link below:
Fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved from
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

## Programming Language and Libraries used:
  1. Python- The code should run using Python versions 3.8
  2. sqlite3 for SQL database Manangement- Python comes with a built-in sqlite database in the form of a library to provide a complete database management system without the need for downloading an additional software. Works best for practising.
  3. pandas for doing transformation tasks on the csv files before loading to db.
  4. os- python module for interacting with operating system
  5. Streamlit- An open source app framework to deploy the ML model in order to showcase the results for testing

## Project Structure:
The project has following three elements:

- ETL Pipeline:
create_db.py - creates a sqlite db for storing the training data and from inputs from the ML prediction results and new patients.
transform_load.py- Pre-processes the data and loads it into the DB for use by ML models.

- ML Pipeline:
heart-failure-prediction-eda-modeling.ipynb - This is the notebook where ED and model building process took place. Once the model was selected, it was saved using joblib in the repository for model serving purposes. 

- Deployment Pipeline:
deploy.py- This is where the pickled model is loaded and integrated with streamlit platform in order to prepare the demo for prediction

## File Structure and Description:
The_RED:

  1. README.md: read me file containing instructions to run the code 
  2. requirements.txt- needed for specifying the libraries that needs to be installed for successfully running the code
  3. create_db.py- for creating a database
  4. heart-failure-prediction-eda-modeling.ipynb
  5. deploy.py


## Instructions for execution
To execute the project follow the steps below: NOTE: Pycharm is used as IDE

  1. Clone the repository
  2. Set up a virtual environment in the project's root directory
  3. Open a terminal in the project directory and run:
  4. python3 -m virtualenv venv
  5. source venv/bin/activate
  6. pip3 install -r requirements.txt
  7. To create a db and the required tables run create_db.py in the project's root directory
  8. To populate the db with data run load-data.py in the directory /data_ingestion_ETL/load.py

## To get heart disease prediction using the streamlit application
Go to: link

## To provide input features for the ML application, you have to specify the values of following features:

  1. "Age: age of the patient [years]"
  2. "Sex: gender of the patient [M: Male, F: Female]"
  3. "ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]"
  4. "RestingBP: resting blood pressure [mm Hg]"
  5. "Cholesterol: serum cholesterol [mm/dl]"
  6. "FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]"
  7. "RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions "
                  "and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular "
                  "hypertrophy by Estes' criteria]"
  8. "MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]"
  9. "ExerciseAngina: exercise-induced angina [Y: Yes, N: No]"
  10. "Oldpeak: oldpeak = ST [Numeric value measured in depression]"
  11. "ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]"


## Once you are done with inputing the values, please click on Predict button on the application to get the detailed report.
