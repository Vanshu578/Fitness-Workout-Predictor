import os

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Fitness & Workout Predictor", page_icon="🏋️")

DATA_FILE = "fast_food_cheat_meal_workout_burn.csv"
CAT_COLS = ["fast_food_chain", "meal_category", "consumer_gender"]
CAT_PREFIXES = tuple(c + "_" for c in CAT_COLS)


@st.cache_resource
def load_artifacts():
    """Load every saved file once (cached across reruns)."""
    return {
        "oh": joblib.load("onehot_encoder.pkl"),
        "ll": joblib.load("label_encoder.pkl"),
        "scaler": joblib.load("standard_scaler.pkl"),
        "reg_cols": joblib.load("reg_columns.pkl"),
        "clf_cols": joblib.load("clf_columns.pkl"),
        "reg": {
            "Random Forest": joblib.load("random_forest_regression.pkl"),
            "Linear Regression": joblib.load("linear_regression.pkl"),
            "Decision Tree": joblib.load("decision_tree_regression.pkl"),
        },
        "clf": {
            "Logistic Regression": joblib.load("logistic_regression.pkl"),
            "Decision Tree": joblib.load("decision_tree_classification.pkl"),
            "Random Forest": joblib.load("random_forest_classification.pkl"),
        },
    }


@st.cache_data
def load_ranges():
    """Median / min / max of each column from the dataset (used for defaults and limits)."""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        return (
            df.median(numeric_only=True).to_dict(),
            df.min(numeric_only=True).to_dict(),
            df.max(numeric_only=True).to_dict(),
        )
    return {}, {}, {}


def build_row(columns, numeric_values, chain, meal, gender, oh):
    """Build one input row with the exact columns/order used in training."""
    row = pd.DataFrame(0.0, index=[0], columns=columns)
    for name, value in numeric_values.items():
        if name in row.columns:
            row.loc[0, name] = value

    cat_df = pd.DataFrame([[chain, meal, gender]], columns=CAT_COLS)
    encoded = oh.transform(cat_df).toarray()[0]
    names = oh.get_feature_names_out(CAT_COLS)
    for name, value in zip(names, encoded):
        if name in row.columns:
            row.loc[0, name] = value
    return row[columns]


art = load_artifacts()
medians, mins, maxs = load_ranges()
chains, meals, genders = art["oh"].categories_

# Numeric features = every model column that is not a one-hot column
numeric_cols = [c for c in art["reg_cols"] if not c.startswith(CAT_PREFIXES)]

st.title("Fitness & Workout Predictor")
st.write(
    "Enter the meal and consumer details to predict the **running time needed "
    "to burn the meal** (regression) and its **workout shock tier** (classification)."
)

mode = st.sidebar.selectbox(
    "Choose prediction type",
    ["Regression (Burn Time)", "Classification (Shock Tier)"],
)

with st.form("inputs"):
    st.subheader("Meal & consumer details")
    values = {}
    cols = st.columns(3)
    for i, name in enumerate(numeric_cols):
        label = name.replace("_", " ").capitalize()
        lo = float(mins.get(name, 0.0))
        hi = float(maxs[name]) if name in maxs else None
        default = float(medians.get(name, lo))
        values[name] = cols[i % 3].number_input(
            label, min_value=lo, max_value=hi, value=default
        )

    chain = st.selectbox("Fast food chain", chains)
    meal = st.selectbox("Meal category", meals)
    gender = st.selectbox("Consumer gender", genders)
    submitted = st.form_submit_button("Predict")

if submitted:
    if values["fat_grams"] * 9 + values["protein_grams"] * 4 > values["total_calories"] * 1.05:
        st.warning(
            "Fat and protein alone add up to more calories than the total "
            "entered. Please double-check your inputs."
        )

    if mode.startswith("Regression"):
        row = build_row(art["reg_cols"], values, chain, meal, gender, art["oh"])
        st.subheader("Predicted running time to burn this meal")
        for name, m in art["reg"].items():
            st.success(f"**{name}**: {m.predict(row)[0]:.1f} minutes")
    else:
        row = build_row(art["clf_cols"], values, chain, meal, gender, art["oh"])
        row_scaled = art["scaler"].transform(row)
        st.subheader("Predicted workout shock tier")
        for name, m in art["clf"].items():
            pred = m.predict(row_scaled)
            label = art["ll"].inverse_transform(pred)[0]
            confidence = m.predict_proba(row_scaled).max() * 100
            st.success(f"**{name}**: {label} ({confidence:.0f}% confidence)")
