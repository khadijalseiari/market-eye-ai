# streamlit_app.py

import streamlit as st
import requests

# Point Streamlit to FastAPI backend
API_URL = "http://localhost:8000"

def signup():
    st.header("Sign Up")
    username = st.text_input("Username", key="su_user")
    password = st.text_input("Password", type="password", key="su_pass")
    if st.button("Create Account"):
        response = requests.post(
            f"{API_URL}/signup",
            json={"username": username, "password": password}
        )
        if response.status_code == 201:
            st.success("✅ Account created! Please log in.")
        else:
            error = response.json().get("detail") or response.json().get("error")
            st.error(f"Error: {error}")

def login():
    st.header("Log In")
    username = st.text_input("Username", key="li_user")
    password = st.text_input("Password", type="password", key="li_pass")
    if st.button("Log In"):
        response = requests.post(
            f"{API_URL}/login",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:
            st.success("✅ Logged in successfully!")
        else:
            error = response.json().get("detail") or response.json().get("error")
            st.error(f"Error: {error}")

def main():
    st.title("Market Eye Authentication")
    choice = st.sidebar.radio("Action", ["Log In", "Sign Up"])
    if choice == "Sign Up":
        signup()
    else:
        login()

if __name__ == "__main__":
    main()