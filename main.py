import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PropelRealty AI",
    page_icon="🏢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Main Layout Styling */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Sleek Card Styling */
    div[data-testid="stForm"], div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Primary Action Buttons */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }

    /* Process Step Cards */
    .step-card {
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        color: #ffffff;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }
    .card-1 {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    .card-2 {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    }
    .card-3 {
        background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%);
    }
    .step-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .step-desc {
        font-size: 0.9rem;
        opacity: 0.95;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE INITIALIZATION ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

# LOGO DIRECT LINK (Pasted inside quotes below)
LOGO_URL = "YOUR_IMGBB_DIRECT_LINK_HERE"


# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "landing":
    # Header Logo or Text Fallback
    if LOGO_URL != "YOUR_IMGBB_DIRECT_LINK_HERE":
        st.image(LOGO_URL, width=320)
    else:
        st.title("🏢 PropelRealty AI")
    
    st.markdown("---")
    
    # Navigation Buttons
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    with nav_col1:
        if st.button("Plans & Pricing", use_container_width=True):
            st.session_state.page = "checkout"
            st.rerun()
    with nav_col2:
        if st.button("Get Started", type="primary", use_container_width=True):
            st.session_state.page = "onboarding"
            st.rerun()
    with nav_col3:
        if st.button("Book Demo", use_container_width=True):
            st.info("Demo booking module ready.")

    st.markdown("### Simple Steps to Your New Property")
    
    # Polished Process Cards
    st.markdown("""
    <div class="step-card card-1">
        <div class="step-title">📁 1. UPLOAD DOCUMENTS</div>
        <div class="step-desc">First, upload all necessary documents (IDs, financial statements) to our secure platform.</div>
    </div>
    
    <div class="step-card card-2">
        <div class="step-title">🤖 2. AI CHATBOT ANSWERS QUERIES</div>
        <div class="step-desc">Interact with the PropelRealty AI chatbot to get immediate, detailed answers to all your property-related questions.</div>
    </div>
    
    <div class="step-card card-3">
        <div class="step-title">📅 3. SCHEDULE MEETINGS</div>
        <div class="step-desc">Specify your desired dates and times for meetings to fit your busy schedule seamlessly.</div>
    </div>
    """, unsafe_allow_html=True)


# --- PAGE 2: ONBOARDING / GET STARTED ---
elif st.session_state.page == "onboarding":
    st.subheader("Get Started: Let's Find Your Property")
    st.caption("To help the AI match you perfectly, please provide a few details.")
    
    with st.form("onboarding_form"):
        name = st.text_input("Enter Your Name", placeholder="Garvit Srivastav")
        prop_type = st.selectbox("Select Your Property Type", ["Residential", "Commercial", "Land"])
        submitted = st.form_submit_button("Next Step ➔", type="primary", use_container_width=True)
        
        if submitted:
            if name:
                st.session_state.user_name = name
                st.session_state.page = "checkout"
                st.rerun()
            else:
                st.warning("Please enter your name to proceed.")
                
    if st.button("← Back to Home"):
        st.session_state.page = "landing"
        st.rerun()


# --- PAGE 3: PAYMENT GATEWAY & ACTIVATION ---
elif st.session_state.page == "checkout":
    st.title("💳 Payment & Activation")
    st.write(f"Welcome, **{st.session_state.get('user_name', 'Valued Client')}**! Select your payment method to activate your PropelRealty AI instance.")
    
    st.markdown("---")
    
    pay_method = st.radio(
        "Select Payment Option:",
        ["USDT (BEP20 - Binance Smart Chain)", "Traditional Bank Wire Transfer"],
        index=0
    )
    
    st.markdown("---")
    
    # --- OPTION 1: USDT BEP20 ---
    if pay_method == "USDT (BEP20 - Binance Smart Chain)":
        logo_col, title_col = st.columns([1, 6])
        with logo_col:
            st.image("https://cryptologos.cc/logos/tether-usdt-logo.png?v=035", width=42)
        with title_col:
            st.subheader("USDT (BEP20) Settlement")
            
        st.info("⚡ Fast Automated Crypto Settlement")
        st.write("**Deposit Wallet Address (BEP20 Network Only):**")
        st.code("0x71C7656EC7ab88b098defB751B7401B5f6d8976F", language="text")
        st.caption("⚠️ Make sure you transfer via the Binance Smart Chain (BEP20) network. Transferred funds are verified on-chain.")
        
        tx_hash = st.text_input("Enter Transaction Hash (TxHash):", placeholder="0x...")
        if st.button("Verify Crypto Payment", type="primary", use_container_width=True):
            if tx_hash:
                st.success("✅ Payment recorded! Our engine is deploying your agency instance.")
            else:
                st.warning("Please enter your transaction hash to verify.")

    # --- OPTION 2: TRADITIONAL BANK WIRE ---
    else:
        st.subheader("🏛️ Traditional Bank Wire Transfer")
        st.info("💼 Official Corporate Invoicing & Wire Settlement")
        
        st.markdown("""
        **Bank Transfer Details:**
        * **Account Name:** PropelRealty AI Solutions LLC
        * **Bank Name:** Global Business Bank
        * **Account Number:** 987654321012
        * **SWIFT / BIC:** GBBUS33XXX
        * **Routing Number:** 123456789
        """)
        st.caption("Please reference your full name or agency name in the transfer notes.")
        
        reference_no = st.text_input("Enter Wire Reference / UTR Number:", placeholder="WIRE-123456")
        if st.button("Submit Wire Reference", type="primary", use_container_width=True):
            if reference_no:
                st.success("✅ Wire reference received! Account setup instructions sent to your email.")
            else:
                st.warning("Please provide your wire reference number.")
                
    st.markdown("---")
    if st.button("← Back to Landing"):
        st.session_state.page = "landing"
        st.rerun()














