# Freight Cost Prediction System

An end-to-end Machine Learning project that predicts freight/shipping cost based on shipment and product details. The project includes data preprocessing, feature engineering, model training, and a deployed Streamlit web app for real-time predictions.

---

## Project Overview

This system predicts **freight cost (USD)** using historical supply chain data.  
It helps estimate shipping costs based on:

- Order quantity
- Product value
- Packaging cost
- Unit price
- Insurance cost
- Delivery delay
- Cost per KG
- Shipment-related indicators

---

## Machine Learning Approach

- Data Cleaning & Preprocessing
- Feature Engineering
- Handling missing values
- Log transformation of target (for stability in some versions)
- Train/Test Split
- Model Training (Random Forest)
- Evaluation using:
  - MAE
  - RMSE
  - R² Score

---

##  Dataset

- Source: Kaggle Supply Chain Shipment Pricing Dataset  
- Size: ~10,000+ records  
- Target variable:
  - `freight_cost_usd`

---

## Features Used

- Line Item Quantity  
- Line Item Value  
- Pack Price  
- Unit Price  
- Line Item Insurance (USD)  
- PO Missing (engineered feature)  
- PQ Missing (engineered feature)  
- Delivery Delay  
- Cost per KG  

---

## The application is deployed using:
- Streamlit for frontend UI
- Docker for containerization
- Render for cloud deployment

### Run - Live App: https://vendor-cost-optimization-using.onrender.com
