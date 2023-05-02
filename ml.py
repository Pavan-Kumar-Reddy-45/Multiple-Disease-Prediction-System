import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Bhargav/OneDrive/Desktop/ml/savedmodels/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Bhargav/OneDrive/Desktop/ml/savedmodels/heart_disease_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                           
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetese Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    with st.form(key='Diabetes_prediction_form'):
        # get user input
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=45)
            SkinThickness = st.number_input('SkinThickness', min_value=0, max_value=65)

        with col2:
            Glucose = st.number_input('Glucose level', min_value=0, max_value=350)
            Insulin = st.number_input('Insulin', min_value=0, max_value=1917)
         

        with col3:
            Bloodpressure = st.number_input('Bloodpressure', min_value=0, max_value=180)
            BMI = st.number_input('BMI', min_value=0.00, max_value=70.00)

        col4, col5, col6 = st.columns(3)
        with col4:
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.000, max_value=3.000) 
        with col5:
            age = st.number_input('Age', min_value=0, max_value=120)
            


        # make prediction
        if st.form_submit_button('Predict Diabetes'):
            
            # create input array
            input_data = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, age]
            # make prediction using model
            prediction = diabetes_model.predict([input_data])[0]
            # show result
            if prediction == 1:
                st.success('The person is likely to have Diabetes.')
            else:
                st.success('The person is unlikely to have Diabetes.')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    with st.form(key='heart_disease_prediction_form'):
        # get user input
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=0, max_value=120)
            trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300)

        with col2:
            sex = st.selectbox('Sex', options=['Male', 'Female'])
            chol = st.number_input('Serum Cholestoral in mg/dl', value=0, step=1)
         

        with col3:
            cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])

            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])

        col4, col5, col6 = st.columns(3)
        with col4:
            restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
            oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.00, max_value=8.00)
            

        with col5:
            thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250)
            slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2])
           

        with col6:
            exang = st.selectbox('Exercise Induced Angina', options=[0, 1])
            ca = st.number_input('Major Vessels Colored by Flourosopy', min_value=0, max_value=3  )

            thal = st.selectbox('Thal', options=[0, 1, 2, 3])

        # make prediction
        if st.form_submit_button('Predict Heart Disease'):
            # convert sex to integer
            if sex == 'Male':
                sex = 1
            else:
                sex = 0
            # create input array
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            # make prediction using model
            prediction = heart_disease_model.predict([input_data])[0]
            # show result
            if prediction == 1:
                st.success('The person is likely to have heart disease.')
            else:
                st.success('The person is unlikely to have heart disease.')
