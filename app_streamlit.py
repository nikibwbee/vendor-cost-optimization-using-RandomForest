import streamlit as st
import pickle
import pandas as pd
import numpy as np   # ✅ IMPORTANT ADDITION

# Load model + features
model = pickle.load(open("freight_cost_model.pkl", "rb"))
features = pickle.load(open("model_features.pkl", "rb"))

st.title("🚚 Freight Cost Prediction App")

st.write("Enter shipment details below:")

# Input fields
line_item_quantity = st.number_input("Line Item Quantity", value=10)
line_item_value = st.number_input("Line Item Value", value=500)
pack_price = st.number_input("Pack Price", value=50)
unit_price = st.number_input("Unit Price", value=5)
line_item_insurance_usd = st.number_input("Insurance USD", value=2)
po_missing = st.number_input("PO Missing", value=0)
pq_missing = st.number_input("PQ Missing", value=0)
delivery_delay = st.number_input("Delivery Delay", value=3)
cost_per_kg = st.number_input("Cost per KG", value=20)

# Predict button
if st.button("Predict Freight Cost"):
    
    # create dataframe
    data = pd.DataFrame([{
        "line_item_quantity": line_item_quantity,
        "line_item_value": line_item_value,
        "pack_price": pack_price,
        "unit_price": unit_price,
        "line_item_insurance_usd": line_item_insurance_usd,
        "po_missing": po_missing,
        "pq_missing": pq_missing,
        "delivery_delay": delivery_delay,
        "cost_per_kg": cost_per_kg,
    }])

    # align features
    data = data.reindex(columns=features, fill_value=0)

    # prediction (LOG SCALE)
    prediction = model.predict(data)

    # ✅ FIX: convert back to real cost
    final_cost = np.exp(prediction[0])

    st.success(f"💰 Predicted Freight Cost: {final_cost:.2f}")