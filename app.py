import streamlit as st

st.set_page_config(
    page_title="CHAYA JEWELLERY",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling (Injected directly into head via st.html)
st.html(
    """
    <style>
    /* Hide Streamlit default interface elements */
    #MainMenu {display: none !important;}
    footer {display: none !important;}
    header {display: none !important;}
    .stAppHeader {display: none !important;}
    
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #F7F3EE !important;
        color: #2B2523 !important;
    }

    .stApp {
        background-color: #F7F3EE !important;
        max-width: 450px !important;
        margin: 0 auto !important;
    }

    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    /* Sticky Navigation Header */
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

    .content-wrapper {
        padding: 20px 20px 40px 20px;
    }

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

    /* Dark Call To Action Box */
    .cta-container {
        background-color: #26211E;
        border-radius: 20px;
        padding: 26px 18px;
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
        margin-bottom: 22px;
        padding: 0 5px;
    }

    /* Working Clickable Buttons */
    a.custom-btn {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        padding: 14px 16px !important;
        border-radius: 14px !important;
        text-decoration: none !important;
        box-sizing: border-box !important;
        margin-bottom: 12px !important;
        cursor: pointer !important;
        pointer-events: auto !important;
        transition: transform 0.15s ease, opacity 0.15s ease !important;
    }

    a.custom-btn:hover {
        opacity: 0.92 !important;
        transform: translateY(-1px) !important;
    }

    .btn-whatsapp {
        background-color: #D3A89B !important;
        color: #1A1A1A !important;
    }

    .btn-outline {
        background-color: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: #FFFFFF !important;
    }

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

    /* Images and Cards */
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
    """
)

# Render Full Single Page Mobile HTML
st.html(
    """
    <div class="top-header">CHAYA <span>JEWELLERY</span></div>

    <div class="content-wrapper">
        <!-- 1. Heading directly at top -->
        <div class="sub-tag">— ZURICH · CERTIFIED DIAMONDS —</div>
        <div class="hero-heading">
            Design the <em>Perfect</em><br>Engagement Ring
        </div>

        <!-- 2. Interactive Working Buttons Box -->
        <div class="cta-container">
            <div class="cta-title-tag">START THE CONVERSATION</div>
            <div class="cta-main-heading">Three ways to reach us</div>
            <div class="cta-subtext">Pick whichever feels right — a quick chat, a browse, or a booked call.</div>
            
            <!-- Button 1 -->
            <a href="https://wa.me/41790000000" target="_blank" class="custom-btn btn-whatsapp">
                <div class="btn-inner">
                    <div class="btn-circle-icon btn-circle-dark">💬</div>
                    <div>
                        <div class="btn-title">Chat with us on WhatsApp</div>
                        <div class="btn-sub">Usually replies within the hour</div>
                    </div>
                </div>
                <span class="btn-arrow">→</span>
            </a>

            <!-- Button 2 -->
            <a href="https://chaya-jewellery.ch" target="_blank" class="custom-btn btn-outline">
                <div class="btn-inner">
                    <div class="btn-circle-icon btn-circle-light">🌐</div>
                    <div>
                        <div class="btn-title">Visit chaya-jewellery.ch</div>
                        <div class="btn-sub">See the full collection & craftsmanship</div>
                    </div>
                </div>
                <span class="btn-arrow">→</span>
            </a>

            <!-- Button 3 -->
            <a href="https://calendly.com" target="_blank" class="custom-btn btn-outline">
                <div class="btn-inner">
                    <div class="btn-circle-icon btn-circle-light">📅</div>
                    <div>
                        <div class="btn-title">Book a 30-minute consultation</div>
                        <div class="btn-sub">Pick a slot on our Calendly</div>
                    </div>
                </div>
                <span class="btn-arrow">→</span>
            </a>
        </div>

        <!-- 3. Ring Showcase Image -->
        <div class="hero-card">
            <img src="https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&q=80&w=800" alt="Ring in Box" />
            <div class="badge">
                <span class="badge-dot"></span> Ethically sourced, since 1976
            </div>
        </div>

        <!-- 4. Guarantee Section -->
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

        <!-- 5. Value Points -->
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

        <!-- 6. Bottom Story Block -->
        <div class="copy-block">
            <div class="sub-tag">WORN TODAY, TREASURED TOMORROW</div>
            <div class="copy-heading">One ring. One decision that has to be right.</div>
            <div class="copy-text">
                Tell us the stone, the budget, and the date you're working toward. We'll shortlist certified diamonds, size the setting, and have it ready in time — no back-and-forth with three different jewellers.
            </div>
        </div>

        <!-- 7. Footer Tagline -->
        <div class="footer-note">
            Certified by GIA, IGI & HRD · Master goldsmiths since 1976 · Zurich, Switzerland
        </div>
    </div>
    """
)
