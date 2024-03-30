import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the scaler outside the function
scaler = StandardScaler()


def load_model(model_path):
    """
    Load a machine learning model from a pickle file.

    Parameters:
        model_path (str): The path to the pickle file containing the model.

    Returns:
        object: The loaded machine learning model.
    """
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model


def load_dataset(dataset_path):
    try:
        dataset = pd.read_excel(dataset_path)
        return dataset
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")
        # Handle the error here (e.g., skip line, log error, etc.)
        return None


def show_prediction_page():
    global scaler  # Add global declaration to access the global variable

    # Example usage:
    model = load_model("model/lr_mini.pkl")
    dataset = load_dataset("dataset/original/salary_dataset.xlsx")

    st.title("Salary Prediction")

    st.image(
        "https://github.com/alicenkbaytop/salary-prediction-2024/blob/main/chart/image/prediction_page.png?raw=true"
    )

    st.write("""### Some information is needed to predict your salary!""")

    # Fit the scaler if it's not already fitted
    if not hasattr(scaler, "mean_"):
        df_dummy = pd.DataFrame(
            {
                "level_code": [0],
                "selected_number_of_technology": [1],
                "experience_code": [0],
                "gender_code": [0],
                "company_size_code": [0],
                "currency_code": [0],
                "selected_raise_period": [0],
            }
        )
        scaler.fit(df_dummy)

    # Collect user input for each instance
    profile = st.slider("Number of profile", min_value=1, max_value=5, value=1)
    input_data = []

    for i in range(profile):
        # LEVEL
        selected_level = st.radio(
            f"Select a level for profile {i+1}", dataset.level.unique()
        )
        if selected_level == "Junior":
            level_code = 0
            available_experience_options = [
                "1 - 3 Yıl",
                "0 - 1 Yıl",
            ]  # Swap the options
        elif selected_level == "Middle":
            level_code = 1
            available_experience_options = ["3 - 5 Yıl", "5 - 7 Yıl"]
        elif selected_level == "Senior":
            level_code = 2
            available_experience_options = [
                "7 - 10 Yıl",
                "10 - 12 Yıl",
                "12 - 14 Yıl",
                "15 Yıl ve üzeri",
            ]

        # TECH_STACK
        selected_number_of_technology = st.selectbox(
            f"Select a number of known technology for profile {i+1}", range(1, 20)
        )
        selected_number_of_technology = selected_number_of_technology * 0.5

        # EXPERIENCE
        selected_experience = st.selectbox(
            f"Select an experience for profile {i+1}", available_experience_options
        )
        # Map selected_experience to its corresponding code
        experience_map = {
            "0 - 1 Yıl": 7,
            "1 - 3 Yıl": 6,
            "3 - 5 Yıl": 5,
            "5 - 7 Yıl": 4,
            "7 - 10 Yıl": 3,
            "10 - 12 Yıl": 2,
            "12 - 14 Yıl": 1,
            "15 Yıl ve üzeri": 0,
        }
        experience_code = experience_map[selected_experience]

        # GENDER
        selected_gender = st.radio(
            f"Select a gender for profile{i+1}", dataset.gender.unique()
        )
        gender_code = 0 if selected_gender == "Erkek" else 1

        # COMPANY_SIZE
        selected_company_size = st.selectbox(
            f"Select a company size for profile{i+1}", dataset.company_size.unique()
        )
        # Map selected_company_size to its corresponding code
        company_size_map = {
            "1 - 5 Kişi": 6,
            "6 - 10 Kişi": 5,
            "11 - 20 Kişi": 4,
            "21 - 50 Kişi": 3,
            "51 - 100 Kişi": 2,
            "101 - 249 Kişi": 1,
            "250+": 0,
        }
        company_size_code = company_size_map[selected_company_size]

        # CURRENCY
        selected_currency = st.selectbox(
            f"Select a currency for profile{i+1}", dataset.currency.unique()
        )
        # Map selected_currency to its corresponding code
        currency_map = {
            "₺ - Türk Lirası": 0,
            "$ - Dolar": 1,
            "€ - Euro": 2,
            "£ - Sterlin": 3,
        }
        currency_code = currency_map[selected_currency]

        # RAISE_PERIOD
        selected_raise_period = st.selectbox(
            f"Select a raise period for profile{i+1}", dataset.raise_period.unique()
        )

        input_data.append(
            {
                "level_code": level_code,
                "selected_number_of_technology": selected_number_of_technology,
                "experience_code": experience_code,
                "gender_code": gender_code,
                "company_size_code": company_size_code,
                "currency_code": currency_code,
                "selected_raise_period": selected_raise_period,
            }
        )

    df = pd.DataFrame(input_data)

    # Transform the input data using the scaler
    scaled_data = scaler.transform(df)

    ok = st.button("Predict Your Salary!")

    if ok:
        predicted_salaries = model.predict(scaled_data)
        for i, predicted_salary in enumerate(predicted_salaries):
            pred_sal = predicted_salary * 0.6
            st.subheader(
                f"The estimated monthly salary for profile{i+1} is {pred_sal:.3f} Turkish Lira"
            )


show_prediction_page()
