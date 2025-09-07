import streamlit as st
import json, os

BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, "valid_icd10_asthma.json")) as f:
    VALID = json.load(f)
with open(os.path.join(BASE_DIR, "asthma_mb.json")) as f:
    MB = json.load(f)

st.title("Basket Checker — Asthma MB )
st.write("Form version: allows you to create a new basket manually when trigger_creation condition is met.")

with st.form("basket_form"):
    icd = st.text_input("Submitted ICD-10 code (free text)").strip().upper()
    med = st.text_input("Requested medicine code (free text)").strip().upper()
    qty = st.number_input("Requested quantity", min_value=0, value=1)
    loaded = st.checkbox("Is ASTHMA MB already loaded?")
    submit_basket = st.form_submit_button("Check basket")

show_create_form = False

if submit_basket:
    valid_ic = icd in [code.upper() for code in VALID["valid_icd10"]]
    med_codes = [m["code"].upper() for m in MB["medicines"]]
    med_in_mb = med in med_codes
    qty_ok = qty <= MB["max_quantity_per_request"]

    if valid_ic and med_in_mb and qty_ok:
        if not loaded:
            st.success("Action: trigger_creation — ICD valid, med in basket, qty OK.")
            show_create_form = True
        else:
            st.success("Action: proceed_to_authorization — Basket loaded; ready for authorization.")
    else:
        reasons = []
        if not valid_ic:
            reasons.append("ICD10 not in valid list")
        if not med_in_mb:
            reasons.append("Requested med not in MB")
        if not qty_ok:
            reasons.append("Requested qty exceeds max allowed")
        st.error("Action: manual_intervention — " + "; ".join(reasons))

if show_create_form:
    st.subheader("📝 Create Your Own Basket")
    with st.form("create_basket_form"):
        med1_name = st.text_input("Medicine Name")
        med1_code = st.text_input("Medicine Code")
        med1_qty = st.number_input("Medicine Max Quantity", min_value=1, value=1)

       # med2_name = st.text_input("Medicine 2 Name")
       # med2_code = st.text_input("Medicine 2 Code")
       # med2_qty = st.number_input("Medicine 2 Max Quantity", min_value=1, value=1)

        submit_new = st.form_submit_button("Create Basket")

    if submit_new:
        new_basket = {
            "custom_basket": [
                {"name": med1_name, "code": med1_code, "max_qty": med1_qty},
                {"name": med2_name, "code": med2_code, "max_qty": med2_qty},
            ]
        }
        st.success("🎉 Basket Created!")
        st.json(new_basket)
