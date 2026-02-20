import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🏋️ Personalized Workout & Diet Planner")

name = st.text_input("Enter your name")
height = st.number_input("Height (cm)", min_value=50)
weight = st.number_input("Weight (kg)", min_value=20)

if st.button("Generate Plan"):
    bmi = weight / ((height/100)**2)

    prompt = f"""
    BMI is {bmi:.1f}.
    Suggest a simple Indian student diet plan.
    Include breakfast, lunch and dinner.
    """

    response = model.generate_content(prompt)

    st.subheader("Your BMI")
    st.write(round(bmi,1))

    st.subheader("AI Diet Plan")
    st.write(response.text)