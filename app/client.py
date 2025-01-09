import streamlit as st
import requests

st.title("SQL Injection Test Server")
st.write("Use this interface to test your Flask server.")

# Input fields
server_url = "http://127.0.0.1:5000/login"
username = st.text_input(label="Username", placeholder="Enter your username")
password = st.text_input(label="Password", type="password", placeholder="Enter your password")

# Button to make the request
if st.button("Login"):
    try:
        # Send the request with data
        payload = {"username": username, "password": password, "param": "streamlit"}
        response = requests.post(server_url, data=payload)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                # Display the Access Granted page
                st.success("You are logged in!")
                st.markdown(
                    f"""
                    <div style="text-align: center; color: green; font-size: 48px; font-weight: bold;">
                        ACCESS GRANTED
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error(response_data.get("message", "Invalid credentials."))
        else:
            st.error("Error communicating with the server.")
    except Exception as e:
        st.error(f"Error: {e}")
