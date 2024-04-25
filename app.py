import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Define the function for making predictions
def diabetes_prediction(input_data):
    # Reshape the input data to match the shape expected by the model
    input_data = np.array(input_data).reshape(1, -1)
    
    # Use the loaded model to make predictions
    prediction = loaded_model.predict(input_data)
    
    # Return the prediction result
    if prediction[0] == 1:
        return "The patient is likely to have diabetes."
    else:
        return "The patient is unlikely to have diabetes."

# creating a function for Prediction
def main():
    st.title('Diabetes Prediction Web App')

    # getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            # Convert input to numeric values
            input_data = [
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]
            
            diagnosis = diabetes_prediction(input_data)
        except ValueError:
            diagnosis = "Error: Please enter valid numeric values."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
