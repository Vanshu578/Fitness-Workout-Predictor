"""
README - Fast Food, Calories & Workout Analysis

Project Overview
----------------
This project analyzes a fast-food and workout dataset using Python.
The main goal is to understand nutritional information, workout burn
requirements, and build machine-learning models for both regression
and classification tasks.

The project is divided into two main machine-learning parts:

1. Regression
   Predicts the running workout time required using Linear Regression,
   Decision Tree Regression, and Random Forest Regression.

2. Classification
   Predicts the workout shock tier using Logistic Regression,
   Decision Tree Classification, and Random Forest Classification.


Dataset
-------
The project uses the following dataset:

    fast_food_cheat_meal_workout_burn.csv

Important columns used in the analysis include:
- total_calories
- fat_grams
- protein_grams
- running_burn_time_min
- cycling_burn_time_min
- walking_burn_time_min
- hiit_burn_time_min
- thermic_effect_calories
- net_caloric_surplus
- fast_food_chain
- meal_category
- consumer_gender
- fitness_level
- workout_shock_tier


Technologies and Libraries
--------------------------
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn


Project Workflow
----------------
Phase 1 - Data Understanding
- Load the CSV dataset.
- Check the first few records.
- Check for missing values.
- Check for duplicate records.
- Calculate mean, median and standard deviation.
- Calculate quartiles and ranges.
- Explore the data using visualizations.

Phase 2 - Data Preprocessing
- Perform one-hot encoding for categorical columns.
- Perform ordinal encoding for fitness level.
- Perform label encoding for workout shock tier.
- Remove the unnecessary order_id column.
- Prepare the data for machine-learning models.


Regression
----------
Target:
    running_burn_time_min

Models used:
- Linear Regression
- Random Forest Regression
- Decision Tree Regression

The dataset is divided into 80% training data and 20% testing data.

Reported test scores:
- Linear Regression: 94.15%
- Random Forest Regression: 97.78%
- Decision Tree Regression: 93.98%

Based on the reported test score, Random Forest Regression performed
best among the three regression models.


Classification
--------------
Target:
    workout_shock_tier

Models used:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The classification data is standardized using StandardScaler.

Reported test accuracies:
- Logistic Regression: 91.125%
- Decision Tree Classifier: 88.94%
- Random Forest Classifier: 90.125%

Additional evaluation metrics are calculated for the classification
models, including:
- Precision
- Recall
- F1-score
- Confusion Matrix
- Cross-validation


Visualization
-------------
The project includes visualizations for:
- Fitness-level distribution
- Correlation analysis
- Confusion matrices
- Random Forest feature importance
- Classification model accuracy comparison
- Regression model accuracy comparison
- Decision tree visualization


Regression Evaluation
---------------------
The regression models are evaluated using:
- Model score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² score

Reported results show that Random Forest Regression gives the strongest
overall performance among the tested regression models.


Classification Evaluation
--------------------------
Classification models are evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- 5-fold cross-validation

Logistic Regression achieved the highest reported test accuracy among
the classification models in this project.


How to Run
----------
1. Install Python 3.x.
2. Install the required libraries:

       pip install pandas numpy matplotlib seaborn scikit-learn

3. Keep the CSV dataset available on your computer.
4. Update the CSV file path in the Python program if necessary.
5. Run the project Python file.


Important Note
--------------
The original project code uses a local Windows file path for the CSV
dataset. If the project is moved to another computer, this path should
be changed to the location of the CSV file on that computer.


Project Outcome
---------------
The project demonstrates a complete basic machine-learning workflow:

    Data Loading
        |
        v
    Data Cleaning
        |
        v
    Statistical Analysis
        |
        v
    Data Visualization
        |
        v
    Data Encoding & Preprocessing
        |
        +----------------------+
        |                      |
        v                      v
    Regression            Classification
        |                      |
        v                      v
    Model Training        Model Training
        |                      |
        v                      v
    Model Evaluation      Model Evaluation
        |                      |
        +----------+-----------+
                   |
                   v
             Compare Results

The project can be used as a practical example of applying Python,
data analysis, preprocessing, regression, classification, and
machine-learning evaluation to a food and workout-related dataset.
"""

# This file is intentionally written as a simple README-style Python
# file so that the project documentation can stay together with the code.

if __name__ == "__main__":
    print("Fast Food, Calories & Workout Analysis")
    print("---------------------------------------")
    print("This project performs data analysis, visualization, regression,")
    print("and classification using Python and scikit-learn.")
    print()
    print("See the comments/documentation at the top of this file for")
    print("the complete project README.")
