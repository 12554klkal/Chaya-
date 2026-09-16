import streamlit as st

# Set page layout and title
st.set_page_config(
    page_title="CHAYA JEWELLERY",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling to match the exact design perfectly
st.markdown(
    """
    <style>
    /* Hide default Streamlit headers, footers, and padding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Import Serif Font */
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

    /* Hero Card & Image Overlay */
    .hero-card {
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        background-color: #E2CDC4;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    .hero-card img {
        width: 100%;
        display: block;
        object-fit: cover;
    }

    .badge {
        position: absolute;
        bottom: 16px;
        left: 16px;
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(8px);
        padding: 8px 14px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 500;
        color: #333;
        display: flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .badge-dot {
        width: 6px;
        height: 6px;
        background-color: #B58A7E;
        border-radius: 50%;
        display: inline-block;
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
        font-size: 34px;
        line-height: 1.18;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 35px;
    }

    .hero-heading em {
        font-style: italic;
        color: #B58A7E;
        font-weight: 400;
    }

    /* Call To Action Section (Immediate Access) */
    .cta-container {
        background-color: #26211E;
        border-radius: 20px;
        padding: 28px 20px;
        margin-bottom: 40px;
        color: #FFFFFF;
    }

    .cta-title-tag {
        text-align: center;
        font-size: 11px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #C2A69B;
        margin-bottom: 8px;
        font-weight: 500;
    }

    .cta-main-heading {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 26px;
        font-weight: 500;
        margin-bottom: 8px;
        color: #F7F3EE;
    }

    .cta-subtext {
        text-align: center;
        font-size: 13px;
        color: #C0B7B1;
        line-height: 1.45;
        margin-bottom: 24px;
        padding: 0 10px;
    }

    /* Button Styling */
    .action-btn {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        padding: 16px 20px;
        border-radius: 16px;
        text-decoration: none !important;
        margin-bottom: 12px;
        transition: all 0.2s ease;
        box-sizing: border-box;
    }

    .btn-whatsapp {
        background-color: #CFA396;
        color: #1A1A1A !important;
    }

    .btn-outline {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #FFFFFF !important;
    }

    .btn-content {
        display: flex;
        align-items: center;
        gap: 14px;
        text-align: left;
    }

    .btn-icon {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }

    .btn-whatsapp .btn-icon {
        background-color: #26211E;
        color: #FFFFFF;
    }

    .btn-outline .btn-icon {
        background-color: #C2A69B;
        color: #26211E;
    }

    .btn-text-main {
        font-size: 14px;
        font-weight: 600;
        line-height: 1.2;
    }

    .btn-text-sub {
        font-size: 12px;
        opacity: 0.75;
        font-weight: 400;
        margin-top: 2px;
    }

    .arrow-icon {
        font-size: 16px;
        opacity: 0.7;
    }

    /* Value Proposition Section */
    .text-block-card {
        background-color: rgba(255,255,255,0.4);
        border-radius: 16px;
        padding: 24px 20px;
        margin-bottom: 30px;
        text-align: center;
    }

    .main-description {
        font-size: 15px;
        line-height: 1.6;
        color: #4A423E;
        margin-bottom: 24px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .stat-item {
        text-align: center;
    }

    .stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        font-weight: 700;
        color: #1A1A1A;
    }

    .stat-desc {
        font-size: 11px;
        color: #7A6E67;
        margin-top: 4px;
        line-height: 1.3;
    }

    .stat-full {
        grid-column: span 2;
        text-align: center;
        margin-top: 5px;
    }

    /* Features Section */
    .feature-list {
        padding: 10px 10px 30px 10px;
    }

    .feature-item {
        text-align: center;
        margin-bottom: 28px;
    }

    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 6px;
    }

    .feature-desc {
        font-size: 13px;
        color: #665C55;
        line-height: 1.5;
    }

    /* Copy Block */
    .copy-block {
        text-align: center;
        padding: 20px 10px 30px 10px;
    }

    .copy-heading {
        font-family: 'Playfair Display', serif;
        font-size: 26px;
        line-height: 1.25;
        color: #1A1A1A;
        margin-bottom: 16px;
    }

    .copy-text {
        font-size: 13px;
        line-height: 1.6;
        color: #5C524B;
    }

    .footer-note {
        text-align: center;
        font-size: 11px;
        color: #8C7F77;
        margin-top: 25px;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1. Top Bar
st.markdown(
    '<div class="top-header">CHAYA <span>JEWELLERY</span></div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# 2. Hero Image Section
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

# 3. Main Title Section
st.markdown(
    """
    <div class="sub-tag">— ZURICH · CERTIFIED DIAMONDS —</div>
    <div class="hero-heading">
        Design the <em>Perfect</em><br>Engagement Ring
    </div>
    """,
    unsafe_allow_html=True,
)

# 4. CTA Block Directly Accessible (Above scroll area on mobile viewports)
st.markdown(
    """
    <div class="cta-container">
        <div class="cta-title-tag">START THE CONVERSATION</div>
        <div class="cta-main-heading">Three ways to reach us</div>
        <div class="cta-subtext">Pick whichever feels right — a quick chat, a browse, or a booked call.</div>
        
        <!-- Button 1: WhatsApp -->
        <a href="https://wa.me/41790000000" target="_blank" class="action-btn btn-whatsapp">
            <div class="btn-content">
                <div class="btn-icon">💬</div>
                <div>
                    <div class="btn-text-main">Chat with us on WhatsApp</div>
                    <div class="btn-text-sub">Usually replies within the hour</div>
                </div>
            </div>
            <span class="arrow-icon">→</span>
        </a>

        <!-- Button 2: Website -->
        <a href="https://chaya-jewellery.ch" target="_blank" class="action-btn btn-outline">
            <div class="btn-content">
                <div class="btn-icon">🌐</div>
                <div>
                    <div class="btn-text-main">Visit chaya-jewellery.ch</div>
                    <div class="btn-text-sub">See the full collection & craftsmanship</div>
                </div>
            </div>
            <span class="arrow-icon">→</span>
        </a>

        <!-- Button 3: Calendly Call -->
        <a href="https://calendly.com" target="_blank" class="action-btn btn-outline">
            <div class="btn-content">
                <div class="btn-icon">📅</div>
                <div>
                    <div class="btn-text-main">Book a 30-minute consultation</div>
                    <div class="btn-text-sub">Pick a slot on our Calendly</div>
                </div>
            </div>
            <span class="arrow-icon">→</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. Value Proposition & Guarantee Section
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

# 6. Feature List
st.markdown(
    """
    <div class="feature-list">
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

# 7. Additional Editorial Copy Block
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
