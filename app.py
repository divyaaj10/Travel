import streamlit as st
import pandas as pd
import os

# Load or create user database
if os.path.exists("users.csv"):
    users_df = pd.read_csv("users.csv")
else:
    users_df = pd.DataFrame(columns=["username", "password"])
    users_df.to_csv("users.csv", index=False)

# Set page config
st.set_page_config(page_title="Travel Recommender", layout="wide")

# Background image using HTML + CSS
def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("assets/background.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# Sidebar for navigation
menu = st.sidebar.selectbox("Choose", ["Login", "Register"])

# ----------------- Login Page -----------------
if menu == "Login":
    st.markdown("## 🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users_df['username'].values:
            correct_pw = users_df[users_df['username'] == username]['password'].values[0]
            if password == correct_pw:
                st.success(f"Welcome back, {username}!")
                st.balloons()
                # You can now show the recommendation system part
            else:
                st.error("Incorrect password")
        else:
            st.error("User not found. Please register first.")

# ----------------- Register Page -----------------
elif menu == "Register":
    st.markdown("## 📝 Register")
    new_user = st.text_input("Choose a Username")
    new_pass = st.text_input("Choose a Password", type="password")
    
    if st.button("Register"):
        if new_user in users_df['username'].values:
            st.warning("Username already exists.")
        elif new_user == "" or new_pass == "":
            st.warning("Please fill in all fields.")
        else:
            users_df = users_df.append({"username": new_user, "password": new_pass}, ignore_index=True)
            users_df.to_csv("users.csv", index=False)
            st.success("Registered successfully! Please login.")
