import streamlit as st
import re

st.title("🔐 SecurePass Analyzer")

password = st.text_input("Enter your password", type="password")

if st.button("Analyze Password"):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 2
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 2
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 2
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        suggestions.append("Add a special character.")

    if score >= 8:
        st.success(f"Strong Password ({score}/10)")
    elif score >= 5:
        st.warning(f"Medium Password ({score}/10)")
    else:
        st.error(f"Weak Password ({score}/10)")

    if suggestions:
        st.subheader("Suggestions")
        for s in suggestions:
            st.write("- " + s)
    else:
        st.success("Excellent! Your password is very strong.")