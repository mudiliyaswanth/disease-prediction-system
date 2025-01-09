import pandas as pd
import numpy as np
from joblib import load
import streamlit as st

if __name__ == '__main__':
    # Set value of 1 corresponding to the symptom
    syms = ['Select','Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering', 'Chills', 'Joint Pain', 'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Muscle Wasting', 'Vomiting', 'Burning Micturition', 'Spotting  urination', 'Fatigue', 'Weight Gain', 'Anxiety', 'Cold Hands And Feets', 'Mood Swings', 'Weight Loss', 'Restlessness', 'Lethargy', 'Patches In Throat', 'Irregular Sugar Level', 'Cough', 'High Fever', 'Sunken Eyes', 'Breathlessness', 'Sweating', 'Dehydration', 'Indigestion', 'Headache', 'Yellowish Skin', 'Dark Urine', 'Nausea', 'Loss Of Appetite', 'Pain Behind The Eyes', 'Back Pain', 'Constipation', 'Abdominal Pain', 'Diarrhoea', 'Mild Fever', 'Yellow Urine', 'Yellowing Of Eyes', 'Acute Liver Failure', 'Fluid Overload', 'Swelling Of Stomach', 'Swelled Lymph Nodes', 'Malaise', 'Blurred And Distorted Vision', 'Phlegm', 'Throat Irritation', 'Redness Of Eyes', 'Sinus Pressure', 'Runny Nose', 'Congestion', 'Chest Pain', 'Weakness In Limbs', 'Fast Heart Rate', 'Pain During Bowel Movements', 'Pain In Anal Region', 'Bloody Stool', 'Irritation In Anus', 'Neck Pain', 'Dizziness', 'Cramps', 'Bruising', 'Obesity', 'Swollen Legs', 'Swollen Blood Vessels', 'Puffy Face And Eyes', 'Enlarged Thyroid', 'Brittle Nails', 'Swollen Extremeties', 'Excessive Hunger', 'Extra Marital Contacts', 'Drying And Tingling Lips', 'Slurred Speech', 'Knee Pain', 'Hip Joint Pain', 'Muscle Weakness', 'Stiff Neck', 'Swelling Joints', 'Movement Stiffness', 'Spinning Movements', 'Loss Of Balance', 'Unsteadiness', 'Weakness Of One Body Side', 'Loss Of Smell', 'Bladder Discomfort', 'Foul Smell Of urine', 'Continuous Feel Of Urine', 'Passage Of Gases', 'Internal Itching', 'Toxic Look (typhos)', 'Depression', 'Irritability', 'Muscle Pain', 'Altered Sensorium', 'Red Spots Over Body', 'Belly Pain', 'Abnormal Menstruation', 'Dischromic  Patches', 'Watering From Eyes', 'Increased Appetite', 'Polyuria', 'Family History', 'Mucoid Sputum', 'Rusty Sputum', 'Lack Of Concentration', 'Visual Disturbances', 'Receiving Blood Transfusion', 'Receiving Unsterile Injections', 'Coma', 'Stomach Bleeding', 'Distention Of Abdomen', 'History Of Alcohol Consumption', 'Fluid Overload.1', 'Blood In Sputum', 'Prominent Veins On Calf', 'Palpitations', 'Painful Walking', 'Pus Filled Pimples', 'Blackheads', 'Scurring', 'Skin Peeling', 'Silver Like Dusting', 'Small Dents In Nails', 'Inflammatory Nails', 'Blister', 'Red Sore Around Nose', 'Yellow Crust Ooze']
    general_symptoms = ['Select',
    'Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering', 
    'Chills', 'Joint Pain', 'Stomach Pain', 'Muscle Wasting', 'Fatigue', 'Weight Gain', 
    'Anxiety', 'Cold Hands And Feets', 'Mood Swings', 'Weight Loss', 'Restlessness', 
    'Lethargy', 'Headache', 'Sweating', 'Dehydration', 'Indigestion', 'Nausea', 
    'Loss Of Appetite', 'Back Pain', 'Abdominal Pain', 'Mild Fever', 'Weakness In Limbs', 
    'Dizziness', 'Cramps', 'Bruising', 'Obesity', 'Puffy Face And Eyes', 'Excessive Hunger', 
    'Muscle Weakness', 'Stiff Neck', 'Movement Stiffness', 'Spinning Movements', 
    'Loss Of Balance', 'Unsteadiness', 'Weakness Of One Body Side', 'Internal Itching', 
    'Depression', 'Irritability', 'Muscle Pain', 'Altered Sensorium', 'Red Spots Over Body', 
    'Belly Pain', 'Increased Appetite', 'Polyuria', 'Lack Of Concentration', 
    'Visual Disturbances', 'Coma', 'Painful Walking', 'Blackheads', 'Scarring', 
    'Skin Peeling', 'Silver Like Dusting'
]
    gastrointestinal_symptoms = ['Select',
    'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Vomiting', 'Spotting urination', 
    'Burning Micturition', 'Diarrhoea', 'Constipation', 'Abdominal Pain', 'Loss Of Appetite', 
    'Stomach Bleeding', 'Distention Of Abdomen', 'Passage Of Gases', 'Belly Pain'
]

    respiratory_symptoms = ['Select',
      'Cough', 'Breathlessness', 'Sinus Pressure', 'Runny Nose', 'Congestion', 
      'Chest Pain', 'Phlegm', 'Throat Irritation', 'Redness Of Eyes', 'Weakness In Limbs', 
      'Fast Heart Rate', 'Patches In Throat', 'High Fever', 'Sunken Eyes', 'Malaise', 
      'Blurred And Distorted Vision', 'Red Spots Over Body', 'Mucoid Sputum', 'Rusty Sputum', 
      'Blood In Sputum'
   ]
    dermatological_symptoms = ['Select',
      'Skin Rash', 'Itching', 'Nodal Skin Eruptions', 'Blister', 'Red Sore Around Nose', 
      'Yellow Crust Ooze', 'Pus Filled Pimples', 'Blackheads', 'Scarring', 'Skin Peeling', 
      'Silver Like Dusting', 'Small Dents In Nails', 'Inflammatory Nails', 'Brittle Nails', 
      'Dischromic Patches'
   ]
    systemic_symptoms = ['Select',
      'Irregular Sugar Level', 'Yellowish Skin', 'Dark Urine', 'Yellow Urine', 
      'Yellowing Of Eyes', 'Acute Liver Failure', 'Fluid Overload', 'Swelling Of Stomach', 
      'Swelled Lymph Nodes', 'Enlarged Thyroid', 'Swollen Legs', 'Swollen Blood Vessels', 
      'Swollen Extremities', 'Bladder Discomfort', 'Foul Smell Of urine', 
      'Continuous Feel Of Urine', 'Toxic Look (typhos)', 'Abnormal Menstruation', 
      'Receiving Blood Transfusion', 'Receiving Unsterile Injections', 'Family History', 
      'History Of Alcohol Consumption', 'Prominent Veins On Calf', 'Palpitations'
   ]
    to_test = []
    st.header("Disease Prediction",divider="gray")
    with st.form("my_form"):
      symp1 = st.selectbox('Describe Your General Symptoms', general_symptoms)
      symp2 = st.selectbox('Describe Your GastroIntestinal Symptoms', gastrointestinal_symptoms)
      symp3 = st.selectbox('Describe Your Respiratory Symptoms', respiratory_symptoms)
      symp4 = st.selectbox('Describe Your Dermatological Symptoms', dermatological_symptoms)
      symp5 = st.selectbox('Describe Your Systemic Symptoms', systemic_symptoms)
      othersymp = st.selectbox('Describe Your any Other Symptoms', syms)
      st.form_submit_button('Submit my picks')
      to_test.extend([symp1,symp2,symp3,symp4,symp5,othersymp])



    mapped_syms = {'Itching': 'itching',
 'Skin Rash': 'skin_rash',
 'Nodal Skin Eruptions': 'nodal_skin_eruptions',
 'Continuous Sneezing': 'continuous_sneezing',
 'Shivering': 'shivering',
 'Chills': 'chills',
 'Joint Pain': 'joint_pain',
 'Stomach Pain': 'stomach_pain',
 'Acidity': 'acidity',
 'Ulcers On Tongue': 'ulcers_on_tongue',
 'Muscle Wasting': 'muscle_wasting',
 'Vomiting': 'vomiting',
 'Burning Micturition': 'burning_micturition',
 'Spotting  urination': 'spotting_ urination',
 'Fatigue': 'fatigue',
 'Weight Gain': 'weight_gain',
 'Anxiety': 'anxiety',
 'Cold Hands And Feets': 'cold_hands_and_feets',
 'Mood Swings': 'mood_swings',
 'Weight Loss': 'weight_loss',
 'Restlessness': 'restlessness',
 'Lethargy': 'lethargy',
 'Patches In Throat': 'patches_in_throat',
 'Irregular Sugar Level': 'irregular_sugar_level',
 'Cough': 'cough',
 'High Fever': 'high_fever',
 'Sunken Eyes': 'sunken_eyes',
 'Breathlessness': 'breathlessness',
 'Sweating': 'sweating',
 'Dehydration': 'dehydration',
 'Indigestion': 'indigestion',
 'Headache': 'headache',
 'Yellowish Skin': 'yellowish_skin',
 'Dark Urine': 'dark_urine',
 'Nausea': 'nausea',
 'Loss Of Appetite': 'loss_of_appetite',
 'Pain Behind The Eyes': 'pain_behind_the_eyes',
 'Back Pain': 'back_pain',
 'Constipation': 'constipation',
 'Abdominal Pain': 'abdominal_pain',
 'Diarrhoea': 'diarrhoea',
 'Mild Fever': 'mild_fever',
 'Yellow Urine': 'yellow_urine',
 'Yellowing Of Eyes': 'yellowing_of_eyes',
 'Acute Liver Failure': 'acute_liver_failure',
 'Fluid Overload': 'fluid_overload',
 'Swelling Of Stomach': 'swelling_of_stomach',
 'Swelled Lymph Nodes': 'swelled_lymph_nodes',
 'Malaise': 'malaise',
 'Blurred And Distorted Vision': 'blurred_and_distorted_vision',
 'Phlegm': 'phlegm',
 'Throat Irritation': 'throat_irritation',
 'Redness Of Eyes': 'redness_of_eyes',
 'Sinus Pressure': 'sinus_pressure',
 'Runny Nose': 'runny_nose',
 'Congestion': 'congestion',
 'Chest Pain': 'chest_pain',
 'Weakness In Limbs': 'weakness_in_limbs',
 'Fast Heart Rate': 'fast_heart_rate',
 'Pain During Bowel Movements': 'pain_during_bowel_movements',
 'Pain In Anal Region': 'pain_in_anal_region',
 'Bloody Stool': 'bloody_stool',
 'Irritation In Anus': 'irritation_in_anus',
 'Neck Pain': 'neck_pain',
 'Dizziness': 'dizziness',
 'Cramps': 'cramps',
 'Bruising': 'bruising',
 'Obesity': 'obesity',
 'Swollen Legs': 'swollen_legs',
 'Swollen Blood Vessels': 'swollen_blood_vessels',
 'Puffy Face And Eyes': 'puffy_face_and_eyes',
 'Enlarged Thyroid': 'enlarged_thyroid',
 'Brittle Nails': 'brittle_nails',
 'Swollen Extremeties': 'swollen_extremeties',
 'Excessive Hunger': 'excessive_hunger',
 'Extra Marital Contacts': 'extra_marital_contacts',
 'Drying And Tingling Lips': 'drying_and_tingling_lips',
 'Slurred Speech': 'slurred_speech',
 'Knee Pain': 'knee_pain',
 'Hip Joint Pain': 'hip_joint_pain',
 'Muscle Weakness': 'muscle_weakness',
 'Stiff Neck': 'stiff_neck',
 'Swelling Joints': 'swelling_joints',
 'Movement Stiffness': 'movement_stiffness',
 'Spinning Movements': 'spinning_movements',
 'Loss Of Balance': 'loss_of_balance',
 'Unsteadiness': 'unsteadiness',
 'Weakness Of One Body Side': 'weakness_of_one_body_side',
 'Loss Of Smell': 'loss_of_smell',
 'Bladder Discomfort': 'bladder_discomfort',
 'Foul Smell Of urine': 'foul_smell_of urine',
 'Continuous Feel Of Urine': 'continuous_feel_of_urine',
 'Passage Of Gases': 'passage_of_gases',
 'Internal Itching': 'internal_itching',
 'Toxic Look (typhos)': 'toxic_look_(typhos)',
 'Depression': 'depression',
 'Irritability': 'irritability',
 'Muscle Pain': 'muscle_pain',
 'Altered Sensorium': 'altered_sensorium',
 'Red Spots Over Body': 'red_spots_over_body',
 'Belly Pain': 'belly_pain',
 'Abnormal Menstruation': 'abnormal_menstruation',
 'Dischromic  Patches': 'dischromic _patches',
 'Watering From Eyes': 'watering_from_eyes',
 'Increased Appetite': 'increased_appetite',
 'Polyuria': 'polyuria',
 'Family History': 'family_history',
 'Mucoid Sputum': 'mucoid_sputum',
 'Rusty Sputum': 'rusty_sputum',
 'Lack Of Concentration': 'lack_of_concentration',
 'Visual Disturbances': 'visual_disturbances',
 'Receiving Blood Transfusion': 'receiving_blood_transfusion',
 'Receiving Unsterile Injections': 'receiving_unsterile_injections',
 'Coma': 'coma',
 'Stomach Bleeding': 'stomach_bleeding',
 'Distention Of Abdomen': 'distention_of_abdomen',
 'History Of Alcohol Consumption': 'history_of_alcohol_consumption',
 'Fluid Overload.1': 'fluid_overload.1',
 'Blood In Sputum': 'blood_in_sputum',
 'Prominent Veins On Calf': 'prominent_veins_on_calf',
 'Palpitations': 'palpitations',
 'Painful Walking': 'painful_walking',
 'Pus Filled Pimples': 'pus_filled_pimples',
 'Blackheads': 'blackheads',
 'Scurring': 'scurring',
 'Skin Peeling': 'skin_peeling',
 'Silver Like Dusting': 'silver_like_dusting',
 'Small Dents In Nails': 'small_dents_in_nails',
 'Inflammatory Nails': 'inflammatory_nails',
 'Blister': 'blister',
 'Red Sore Around Nose': 'red_sore_around_nose',
 'Yellow Crust Ooze': 'yellow_crust_ooze'}
    
    symptoms = {'itching': 0, 'skin_rash': 0, 'nodal_skin_eruptions': 0, 'continuous_sneezing': 0,
                'shivering': 0, 'chills': 0, 'joint_pain': 0, 'stomach_pain': 0, 'acidity': 0, 'ulcers_on_tongue': 0,
                'muscle_wasting': 0, 'vomiting': 0, 'burning_micturition': 0, 'spotting_ urination': 0, 'fatigue': 0,
                'weight_gain': 0, 'anxiety': 0, 'cold_hands_and_feets': 0, 'mood_swings': 0, 'weight_loss': 0,
                'restlessness': 0, 'lethargy': 0, 'patches_in_throat': 0, 'irregular_sugar_level': 0, 'cough': 0,
                'high_fever': 0, 'sunken_eyes': 0, 'breathlessness': 0, 'sweating': 0, 'dehydration': 0,
                'indigestion': 0, 'headache': 0, 'yellowish_skin': 0, 'dark_urine': 0, 'nausea': 0, 'loss_of_appetite': 0,
                'pain_behind_the_eyes': 0, 'back_pain': 0, 'constipation': 0, 'abdominal_pain': 0, 'diarrhoea': 0, 'mild_fever': 0,
                'yellow_urine': 0, 'yellowing_of_eyes': 0, 'acute_liver_failure': 0, 'fluid_overload': 0, 'swelling_of_stomach': 0,
                'swelled_lymph_nodes': 0, 'malaise': 0, 'blurred_and_distorted_vision': 0, 'phlegm': 0, 'throat_irritation': 0,
                'redness_of_eyes': 0, 'sinus_pressure': 0, 'runny_nose': 0, 'congestion': 0, 'chest_pain': 0, 'weakness_in_limbs': 0,
                'fast_heart_rate': 0, 'pain_during_bowel_movements': 0, 'pain_in_anal_region': 0, 'bloody_stool': 0,
                'irritation_in_anus': 0, 'neck_pain': 0, 'dizziness': 0, 'cramps': 0, 'bruising': 0, 'obesity': 0, 'swollen_legs': 0,
                'swollen_blood_vessels': 0, 'puffy_face_and_eyes': 0, 'enlarged_thyroid': 0, 'brittle_nails': 0, 'swollen_extremeties': 0,
                'excessive_hunger': 0, 'extra_marital_contacts': 0, 'drying_and_tingling_lips': 0, 'slurred_speech': 0,
                'knee_pain': 0, 'hip_joint_pain': 0, 'muscle_weakness': 0, 'stiff_neck': 0, 'swelling_joints': 0, 'movement_stiffness': 0,
                'spinning_movements': 0, 'loss_of_balance': 0, 'unsteadiness': 0, 'weakness_of_one_body_side': 0, 'loss_of_smell': 0,
                'bladder_discomfort': 0, 'foul_smell_of urine': 0, 'continuous_feel_of_urine': 0, 'passage_of_gases': 0, 'internal_itching': 0,
                'toxic_look_(typhos)': 0, 'depression': 0, 'irritability': 0, 'muscle_pain': 1, 'altered_sensorium': 0,
                'red_spots_over_body': 0, 'belly_pain': 0, 'abnormal_menstruation': 0, 'dischromic _patches': 0, 'watering_from_eyes': 0,
                'increased_appetite': 0, 'polyuria': 0, 'family_history': 0, 'mucoid_sputum': 0, 'rusty_sputum': 0, 'lack_of_concentration': 0,
                'visual_disturbances': 0, 'receiving_blood_transfusion': 0, 'receiving_unsterile_injections': 0, 'coma': 0,
                'stomach_bleeding': 0, 'distention_of_abdomen': 0, 'history_of_alcohol_consumption': 0, 'fluid_overload.1': 0,
                'blood_in_sputum': 0, 'prominent_veins_on_calf': 0, 'palpitations': 0, 'painful_walking': 0, 'pus_filled_pimples': 0,
                'blackheads': 0, 'scurring': 0, 'skin_peeling': 0, 'silver_like_dusting': 0, 'small_dents_in_nails': 0, 'inflammatory_nails': 0,
                'blister': 0, 'red_sore_around_nose': 0, 'yellow_crust_ooze': 0}
    for i in symptoms:
        symptoms[i] = 0
    for j in to_test:
       if j == 'Select':
          continue
       symptoms[mapped_syms[j]] = 1

    # Prepare Test Data
    df_test = pd.DataFrame(columns=list(symptoms.keys()))
    df_test.loc[0] = np.array(list(symptoms.values()))

    # Load pre-trained model
    clf = load(str("./saved_model/random_forest.joblib"))
    result = clf.predict(df_test)
    st.write(result[0])
    st.header(f"May be You are Suffering from {result[0]}")
 
   
