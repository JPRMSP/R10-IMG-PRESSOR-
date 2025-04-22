import streamlit as st

# You can change this password to anything you'd like
PASSWORD = "letmein"

def check_password():
    """
    Prompts user for a password and stores validation result in Streamlit's session state.
    Returns True if the password is correct, False otherwise.
    """

    def password_entered():
        """Callback to check password when entered"""
        if st.session_state["password"] == PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove password from session
        else:
            st.session_state["password_correct"] = False

    # If password hasn't been entered yet
    if "password_correct" not in st.session_state:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        return False

    # If password was entered incorrectly
    elif not st.session_state["password_correct"]:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        st.error("❌ Incorrect password")
        return False

    # If password is correct
    else:
        return True
