import streamlit as st
import pyttsx3

def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Under Weight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Over Weight"
    elif 30 <= bmi <35:
        category = "Class1 Obesity"
    elif 35 <= bmi < 40:
        category = "Class2 Obesity"
    else:
        category = " Severe Obesity"
    return bmi, category

def main():
    st.image(r"BMI image.jpg")
    st.title("BMI Calculator")
    st.write("Please enter your weight and your height")
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (m)")
    
    if st.button("Calculate BMI"):
        bmi, category = bmi_calculator(height, weight)
        st.write(f"Your BMI is {bmi:.2f} and your category is {category}")

        # Using pyttsx3 to speak the result
        speak = pyttsx3.init()
        speak.say(f"Your BMI is {bmi:.2f} and your category is {category}")
        speak.runAndWait()

if __name__ == "__main__":
    main()

    
