import streamlit as st
import pandas as pd
import pickle
# App configuration
st.set_page_config(page_title="ML App", layout="wide")

# Title and description
st.title( "💹 BottleBot 🍷 - Prediction App  ")
st.markdown("""
Welcome to the ML Prediction App!  
Use the sidebar to navigate through the sections:
- **Data**: Preview and understand the dataset
- **Visuals**: Explore feature distributions
- **Predict**: Input values to make predictions using the trained ML model
""")

# Sidebar
st.sidebar.title("📂 Navigation")
app_mode = st.sidebar.selectbox(
    "Choose the section",
    ["Data", "Visuals", "Predict"],
    help="Select the part of the app you want to view or interact with"
)

# Load model and data
model = pickle.load(open("model.pkl", "rb"))
df = pd.read_csv("data/dataset.csv")

# Data Section
if app_mode == "Data":
    st.subheader("📊 Dataset Overview")
    st.markdown("Here's a quick look at the dataset used to train the machine learning model.")
    st.dataframe(df.head())
    st.write(f"**Shape of dataset**: {df.shape}")
    st.write("**Statistical summary**:")
    st.write(df.describe())

    with st.expander("ℹ️ About the Dataset"):
        st.markdown("""
        This dataset contains features related to [your dataset context here, e.g., chemical properties of wine, patient health data, etc.].
        The target variable is [target_column].
        """)

# Visualizations Section
elif app_mode == "Visuals":
    st.subheader("📈 Visualizations")
    st.markdown("Here are some basic charts for numeric columns in the dataset.")
    st.bar_chart(df.select_dtypes('number'))

    with st.expander("ℹ️ Tips"):
        st.markdown("""
        - These charts help you understand feature distributions.
        - Use this insight to identify skewed data or outliers.
        """)

# Prediction Section
elif app_mode == "Predict":
    st.subheader("🎯 Make a Prediction")
    st.markdown("Enter values for the required features below to get a prediction.")

    # Input fields with help text
    input1 = st.number_input("Feature 1", help="This is a numeric input for Feature 1 (e.g., acidity, age, etc.)")
    input2 = st.number_input("Feature 2", help="This is a numeric input for Feature 2 (e.g., sugar level, income, etc.)")
    input3 = st.number_input("Feature 3", help="This is a numeric input for Feature 3 (e.g., alcohol %, cholesterol level, etc.)")

    input_data = [[input1, input2, input3]]

    if st.button("🔍 Predict"):
        try:
            prediction = model.predict(input_data)
            st.success(f"✅ Prediction Result: {prediction[0]}")
            st.caption("This result is based on the machine learning model trained with historical data.")
        except Exception as e:
            st.error(f"⚠️ Prediction failed: {e}")

    with st.expander("ℹ️ Need Help?"):
        st.markdown("""
        - Fill in all input fields with numeric values.
        - Click the **Predict** button to generate the result.
        - Make sure input ranges are reasonable based on training data.
        """)
