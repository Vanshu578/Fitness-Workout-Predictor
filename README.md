# 🏋️ Fitness & Workout Predictor

An end-to-end machine learning project on fast-food meals. It predicts:

1. **Running burn time (regression):** how many minutes of running are needed to burn a meal.
2. **Workout shock tier (classification):** which of 4 tiers the meal falls into.

Both models are served through an interactive **Streamlit** web app.


## Dataset

`fast_food_cheat_meal_workout_burn.csv` — 8,000 rows, no missing values, no duplicates.
_Add the dataset source link here._

| Type | Columns |
|---|---|
| Meal nutrition | `item_count`, `total_calories`, `fat_grams`, `saturated_fat_grams`, `carb_grams`, `sugar_grams`, `protein_grams`, `sodium_mg` |
| Consumer | `consumer_age`, `consumer_weight_kg`, `daily_calorie_allowance_pct`, `consumer_gender` |
| Meal info | `fast_food_chain`, `meal_category` |
| **Regression target** | `running_burn_time_min` |
| **Classification target** | `workout_shock_tier` — Moderate Burn, High Sweat Penalty, Severe Cardio Deficit, Extreme / Half-Marathon Toll |

### Features used by the models

- **11 numeric features:** the nutrition, consumer-age, weight and allowance columns listed above.
- **Categorical features (one-hot encoded):** fast food chain, meal category, consumer gender.

### Columns deliberately excluded (data leakage)

`cycling_burn_time_min`, `walking_burn_time_min`, `hiit_burn_time_min`, `thermic_effect_calories` and `net_caloric_surplus` are derived from the same values as the targets, so they are removed from the features. `order_id` is dropped as an identifier.

> **Leakage fix:** an earlier version of the regression model also used `workout_shock_tier` as an input feature, which inflated its scores (R² ≈ 0.99). It is now removed from the regression features, so the reported regression results are realistic.

---

## Workflow

1. **Data understanding:** null and duplicate checks, mean / median / standard deviation / quartiles / range, correlation heatmap and distribution plots.
2. **Preprocessing:** one-hot encoding (chain, meal category, gender), ordinal encoding for fitness level, label encoding for the tier target, `StandardScaler` for classification (fit on the training split only).
3. **Regression models:** Linear Regression, Decision Tree Regressor, Random Forest Regressor.
4. **Classification models:** Logistic Regression, Decision Tree Classifier (tuned with `GridSearchCV`), Random Forest Classifier.
5. **Evaluation:** R², MAE and MSE for regression; accuracy, precision, recall, F1, confusion matrix and 5-fold cross-validation for classification.
6. **Deployment:** the trained models, scaler, encoders and column lists are saved with `joblib` and loaded by the Streamlit app.

---

## Results

_Fill these tables from the output printed by `python project3.py`._

### Regression — target: `running_burn_time_min`

| Model | R² | MAE (min) | MSE |
|---|---|---|---|
| Linear Regression |0.9403 |9.564 |176.004 |
| Decision Tree (max_depth=5) | 0.9365|10.222 |187.237 |
| Random Forest |0.9744 | 10.222| 187.237|

### Classification — target: `workout_shock_tier`

| Model | Test accuracy | F1 (weighted) | 5-fold CV accuracy |
|---|---|---|---|
| Logistic Regression | 91.12|91.1 | |
| Decision Tree (entropy, max_depth=6) | 88.94|89.55 | |
| Random Forest | 89.62| |89.55 |

---

## Streamlit app

The app has two modes, chosen from the sidebar:

- **Regression (Burn Time):** shows the predicted running time from all three regression models.
- **Classification (Shock Tier):** shows the predicted tier from all three classifiers, with a confidence percentage.

**Confidence** is the probability the model assigns to the tier it chose. It is not the model's overall accuracy.

Inputs are limited to the minimum and maximum values found in the dataset, and default to the dataset median. The app also warns if fat and protein calories exceed the total calories entered.

---

## Project structure

```
├── project3.py                      # EDA, preprocessing, training, saving models
├── app.py                           # Streamlit app
├── fast_food_cheat_meal_workout_burn.csv
├── requirements.txt
├── README.md
│
├── linear_regression.pkl            # regression models
├── decision_tree_regression.pkl
├── random_forest_regression.pkl
├── logistic_regression.pkl          # classification models
├── decision_tree_classification.pkl
├── random_forest_classification.pkl
│
├── standard_scaler.pkl              # scaler used by the classifiers
├── onehot_encoder.pkl               # encoder for chain / meal category / gender
├── label_encoder.pkl                # decodes tier numbers back to names
├── reg_columns.pkl                  # exact feature columns for regression
└── clf_columns.pkl                  # exact feature columns for classification
```

---

## How to run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train the models and create the .pkl files
python project3.py

# 3. Launch the web app
streamlit run app.py
```

---

## Limitations

- The dataset looks **synthetic**, so these scores should not be read as real-world performance.
- Models are compared on a single train/test split. Differences of 1–2% between models are within noise, so the cross-validation scores are a better guide.
- Inputs far outside the training data (for example an unusual chain and meal combination) can give unreliable predictions, especially from Linear Regression.
- `fitness_level` is encoded in the script but not used as a feature.

---

## Tech stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Joblib · Streamlit
