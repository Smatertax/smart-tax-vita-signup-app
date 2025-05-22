
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Tax VITA Program Sign-Up")

st.title("📋 Smart Tax – Free IRS VITA Tax Help Sign-Up")
st.markdown("Complete this form to request free tax help through our IRS-certified VITA program. We'll follow up to confirm your appointment.")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
zip_code = st.text_input("ZIP Code")
filing_status = st.selectbox("Filing Status", ["Single", "Married", "Head of Household"])
income_type = st.multiselect("Income Sources", ["W-2", "1099/Contract", "Self-Employed", "Social Security", "Unemployment", "Other"])

preferred_day = st.selectbox("Preferred Day for Appointment", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
preferred_time = st.selectbox("Preferred Time", ["Morning", "Afternoon", "Evening"])

comments = st.text_area("Additional Notes (optional)")

# Submission logic
if st.button("Submit Sign-Up"):
    submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "ZIP Code": zip_code,
        "Filing Status": filing_status,
        "Income Sources": ", ".join(income_type),
        "Preferred Day": preferred_day,
        "Preferred Time": preferred_time,
        "Notes": comments,
        "Submitted At": submitted_at
    }

    # Save to CSV
    df = pd.DataFrame([record])
    df.to_csv("vita_signups.csv", mode='a', header=not pd.io.common.file_exists("vita_signups.csv"), index=False)

    st.success("✅ Thank you! Your request has been submitted. We'll contact you to schedule your appointment.")
    st.balloons()

st.markdown("---")
st.caption("Smart Tax – Powered by the IRS VITA Program | Free tax help for eligible community members.")
