import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
def load_model():
    with open('model_1.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Create a Streamlit app
def main():

    st.image("de.webp", use_column_width=True, width=100)
    st.title("Customer Churn Prediction")

    # Load the model
    model = load_model()

    # Get user input
    age = st.slider("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])

    # Perform label encoding for Gender
    gender_encoder = LabelEncoder()
    gender_encoded = gender_encoder.fit_transform([gender])

    monthly_bill = st.number_input("Monthly Bill", min_value=0.0, value=50.0)
    subscription_length = st.slider("Subscription Length (months)")
    
    # Calculate the result of Monthly Bill * Subscription Length
    Total_subscription_cost = monthly_bill * subscription_length

    # Get user input for each location using checkboxes
    location_a = st.checkbox("Houston")
    location_b = st.checkbox("Miami")
    location_c = st.checkbox("Los Angeles")
    location_d = st.checkbox("New York")
    location_e = st.checkbox("Chicago")

    total_monthly_gb = st.number_input("Total Monthly GB", min_value=0.0, value=5.0)
    
    # Calculate the ratio Total Monthly GB / Monthly Bill
    Per_GB_Cost = total_monthly_gb / monthly_bill

    # Prepare user input data
    input_data = [age, gender_encoded[0],subscription_length, monthly_bill, total_monthly_gb,
                  location_a, location_b, location_c, location_d, location_e,Per_GB_Cost,
                   Total_subscription_cost ]  # Include the calculated ratio

    # Make a prediction using the loaded model
    prediction = model.predict([input_data])

    # Display the prediction result
    if prediction[0] == 1:
        st.write("Predicted Churn Status: Churn")
    else:
        st.write("Predicted Churn Status: Not Churn")

if __name__ == "__main__":
    main()
