import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PropelRealty AI", page_icon="🏢", layout="centered")

# 2. Clean Mobile Typography Adjustments
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Session State Initialization
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "landing":
    st.title("🏢 PropelRealty AI")
    st.markdown("---")
    st.header("Welcome to PropelRealty AI.")
    st.subheader("Your Smart Real Estate Assistant. Let AI guide you to the perfect property.")
    
    st.write("")
    if st.button("Get Started ➔", type="primary", use_container_width=True):
        st.session_state.page = "how_it_works"
        st.rerun()
    st.caption("Discover your next home with ease.")

# --- PAGE 2: HOW IT WORKS ---
elif st.session_state.page == "how_it_works":
    # Top Navigation Bar
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("HOME", use_container_width=True):
        st.session_state.page = "how_it_works"
        st.rerun()
    if col2.button("ABOUT US", use_container_width=True):
        st.session_state.page = "about_us"
        st.rerun()
    if col3.button("PLANS", use_container_width=True):
        st.session_state.page = "plans"
        st.rerun()
    if col4.button("BOOK DEMO", use_container_width=True):
        st.session_state.page = "book_demo"
        st.rerun()
        
    st.markdown("---")
    st.header("Simple Steps to Your New Property")
    
    st.markdown("📄 **1. UPLOAD DOCUMENTS**")
    st.write("First, upload all necessary documents (IDs, financial statements) to our secure platform.")
    
    st.markdown("🤖 **2. AI CHATBOT ANSWERS QUERIES**")
    st.write("Interact with the PropelRealty AI chatbot to get immediate, detailed answers to all your property-related questions.")
    
    st.markdown("📅 **3. SCHEDULE MEETINGS**")
    st.write("Specify your desired dates and times for meetings to fit your busy schedule.")
    
    st.markdown("✅ **4. CONFIRMATION**")
    st.write("Your designated advisor will confirm the meeting based on your availability.")
    
    st.markdown("🏡 **5. PROPERTY VIEWING**")
    st.write("Meet your advisor at your desired time for a seamless property viewing experience.")
    
    st.write("")
    if st.button("GET STARTED ➔", type="primary", use_container_width=True):
        st.session_state.page = "form"
        st.rerun()

# --- PAGE 3: AGENCY SETUP FORM ---
elif st.session_state.page == "form":
    st.header("Setup Your Agency Profile")
    
    with st.form("agency_form"):
        agency_name = st.text_input("Agency Name", placeholder="Enter Agency Name")
        agency_email = st.text_input("Agency Email Address", placeholder="name@agency.com")
        phone = st.text_input("Primary Phone Number", placeholder="+91 98765 43210 (include country code)")
        address = st.text_input("Agency Address", placeholder="Street Address, City")
        agency_type = st.selectbox("Agency Type", ["Residential", "Commercial", "Luxury", "Other"])
        
        submitted = st.form_submit_button("COMPLETE SETUP ➔", type="primary", use_container_width=True)
        if submitted:
            if agency_name and agency_email:
                st.session_state.page = "plans"
                st.rerun()
            else:
                st.error("Please fill in at least the Agency Name and Email.")

# --- PAGE 4: SELECT AGENCY PLAN ---
elif st.session_state.page == "plans":
    st.header("Select Your Agency Plan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ONE-TIME ACCESS")
        st.title("$1000")
        st.caption("One-time fee")
        st.markdown("""
        * ✏️ Agency Profile Creation & Branding
        * 📄 Initial Document Repository (up to 50 files)
        * 🤖 Limited AI Chatbot Queries (1000/mo)
        * 👤 Single Administrator Access
        * 📧 Email Support
        """)
        if st.button("SELECT ONE-TIME", key="btn_one_time", use_container_width=True):
            st.session_state.selected_plan = "One-Time Access ($1000)"
            st.session_state.page = "checkout"
            st.rerun()
            
    with col2:
        st.subheader("PREMIUM RETAINER ⭐")
        st.title("$1000 + $200/mo")
        st.caption("Upfront + Monthly Retainer")
        st.markdown("""
        * ✏️ Agency Setup Creation & Branding
        * 📄 **Unlimited** Document Repository
        * 🤖 **Unlimited** AI Chatbot Queries & Custom Training
        * 👥 Multiple Team Member Access
        * 📊 Advanced Performance Dashboard & Reporting
        * 🎧 Priority Email & Chat Support
        * 📅 Automated Client Meeting Scheduling & Reminders
        * 👤 Dedicated Account Manager
        """)
        if st.button("SELECT RETAINER", key="btn_retainer", type="primary", use_container_width=True):
            st.session_state.selected_plan = "Premium Retainer ($1000 + $200/mo)"
            st.session_state.page = "checkout"
            st.rerun()

    st.info("Retainer features are exclusive to the monthly plan and enhance team productivity and client engagement.")

# --- PAGE 5: PAYMENT GATEWAY ---
elif st.session_state.page == "checkout":
    st.header("💳 Payment & Activation")
    st.write(f"Selected Plan: **{st.session_state.get('selected_plan', 'Premium Retainer')}**")
    st.markdown("---")
    
    pay_method = st.radio("Choose Payment Method:", ["USDT (BEP20 - Binance Smart Chain)", "Standard Bank Wire Transfer"])
    
    if pay_method == "USDT (BEP20 - Binance Smart Chain)":
        st.info("⚡ Fast Automated Crypto Settlement")
        st.write("Deposit Wallet Address (BEP20):")
        st.code("0x71C7656EC7ab88b098defB751B7401B5f6d8976F", language="text")
        st.caption("Send exact amount in USDT via BEP20 network. Enter your transaction hash below for verification.")
        tx_hash = st.text_input("Transaction Hash (TxHash)")
        if st.button("Verify Crypto Payment", type="primary", use_container_width=True):
            if tx_hash:
                st.success("Payment recorded! Our team is configuring your PropelRealty AI instance.")
            else:
                st.warning("Please enter your transaction hash.")
            
    else:
        st.info("🏦 Direct Corporate Bank Transfer")
        st.markdown("""
        * **Bank Name:** Global Real Estate Clearing Bank
        * **Account Name:** PropelRealty AI LLC
        * **IBAN / Account:** US89 3704 0044 0532 0130 00
        * **SWIFT/BIC:** GRELUS33
        """)
        reference = st.text_input("Enter Wire Reference / UTR Number")
        if st.button("Submit Wire Confirmation", type="primary", use_container_width=True):
            if reference:
                st.success("Wire reference recorded. Access details will be emailed upon clearing.")
            else:
                st.warning("Please enter your wire transfer reference number.")

# --- PAGE 6: ABOUT US ---
elif st.session_state.page == "about_us":
    st.header("About PropelRealty AI")
    st.markdown("""
    **PropelRealty AI** is built specifically for modern real estate agencies, brokerages, and advisors. 
    
    Our platform automates client intake, securely parses complex property documentation, and provides 24/7 intelligent AI chatbot assistance to ensure no lead or query goes unanswered.
    
    * 🔒 **Enterprise-Grade Security:** 256-bit document encryption.
    * ⚡ **Ultra-Fast AI Engine:** Instant response generation for client inquiries.
    * 📅 **Seamless Scheduling:** Integrated calendar booking and client follow-ups.
    """)
    if st.button("⬅ Back to Home", type="primary"):
        st.session_state.page = "how_it_works"
        st.rerun()

# --- PAGE 7: BOOK OUR DEMO ---
elif st.session_state.page == "book_demo":
    st.header("Book a Live 1-on-1 Demo")
    st.write("Schedule a direct walk-through with our product specialists to see PropelRealty AI in action.")
    
    with st.form("demo_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Work Email")
        preferred_date = st.date_input("Preferred Demo Date")
        notes = st.text_area("Specific Requirements / Team Size")
        
        if st.form_submit_button("BOOK DEMO NOW ➔", type="primary", use_container_width=True):
            if name and email:
                st.success("Demo request submitted! We will send a calendar invitation shortly.")
            else:
                st.error("Please enter your name and email.")
                
    if st.button("⬅ Back to Home"):
        st.session_state.page = "how_it_works"
        st.rerun()













