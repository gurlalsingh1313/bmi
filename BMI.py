import streamlit as st
def calculate_bmi(height, weight):
    if height <= 0 or weight <= 0:
        return 0
    bmi = weight / (height / 100) ** 2
    return bmi

st.title("BMI CALCULATOR")
height = st.number_input("Enter your height (in cm)", min_value=0)
weight = st.number_input("Enter your weight (in kg)", min_value=0)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(height, weight)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Interpret the BMI
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")

st.markdown("BMI Categories:")
st.markdown(" - Underweight: < 18.5")
st.markdown(" - Normal Weight: 18.5 - 24.9")
st.markdown(" - Overweight: 25 - 29.9")
st.markdown(" - Obese: 30 or greater")





