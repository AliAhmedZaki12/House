# 🏡 House Price Prediction 
(https://houseprice-app12.streamlit.app/)

##  (Overview)
This project focuses on building an intelligent **machine learning model** capable of accurately predicting **house prices** based on a variety of real estate features.

The system leverages advanced regression algorithms and ensemble techniques to deliver **high-accuracy predictions**, providing valuable insights for home buyers, investors, and real estate professionals.

---

##  (Project Description)
The project uses structured housing data to analyze and learn the relationship between different property features and their market prices.

It combines the power of multiple machine learning models through an **ensemble approach** to enhance performance and stability.

###  Algorithms Used
- **Random Forest Regressor**  
- **Gradient Boosting Regressor**  
- **XGBoost Regressor**  
- **CatBoost Regressor**  
---

## ( Workflow )

1. **Data Collection** – Load and explore real estate datasets.  
2. **Preprocessing** – Handle missing values, encode categorical data, and scale numeric features.  
3. **Feature Engineering** – Remove redundant or correlated features and select the most informative ones.  
4. **Model Training** – Train multiple regression models with hyperparameter tuning.  
5. **Evaluation** – Assess performance using standard regression metrics.  
6. **Model Saving** – Export the final trained model for deployment using Joblib.  

---

##  (Evaluation Metrics)

| Metric | Description |
|--------|--------------|
| **R² Score** | Measures how well the model explains variance in data. |
| **MAE (Mean Absolute Error)** | Average absolute difference between predicted and actual prices. |
| **RMSE (Root Mean Squared Error)** | Penalizes larger prediction errors more heavily. |

These metrics collectively provide a comprehensive performance assessment for regression models.

---

## (Example Input)

When deployed interactively, users can input property details as follows:

| Feature | Example Value |
|----------|----------------|
| **Number of Bedrooms** | 
| **Number of Bathrooms** |
| **Living Area (sqft)** | 
| **Number of Floors** | 
| **Waterfront View** | 
| **View Quality** | 
| **ZIP Code** | 
| **House Age (years)** | 

After entering these values, the system generates a predicted house price instantly.

---

