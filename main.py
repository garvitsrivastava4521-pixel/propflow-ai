import streamlit as st

# Set page configuration
st.set_page_config(page_title="EstateMind AI", page_icon="🏢", layout="centered")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "landing":
    st.title("🏢 EstateMind AI")
    st.markdown("---")
    st.header("Welcome to EstateMind AI.")
    st.subheader("Your Smart Real Estate Assistant. Let AI guide you to the perfect property.")
    
    st.write("") # Spacer
    if st.button("Get Started ➔", type="primary", use_container_width=True):
        st.session_state.page = "how_it_works"
        st.rerun()
    st.caption("Discover your next home with ease.")

# --- PAGE 2: HOW IT WORKS ---
elif st.session_state.page == "how_it_works":
    # Top Navigation Bar
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("**HOME**")
    col2.markdown("ABOUT US")
    col3.markdown("PLANS")
    col4.markdown("BOOK OUR DEMO")
    st.markdown("---")
    
    st.header("Simple Steps to Your New Property")
    
    st.markdown("📄 **1. UPLOAD DOCUMENTS**")
    st.write("First, upload all necessary documents (IDs, financial statements) to our secure platform.")
    
    st.markdown("🤖 **2. AI CHATBOT ANSWERS QUERIES**")
    st.write("Interact with the EstateMind AI chatbot to get immediate, detailed answers to all your property-related questions.")
    
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
        phone = st.text_input("Primary Phone Number", placeholder="+1 (555) 000-0000")
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
            st.success("Plan Selected! Proceeding to payment setup...")
            
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
            st.success("Retainer Selected! Proceeding to payment setup...")

    st.info("Retainer features are exclusive to the monthly plan and enhance team productivity and client engagement.")













