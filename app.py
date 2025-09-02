import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Women Grievance Cell – Dewan College",
    page_icon="🎓",
    layout="centered",
)

# ----------- Custom CSS for styling -------------
st.markdown(
    """
    <style>
    /* Remove padding around main content */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    body {
        background-color: #fff0f5;
    }

    .card {
        background-color: transparent;
        padding: 2rem;
        border-radius: 12px;
        max-width: 600px;
        margin: auto;
    }

    .logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-height: 150px;   /* increase from 100px to 150px */
    width: auto;
}


    h1 {
        color: #d63384;
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 0.3rem;
    }

    h3 {
        text-align: center;
        color: #555;
        font-weight: normal;
        margin-bottom: 1.2rem;
    }

    p {
        text-align: center;
        font-size: 1.05rem;
        color: #333;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }

    .button {
        display: block;
        width: fit-content;
        margin: auto;
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        padding: 0.8em 2em;
        border-radius: 8px;
        text-decoration: none;
        font-size: 1.05rem;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #e754a7;
    }

    .footer {
        text-align: center;
        color: #b30059;
        font-size: 0.85rem;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ----------- Main Content ------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.image("dewan_logo.png", use_container_width=False)

st.markdown("<h1>Congratulations!</h1>", unsafe_allow_html=True)
st.markdown("<h3>Women Grievance Cell – Dewan College</h3>", unsafe_allow_html=True)

st.markdown(
    """
    <p>
        Thank you for your active participation and contribution.  
        Please click below to download your certificate.
    </p>
    """,
    unsafe_allow_html=True,
)

form_link = "https://forms.gle/T38A4hTD3Px1SBPf9"

st.markdown(
    f"""
    <a href="{form_link}" target="_blank" class="button">🎓 Get Certificate</a>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="footer">Empowered Women Empower the World 🌍</div>',
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
