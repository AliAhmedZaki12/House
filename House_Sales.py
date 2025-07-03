import streamlit as st
import pandas as pd
import joblib

# تحميل النموذج
model = joblib.load("final_house.pkl")

# ✅ تحميل قائمة الأعمدة الأصلية (إذا كنت قد حفظتها أثناء التدريب)
try:
    model_columns = joblib.load("columns.pkl")
except:
    model_columns = model.named_steps['preprocessor'].feature_names_in_.tolist()

st.title("🏡 House Price Prediction (Simplified)")
st.markdown("### Enter the basic information about the house:")

# ========== 📥 إدخال البيانات من المستخدم ==========
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1.0, 5.0, 2.0, step=0.25)
sqft_living = st.number_input("Living Area (sqft)", 300, 10000, 2000)
floors = st.selectbox("Number of Floors", [1.0, 1.5, 2.0, 2.5, 3.0])
waterfront = st.selectbox("Waterfront View", [0, 1])
view = st.selectbox("View Quality", [0, 1, 2, 3, 4])
zipcode = st.selectbox("ZIP Code", [98001, 98004, 98006, 98033, 98052, 98059, 98103, 98115, 98117, 98125])
house_age = st.slider("House Age", 0, 120, 20)

# ========== ⏳ عند الضغط على زر التنبؤ ==========
if st.button("🔍 Predict Price"):
    # إنشاء إطار البيانات مع القيم المدخلة + القيم الافتراضية للأعمدة الأخرى
    input_data = pd.DataFrame([{
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'zipcode': zipcode,
        'house_age': house_age,
        'sqft_lot': 5000,
        'condition': 3,
        'grade': 7,
        'sqft_above': sqft_living,
        'sqft_basement': 0,
        'lat': 47.5,
        'long': -122.2,
        'sqft_living15': sqft_living,
        'sqft_lot15': 5000,
        'renovation_age': 0,
        'sale_year': 2022
    }])

    # ✅ تأكد من أن جميع الأعمدة المطلوبة موجودة (وإضافة المفقود إن وجد)
    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0  # قيمة افتراضية

    # ✅ إعادة ترتيب الأعمدة
    input_data = input_data[model_columns]

    # التنبؤ بالسعر
    predicted_price = model.predict(input_data)[0]

    # عرض النتيجة
    st.success(f"💲 Estimated House Price: ${predicted_price:,.2f}")
    st.caption("Developed by Ali Ahmed Zaki")
