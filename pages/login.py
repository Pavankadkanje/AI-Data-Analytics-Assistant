import streamlit as st
import hashlib
import mysql.connector

from utils.database import get_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(name, email, password):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        password_hash = hash_password(password)

        query = """
        INSERT INTO users (name, email, password_hash)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (name, email, password_hash)
        )

        connection.commit()
        return True, "Account created successfully!"

    except mysql.connector.IntegrityError:
        return False, "An account with this email already exists."

    except Exception as e:
        return False, f"Database error: {e}"

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def login_user(email, password):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        password_hash = hash_password(password)

        query = """
        SELECT id, name, email
        FROM users
        WHERE email = %s
        AND password_hash = %s
        """

        cursor.execute(
            query,
            (email, password_hash)
        )

        user = cursor.fetchone()

        return user

    except Exception as e:
        st.error(f"Database error: {e}")
        return None

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def show():

    st.title("👤 Account")

    # Initialize login session
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_name" not in st.session_state:
        st.session_state.user_name = None

    # Already logged in
    if st.session_state.logged_in:

        st.success(
            f"Welcome, {st.session_state.user_name}! You are logged in."
        )

        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.user_name = None
            st.rerun()

        return

    option = st.radio(
        "Choose an option",
        [
            "🔐 Login",
            "📝 Register",
            "👤 Continue as Guest"
        ]
    )

    # LOGIN
    if option == "🔐 Login":

        st.subheader("Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if not email or not password:
                st.warning("Please enter email and password.")

            else:

                user = login_user(
                    email,
                    password
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.user_name = user["name"]
                    st.session_state.user_email = user["email"]

                    st.success(
                        f"Welcome {user['name']}!"
                    )

                    st.rerun()

                else:
                    st.error(
                        "Invalid email or password."
                    )

    # REGISTER
    elif option == "📝 Register":

        st.subheader("Create Account")

        name = st.text_input("Name")

        email = st.text_input(
            "Email",
            key="register_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Create Account"):

            if not name or not email or not password:
                st.warning(
                    "Please fill all fields."
                )

            elif password != confirm_password:
                st.error(
                    "Passwords do not match."
                )

            elif len(password) < 6:
                st.warning(
                    "Password must contain at least 6 characters."
                )

            else:

                success, message = register_user(
                    name,
                    email,
                    password
                )

                if success:
                    st.success(message)
                    st.info(
                        "Your account has been created. Select Login to continue."
                    )

                else:
                    st.error(message)

    # GUEST
    elif option == "👤 Continue as Guest":

        st.info(
            "You can continue using the application without creating an account."
        )

        if st.button("Continue as Guest"):

            st.session_state.logged_in = False
            st.session_state.user_name = "Guest"

            st.success(
                "Continuing as Guest."
            )