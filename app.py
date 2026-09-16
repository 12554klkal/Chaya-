import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CHAYA Jewellery",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling (Mobile Optimized, Luxury Aesthetic)
st.markdown(
    """
    <style>
    /* Hide Streamlit default UI elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global background and typography */
    body {
        background-color: #FAFAFA;
        font-family: 'Playfair Display', 'Helvetica Neue', serif;
        color: #111111;
    }
    
    .stApp {
        max-width: 480px;
        margin: 0 auto;
        padding-top: 1rem;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* Typography */
    .brand-title {
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
        color: #1A1A1A;
    }

    .subtitle {
        font-size: 0.85rem;
        text-align: center;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #777777;
        margin-bottom: 0.8rem;
    }

    .description {
        font-size: 0.95rem;
        text-align: center;
        line-height: 1.5;
        color: #444444;
        margin-bottom: 1.5rem;
        padding: 0 10px;
    }

    /* Primary CTA Link Buttons */
    .btn-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 2rem;
    }

    .cta-btn {
        display: block;
        width: 100%;
        padding: 14px 20px;
        text-align: center;
        text-decoration: none !important;
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        border-radius: 4px;
        transition: all 0.3s ease;
        box-sizing: border-box;
    }

    .btn-primary {
        background-color: #1A1A1A;
        color: #FFFFFF !important;
        border: 1px solid #1A1A1A;
    }

    .btn-secondary {
        background-color: #FFFFFF;
        color: #1A1A1A !important;
        border: 1px solid #1A1A1A;
    }

    .cta-btn:hover {
        opacity: 0.85;
        transform: translateY(-1px);
    }
    </style>
    """,
    unsafe_allow_allowed_html=True,
    unsafe_allow_html=True,
)

# Header Section (Above the fold)
st.markdown('<div class="brand-title">CHAYA</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">FINE JEWELLERY • ZURICH</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">Handcrafted timeless elegance. Discover our exclusive collection or book a private consultation at our Zurich boutique.</div>',
    unsafe_allow_html=True,
)

# Call to Action Buttons (Above the fold for mobile)
st.markdown(
    """
    <div class="btn-container">
        <a href="https://chaya-jewellery.netlify.app" target="_blank" class="cta-btn btn-primary">
            Explore Collection
        </a>
        <a href="https://www.1stdibs.com/dealers/chaya-jewellery/" target="_blank" class="cta-btn btn-secondary">
            Visit Online Store
        </a>
        <a href="mailto:info@chayajewellery.com" target="_blank" class="cta-btn btn-secondary">
            Book Private Appointment
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
