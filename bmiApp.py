import streamlit as st

# Application Title
st.title("🏋️ แอปพลิเคชันคำนวณค่าดัชนีมวลกาย (BMI)")
st.caption("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

# Input fields for Weight and Height
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=0.0, value=55.0, step=0.1)
height = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=0.0, value=158.0, step=0.1)

# Calculate button
if st.button("คำนวณค่า BMI 🎯"):
    if height > 0:
        # Convert height from centimeters to meters
        height_m = height / 100
        
        # Calculate BMI: weight / (height_m ^ 2)
        bmi = weight / (height_m ** 2)
        
        # Display calculated BMI result
        st.subheader(f"ค่า BMI ของคุณคือ: {bmi:.2f}")
        
        # Interpretation logic based on BMI value
        if bmi < 18.5:
            st.warning("คุณอยู่ในเกณฑ์: ผอม")
        elif 18.5 <= bmi < 23.0:
            st.success("คุณอยู่ในเกณฑ์: สุขภาพดี (ปกติ)")
        elif 23.0 <= bmi < 25.0:
            st.warning("คุณอยู่ในเกณฑ์: ท้วม")
        else:
            st.error("คุณอยู่ในเกณฑ์: อ้วน")
            
        st.divider()
        st.write("นางสาว บัณฑิตา ทิวาวรรณ์ เลขที่ 32 ม.4/14")
    else:
        st.error("กรุณากรอกส่วนสูงให้มากกว่า 0")
