import streamlit as st

# Set page layout and title
st.set_page_config(
    page_title="CHAYA JEWELLERY",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling to match the exact mobile design perfectly
st.markdown(
    """
    <style>
    /* Hide default Streamlit headers, footers, and padding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Import Serif & Sans-Serif Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #F7F3EE;
        color: #2B2523;
    }

    .stApp {
        background-color: #F7F3EE;
        max-width: 450px;
        margin: 0 auto;
    }

    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    /* Top Sticky Header */
    .top-header {
        position: sticky;
        top: 0;
        background-color: #F7F3EE;
        text-align: center;
        padding: 18px 0 14px 0;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        letter-spacing: 0.18em;
        font-weight: 600;
        color: #1A1A1A;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        z-index: 999;
    }

    .top-header span {
        color: #B58A7E;
        font-weight: 400;
    }

    /* Main Container */
    .content-wrapper {
        padding: 20px 20px 40px 20px;
    }

    /* Subtitle & Headings */
    .sub-tag {
        text-align: center;
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: #A38C82;
        margin-bottom: 12px;
        font-weight: 500;
    }

    .hero-heading {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 32px;
        line-height: 1.18;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 25px;
    }

    .hero-heading em {
        font-style: italic;
        color: #B58A7E;
        font-weight: 400;
    }

    /* Call To Action Container */
    .cta-container {
        background-color: #26211E;
        border-radius: 20px;
        padding: 24px 18px;
        margin-bottom: 30px;
        color: #FFFFFF;
    }

    .cta-title-tag {
        text-align: center;
        font-size: 10px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #C2A69B;
        margin-bottom: 6px;
        font-weight: 500;
    }

    .cta-main-heading {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 24px;
        font-weight: 500;
        margin-bottom: 6px;
        color: #F7F3EE;
    }

    .cta-subtext {
        text-align: center;
        font-size: 12px;
        color: #C0B7B1;
        line-height: 1.45;
        margin-bottom: 20px;
        padding: 0 5px;
    }

    /* Streamlit Native Link Buttons Overrides */
    div[data-testid="stLinkButton"] {
        width: 100% !important;
        margin-bottom: 12px !important;
    }

    div[data-testid="stLinkButton"] > a {
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        padding: 14px 16px !important;
        border-radius: 14px !important;
        text-decoration: none !important;
        box-sizing: border-box !important;
        transition: transform 0.15s ease, opacity 0.15s ease !important;
        border: none !important;
    }

    div[data-testid="stLinkButton"] > a:hover {
        opacity: 0.92 !important;
        transform: translateY(-1px) !important;
    }

    /* First Button (Accent Pinkish Bronze) */
    div[data-testid="stElementContainer"]:nth-of-type(1) div[data-testid="stLinkButton"] > a {
        background-color: #D3A89B !important;
        color: #1A1A1A !important;
    }

    /* Second & Third Buttons (Dark Glass Accent) */
    div[data-testid="stElementContainer"]:nth-of-type(2) div[data-testid="stLinkButton"] > a,
    div[data-testid="stElementContainer"]:nth-of-type(3) div[data-testid="stLinkButton"] > a {
        background-color: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: #FFFFFF !important;
    }

    /* Button Layout Styling */
    .btn-inner {
        display: flex;
        align-items: center;
        gap: 12px;
        width: 100%;
        text-align: left;
    }

    .btn-circle-icon {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        flex-shrink: 0;
    }

    .btn-circle-dark {
        background-color: #26211E;
        color: #FFFFFF;
    }

    .btn-circle-light {
        background-color: #C2A69B;
        color: #26211E;
    }

    .btn-title {
        font-size: 13.5px;
        font-weight: 600;
        line-height: 1.25;
        letter-spacing: -0.01em;
    }

    .btn-sub {
        font-size: 11.5px;
        opacity: 0.75;
        font-weight: 400;
        margin-top: 2px;
    }

    .btn-arrow {
        font-size: 16px;
        opacity: 0.8;
        padding-left: 8px;
    }

    /* Hero Image */
    .hero-card {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        background-color: #E2CDC4;
        margin-bottom: 25px;
    }

    .hero-card img {
        width: 100%;
        display: block;
        object-fit: cover;
    }

    .badge {
        position: absolute;
        bottom: 14px;
        left: 14px;
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(8px);
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: 500;
        color: #333;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .badge-dot {
        width: 6px;
        height: 6px;
        background-color: #B58A7E;
        border-radius: 50%;
    }

    /* Value Proposition Section */
    .text-block-card {
        background-color: rgba(255,255,255,0.5);
        border-radius: 16px;
        padding: 20px 18px;
        margin-bottom: 25px;
        text-align: center;
    }

    .main-description {
        font-size: 14px;
        line-height: 1.55;
        color: #4A423E;
        margin-bottom: 20px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        padding-top: 16px;
        border-top: 1px solid rgba(0,0,0,0.08);
    }

    .stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 700;
        color: #1A1A1A;
    }

    .stat-desc {
        font-size: 11px;
        color: #7A6E67;
        margin-top: 2px;
        line-height: 1.3;
    }

    .stat-full {
        grid-column: span 2;
        text-align: center;
        margin-top: 4px;
    }

    /* Features Section */
    .feature-item {
        text-align: center;
        margin-bottom: 22px;
    }

    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 17px;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 4px;
    }

    .feature-desc {
        font-size: 12.5px;
        color: #665C55;
        line-height: 1.5;
    }

    /* Copy Block */
    .copy-block {
        text-align: center;
        padding: 15px 5px 25px 5px;
    }

    .copy-heading {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        line-height: 1.25;
        color: #1A1A1A;
        margin-bottom: 12px;
    }

    .copy-text {
        font-size: 12.5px;
        line-height: 1.6;
        color: #5C524B;
    }

    .footer-note {
        text-align: center;
        font-size: 11px;
        color: #8C7F77;
        margin-top: 20px;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1. Header
st.markdown(
    '<div class="top-header">CHAYA <span>JEWELLERY</span></div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# 2. Main Title Section (Directly at top for non-scroll access)
st.markdown(
    """
    <div class="sub-tag">— ZURICH · CERTIFIED DIAMONDS —</div>
    <div class="hero-heading">
        Design the <em>Perfect</em><br>Engagement Ring
    </div>
    """,
    unsafe_allow_html=True,
)

# 3. CTA Block (Interactive Functional Streamlit Link Buttons)
st.markdown(
    """
    <div class="cta-container">
        <div class="cta-title-tag">START THE CONVERSATION</div>
        <div class="cta-main-heading">Three ways to reach us</div>
        <div class="cta-subtext">Pick whichever feels right — a quick chat, a browse, or a booked call.</div>
    """,
    unsafe_allow_html=True,
)

# Working Button 1: WhatsApp
st.link_button(
    label="""
        <div class="btn-inner">
            <div class="btn-circle-icon btn-circle-dark">💬</div>
            <div style="flex-grow: 1;">
                <div class="btn-title">Chat with us on WhatsApp</div>
                <div class="btn-sub">Usually replies within the hour</div>
            </div>
            <span class="btn-arrow">→</span>
        </div>
    """,
    url="https://wa.me/41790000000",
    use_container_width=True,
)

# Working Button 2: Website
st.link_button(
    label="""
        <div class="btn-inner">
            <div class="btn-circle-icon btn-circle-light">🌐</div>
            <div style="flex-grow: 1;">
                <div class="btn-title">Visit chaya-jewellery.ch</div>
                <div class="btn-sub">See the full collection & craftsmanship</div>
            </div>
            <span class="btn-arrow">→</span>
        </div>
    """,
    url="https://chaya-jewellery.ch",
    use_container_width=True,
)

# Working Button 3: Calendly
st.link_button(
    label="""
        <div class="btn-inner">
            <div class="btn-circle-icon btn-circle-light">📅</div>
            <div style="flex-grow: 1;">
                <div class="btn-title">Book a 30-minute consultation</div>
                <div class="btn-sub">Pick a slot on our Calendly</div>
            </div>
            <span class="btn-arrow">→</span>
        </div>
    """,
    url="https://calendly.com",
    use_container_width=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# 4. Hero Ring Image
st.markdown(
    """
    <div class="hero-card">
        <img src="https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&q=80&w=800" alt="Engagement Ring in Box" />
        <div class="badge">
            <span class="badge-dot"></span> Ethically sourced, since 1976
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. Guarantee Card
st.markdown(
    """
    <div class="text-block-card">
        <div class="main-description">
            Get the best-price certified diamond engagement ring in Switzerland and a fully planned proposal in 30 days — or you get your money back.
        </div>
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-num">30</div>
                <div class="stat-desc">days to a<br>planned proposal</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">GIA</div>
                <div class="stat-desc">& IGI certified<br>stones</div>
            </div>
            <div class="stat-full">
                <div class="stat-num">100%</div>
                <div class="stat-desc">money-back guarantee</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 6. Features Breakdown
st.markdown(
    """
    <div>
        <div class="feature-item">
            <div class="feature-title">Priced with integrity</div>
            <div class="feature-desc">No showroom markup — the same stone, without the price built for one.</div>
        </div>
        <div class="feature-item">
            <div class="feature-title">Master goldsmiths</div>
            <div class="feature-desc">Every setting is hand-finished in-house, not outsourced.</div>
        </div>
        <div class="feature-item">
            <div class="feature-title">Proposal, planned</div>
            <div class="feature-desc">Ring, timeline, and setting sorted together — in 30 days.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 7. Editorial Section
st.markdown(
    """
    <div class="copy-block">
        <div class="sub-tag">WORN TODAY, TREASURED TOMORROW</div>
        <div class="copy-heading">One ring. One decision that has to be right.</div>
        <div class="copy-text">
            Tell us the stone, the budget, and the date you're working toward. We'll shortlist certified diamonds, size the setting, and have it ready in time — no back-and-forth with three different jewellers.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 8. Footer
st.markdown(
    """
    <div class="footer-note">
        Certified by GIA, IGI & HRD · Master goldsmiths since 1976 · Zurich, Switzerland
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
