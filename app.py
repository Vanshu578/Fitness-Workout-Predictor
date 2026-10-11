import joblib
import numpy as np
import streamlit as st

# Load the standard scaler
scaler = joblib.load('standard_scaler.pkl')

# Load Regression Models
lin_model = joblib.load('linear_regression.pkl')
rf_reg_model = joblib.load('random_forest_regression.pkl')
dt_reg_model = joblib.load('decession_tree_regression.pkl')

# Load Classification Models
lr_clf_model = joblib.load('logistic_regression.pkl')
dt_clf_model = joblib.load('decession_tree_classification.pkl')
rf_clf_model = joblib.load('random_forest_classification.pkl')

st.title('Fitness & Workout Predictor Portfolio App')
st.write(
    'Interactive web app featuring machine learning models for running burn'
    ' time and workout shock tier classification.'
)

# Sidebar navigation for app mode
app_mode = st.sidebar.selectbox(
    'Choose Prediction Type', ['Regression (Burn Time)', 'Classification (Shock Tier)']
)

if app_mode == 'Regression (Burn Time)':
  st.header('Running Burn Time Predictor')

  # Model selector for regression
  reg_model_choice = st.selectbox(
      'Select Regression Model',
      ['Random Forest', 'Linear Regression', 'Decision Tree'],
  )

  # User input features
  total_calories = st.number_input('Total Calories', value=1500.0)
  fat_grams = st.number_input('Fat Grams', value=75.0)
  protein_grams = st.number_input('Protein Grams', value=50.0)

  if st.button('Predict Burn Time'):
    # Create an array of zeros with 26 features to match training shape
    input_data = np.zeros((1, 26))
    input_data[0, 0] = total_calories
    input_data[0, 1] = fat_grams
    input_data[0, 2] = protein_grams

    # Route input to the chosen regression model
    if reg_model_choice == 'Random Forest':
      prediction = rf_reg_model.predict(input_data)
    elif reg_model_choice == 'Linear Regression':
      prediction = lin_model.predict(input_data)
    else:
      prediction = dt_reg_model.predict(input_data)

    st.success(f'**{reg_model_choice}**: {prediction[0]:.2f} mins')

else:
  st.header('Workout Shock Tier Predictor')

  # Model selector for classification
  clf_model_choice = st.selectbox(
      'Select Classification Model',
      [
          'Logistic Regression',
          'Decision Tree Classifier',
          'Random Forest Classifier',
      ],
  )

  # User input features
  total_calories_clf = st.number_input('Total Calories (Clf)', value=1500.0)
  fat_grams_clf = st.number_input('Fat Grams (Clf)', value=75.0)
  protein_grams_clf = st.number_input('Protein Grams (Clf)', value=50.0)

  if st.button('Predict Shock Tier'):
    # Create an array of zeros with 26 features for classification
    input_data_clf = np.zeros((1, 25))
    input_data_clf[0, 0] = total_calories_clf
    input_data_clf[0, 1] = fat_grams_clf
    input_data_clf[0, 2] = protein_grams_clf

    # Scale input data using the saved scaler
    input_scaled = scaler.transform(input_data_clf)

    # Route input to the chosen classification model
    if clf_model_choice == 'Logistic Regression':
      prediction_clf = lr_clf_model.predict(input_scaled)
    elif clf_model_choice == 'Decision Tree Classifier':
      prediction_clf = dt_clf_model.predict(input_scaled)
    else:
      prediction_clf = rf_clf_model.predict(input_scaled)

    # Map numeric prediction to descriptive labels
    tier_mapping = {
        0: 'Extreme / Half-Marathon Toll',
        1: 'High Sweat Penalty',
        2: 'Moderate Burn',
        3: 'Severe Cardio Deficit',
    }
    predicted_tier = tier_mapping.get(
        prediction_clf[0], str(prediction_clf[0])
    )

    st.success(f'**{clf_model_choice}**: {predicted_tier}')