import streamlit as st
import string
import secrets
import random

# Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="wide")

# Custom CSS to center content and style the footer
st.markdown("""
    <style>
    /* Centers the main block */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    /* Fixed Footer styling */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #0077b5;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout: Create three columns and use the middle one to center the UI
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("🔐 Random Password Generator")
    
    length = st.slider("Choose password length", 6, 32, 12)
    use_letters = st.checkbox("Include letters", True)
    use_numbers = st.checkbox("Include numbers", True)
    use_symbols = st.checkbox("Include symbols", True)
    exclude = st.text_input("Exclude characters (optional)", "lI1O0")

    if st.button("Generate Password", use_container_width=True):
        groups = []

        if use_letters:
            letters = "".join(c for c in string.ascii_letters if c not in exclude)
            if letters:
                groups.append(letters)

        if use_numbers:
            numbers = "".join(c for c in string.digits if c not in exclude)
            if numbers:
                groups.append(numbers)

        if use_symbols:
            symbols = "".join(c for c in "!@#$%^&*?" if c not in exclude)
            if symbols:
                groups.append(symbols)

        if not groups:
            st.error("Please select at least one character type.")
        elif length < len(groups):
            st.error(f"Password length must be at least {len(groups)}.")
        else:
            all_chars = "".join(groups)
            # Ensure at least one character from each selected group is used
            password = [secrets.choice(group) for group in groups]
            # Fill the rest randomly
            password += [secrets.choice(all_chars) for _ in range(length - len(groups))]
            # Shuffle for better randomness
            random.SystemRandom().shuffle(password)

            final_password = "".join(password)

            st.success("Password generated successfully!")
            st.code(final_password, language=None)
            st.caption("Use the copy button on the code box to copy it.")

# Footer Section
footer_html = """
<div class="footer">
    <p>Created by <b>Chirag Parashar</b> | 
    <a href="https://www.linkedin.com/in/chiragparashar9665" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" height="20" style="vertical-align: middle; margin-right: 5px;">
        Connect on LinkedIn
    </a>
    </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)