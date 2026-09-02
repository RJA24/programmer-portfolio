# MUST BE FIRST
import streamlit as st
import plotly.express as px
import pandas as pd
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="Ron Jay C. Ayup | Developer Portfolio", layout="wide", page_icon=":material/code:")

# --- DATA & ASSETS ---
# Upgraded radar chart focusing on strict technical competencies
df = pd.DataFrame(dict(
    r=[90, 85, 80, 85, 75, 80],
    theta=['Data Engineering & ETL', 'Full-Stack Development', 'Geospatial Mapping', 'Database Admin (SQL/NoSQL)', 'Mobile App Dev', 'UI/UX & Frontend'],
    Details=[
        'Building automated parsers and data pipelines with Pandas',
        'Developing end-to-end web applications using Streamlit & Python',
        'Plotly choropleth maps, custom GeoJSON, and coordinate manipulation',
        'Managing Supabase (PostgreSQL) and live Google Sheets APIs',
        'Cross-platform mobile development using React Native & Expo',
        'Designing intuitive interfaces, AgGrid tables, and digital assets'
    ]
))

fig = px.line_polar(
    df, 
    r='r', 
    theta='theta', 
    line_close=True,
    hover_data={'r': False, 'theta': False, 'Details': True}
)

fig.update_traces(
    fill='toself', 
    line_color='#0ea5e9', # Electric Blue
    fillcolor='rgba(14, 165, 233, 0.2)',
    mode='lines+markers', 
    marker=dict(size=8, color='#38bdf8', line=dict(color='white', width=1)),
    hovertemplate='<b>%{theta}</b><br><br>%{customdata[0]}<extra></extra>'
)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#f8fafc",
    polar=dict(
        bgcolor='rgba(0,0,0,0)', 
        radialaxis=dict(visible=False),
        angularaxis=dict(linewidth=1, linecolor='rgba(255,255,255,0.1)')
    ),
    margin=dict(l=40, r=40, t=20, b=20),
    height=350,
    hoverlabel=dict(
        bgcolor="#0f172a",
        font_size=14,
        font_family="sans-serif",
        bordercolor="#0ea5e9"
    )
)

# --- RESUME SETUP ---
try:
    with open("resume.pdf", "rb") as pdf_file:
        resume_bytes = pdf_file.read()
except FileNotFoundError:
    resume_bytes = b"Please upload your resume.pdf to the repository to enable this download."

# --- MODERN DEVELOPER CSS ---
st.markdown("""
    <style>
    /* Dark Slate Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        background-attachment: fixed;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] { background-color: rgba(15, 23, 42, 0.95); border-right: 1px solid rgba(255,255,255,0.05); }
    
    /* ---------------------------------------------------- */
    /* SLEEK SIDEBAR NAVIGATION */
    /* ---------------------------------------------------- */
    section[data-testid="stSidebar"] .stButton > button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 8px 12px !important;
        border-radius: 6px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] .stButton > button div[data-testid="stMarkdownContainer"] {
        display: flex !important;
        width: 100% !important;
        justify-content: flex-start !important;
    }
    section[data-testid="stSidebar"] .stButton > button p {
        font-size: 15px !important;
        font-weight: 500 !important;
        color: #cbd5e1 !important;
        margin: 0 !important;
        text-align: left !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(14, 165, 233, 0.1) !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover p {
        color: #38bdf8 !important;
    }
    
    /* Typing Animation for Subtitle */
    .typing-text {
        overflow: hidden;
        border-right: 3px solid #0ea5e9;
        white-space: nowrap;
        animation: typing 3.5s steps(45, end) forwards, blink 0.8s step-end infinite;
        font-size: 1.4rem;
        font-weight: 600;
        color: #38bdf8;
        margin-top: -15px;
        margin-bottom: 20px;
        max-width: fit-content;
    }
    
    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { from, to { border-color: transparent; } 50% { border-color: #0ea5e9; } }
    
    /* Sleek Glassmorphism Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(30, 41, 59, 0.3) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Headers & Text */
    h1 { color: #f8fafc !important; font-weight: 800 !important; letter-spacing: -0.5px; }
    h2, h3 { color: #f8fafc !important; font-weight: 700; }
    h4 { color: #cbd5e1 !important; font-size: 1.1rem !important; margin-bottom: 5px !important;}
    p, li { color: #94a3b8; line-height: 1.7; font-size: 1.05rem;}
    
    /* Standard Buttons */
    .stButton>button[kind="primary"], [data-testid="stDownloadButton"] button { 
        background-color: #0ea5e9 !important;
        color: white !important; 
        border-radius: 6px !important; 
        border: none !important;
        transition: 0.2s ease !important;
        font-weight: 600 !important;
    }
    .stButton>button[kind="primary"]:hover, [data-testid="stDownloadButton"] button:hover {
        background-color: #0284c7 !important;
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3) !important;
    }

    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    
    /* Profile Image Treatment */
    .profile-img {
        background-color: #ffffff;
        border-radius: 50%;
        border: 3px solid #0ea5e9;
        box-shadow: 0 0 25px rgba(14, 165, 233, 0.3);
        width: 260px;
        height: 260px;
        object-fit: cover;
        margin: 0 auto;
        display: block;
    }

    /* Tech Badges (Pills) */
    .tech-pill {
        display: inline-block;
        background: rgba(14, 165, 233, 0.1);
        border: 1px solid rgba(14, 165, 233, 0.3);
        color: #38bdf8;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0 5px 8px 0;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### :material/dashboard: Navigation")
    
    if st.button("Home / About Me", icon=":material/person:", use_container_width=True): 
        st.session_state.page = "home"
    if st.button("Projects & Apps", icon=":material/terminal:", use_container_width=True): 
        st.session_state.page = "projects"
    if st.button("Professional Experience", icon=":material/work_history:", use_container_width=True): 
        st.session_state.page = "experience"
        
    st.markdown("---")
    st.markdown("### :material/link: Connect")
    st.markdown(":material/mail: [Email](mailto:ronjay.1204@gmail.com)")
    st.markdown(":material/code: [GitHub](https://github.com/RJA24)")
    st.markdown(":material/work: [LinkedIn](https://www.linkedin.com/in/ron-jay-ayup-a1824b3b3)")

if 'page' not in st.session_state:
    st.session_state.page = "home"

# ==========================================
# PAGE 1: HOME (ABOUT ME)
# ==========================================
if st.session_state.page == "home":
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.markdown(f"""
            <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/Profile.png?raw=true" class="profile-img">
            """, unsafe_allow_html=True)

    with col2:
        st.title("Ron Jay C. Ayup")
        st.markdown('<div class="typing-text">Full-Stack Programmer & Data Analyst</div>', unsafe_allow_html=True)
        
        st.write("I am a highly adaptable software developer and data analyst specializing in building secure, end-to-end data pipelines and scalable web applications. With a robust background in epidemiology and public health data management, I transform fragmented, high-volume metrics into automated, real-time command centers.")
        
        st.write("My expertise lies in architecting complex Streamlit dashboards, engineering automated ETL (Extract, Transform, Load) parsers, managing relational databases (PostgreSQL/Supabase), and deploying dynamic geospatial visualizations. I am actively seeking roles where I can leverage my technical precision to streamline operations, enforce data integrity, and build high-impact digital tools.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button("Download Resume (PDF)", icon=":material/download:", data=resume_bytes, file_name="Ron_Jay_Ayup_Resume.pdf", mime="application/pdf", type="primary")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. CORE COMPETENCIES & TECH STACK
    c1, c2 = st.columns([1, 1])
    with c1:
        with st.container(border=True):
            st.subheader(":material/radar: Core Competencies")
            st.plotly_chart(fig, use_container_width=True)

        with st.container(border=True):
            st.subheader(":material/contact_mail: Contact Me")
            
            with st.form("contact_form", clear_on_submit=True):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Your Message", height=100)
                
                submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
                
                if submitted:
                    if not name or not email or not message:
                        st.warning("⚠️ Please fill out all fields before sending.")
                    else:
                        with st.spinner("Transmitting to backend..."):
                            try:
                                # Format the email
                                email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                                msg = MIMEText(email_body)
                                msg['Subject'] = f"New Portfolio Message from {name}"
                                msg['From'] = st.secrets["EMAIL_USER"]
                                msg['To'] = "ronjay.1204@gmail.com"
                                
                                # Connect to Gmail's secure SMTP server and send
                                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                                    server.login(st.secrets["EMAIL_USER"], st.secrets["EMAIL_PASS"])
                                    server.sendmail(st.secrets["EMAIL_USER"], "ronjay.1204@gmail.com", msg.as_string())
                                    
                                st.success("✅ Message successfully sent! I will get back to you shortly.")
                            except Exception as e:
                                st.error(f"🚨 Server error: {e}")

    with c2:
        with st.container(border=True):
            st.subheader(":material/memory: Technical Stack")
            
            st.markdown("#### Languages & Frameworks")
            st.markdown("""
            <div style="margin-bottom: 15px;">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Streamlit</span>
                <span class="tech-pill">React Native</span>
                <span class="tech-pill">Expo</span>
                <span class="tech-pill">SQL</span>
                <span class="tech-pill">JavaScript</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Data Engineering & Analytics")
            st.markdown("""
            <div style="margin-bottom: 15px;">
                <span class="tech-pill">Pandas</span>
                <span class="tech-pill">Plotly Express</span>
                <span class="tech-pill">OpenCV</span>
                <span class="tech-pill">MediaPipe</span>
                <span class="tech-pill">ETL Pipelines</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Databases & Infrastructure")
            st.markdown("""
            <div style="margin-bottom: 15px;">
                <span class="tech-pill">PostgreSQL</span>
                <span class="tech-pill">Supabase</span>
                <span class="tech-pill">Google Sheets API</span>
                <span class="tech-pill">Git / GitHub</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Design & Multimedia")
            st.markdown("""
            <div>
                <span class="tech-pill">Canva</span>
                <span class="tech-pill">Figma</span>
                <span class="tech-pill">Premiere Pro</span>
                <span class="tech-pill">UI/UX Auditing</span>
            </div>
            """, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.subheader(":material/forum: Frequently Asked Questions")
            
            with st.expander("Working hours and timezone?"):
                st.write("I am based in the Philippines (GMT+8). I offer highly flexible working hours and can easily overlap with your team's local timezone to ensure seamless, real-time communication.")
                
            with st.expander("How do you handle data privacy and security?"):
                st.write("Coming from a background in provincial health data management, I adhere to strict data privacy protocols. I design my applications with role-based access control, secure hashed credentials, and encrypted database connections to ensure sensitive metrics are always protected.")
                
            with st.expander("Can you handle end-to-end development?"):
                st.write("Absolutely. I manage the entire software lifecycle—from architecting the initial database schema and building automated ETL pipelines, to designing the frontend UI and deploying the final web application.")

            with st.expander("Approach to AI-assisted coding?"):
                st.write("I leverage AI as a force multiplier to rapidly construct boilerplate logic, troubleshoot complex SQL queries, and optimize edge-case debugging. This allows me to work faster and focus my engineering efforts on secure, high-level system architecture.")

# ==========================================
# PAGE 2: PROJECTS & APPLICATIONS
# ==========================================
elif st.session_state.page == "projects":
    st.title(":material/code_blocks: Projects & Applications")
    st.write("An archive of my enterprise dashboards, standalone software engineering projects, and data visualization architecture.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Tier 1: Enterprise Data Systems")
    
    # --- PESU PORTAL ---
    with st.container(border=True):
        st.header("Abra PESU Surveillance Portal")
        st.markdown("<span class='tech-stack'>Python • Streamlit • Pandas • Plotly • Google Sheets API • Cryptography</span>", unsafe_allow_html=True)
        st.write("Engineered a secure epidemiological surveillance portal to monitor Dengue and Tuberculosis (DSTB, DRTB, MN, TPT, HIV) outbreaks across 27 municipalities. Features role-based access control with hashed credentials and an admin approval matrix. The system automatically computes Year-Over-Year (YOY) variance, generates dynamic clinical classifications, builds population pyramids, and utilizes predictive cross-tabulation algorithms for 'Clustering Barangay' detection. Integrated advanced Plotly choropleth maps with custom vector coordinate nudging to eliminate label collisions.")
        
    # --- SIA 2026 DASHBOARD ---
    with st.container(border=True):
        st.header("National Immunization Program: SIA 2026 Command Center")
        st.markdown("<span class='tech-stack'>Python • Streamlit • Supabase (PostgreSQL) • AgGrid • Plotly Express</span>", unsafe_allow_html=True)
        st.write("Developed a real-time provincial command center for the 2026 Measles-Rubella and Vitamin A vaccination campaign. Engineered a robust backend integration that bypasses Supabase pagination limits to securely upsert target databases. Features an automated discrepancy reconciliation engine comparing official 'VaccTrack' exports against live RHU submissions via AgGrid. The application generates dynamic daily tally sheets and supports ultra-high-resolution map exports specifically configured for official print layouts.")
        
    # --- FHSIS COMMAND CENTER ---
    with st.container(border=True):
        st.header("Abra FHSIS Command Center")
        st.markdown("<span class='tech-stack'>Python • Streamlit • Pandas • Plotly Express</span>", unsafe_allow_html=True)
        st.write("Architected a massive, modular reporting engine that automatically ingests, cleans, and visualizes Field Health Services Information System (FHSIS) data. Built an 'auto-healing' ETL pipeline that dynamically standardizes headers and bypasses broken DOH Excel templates with zero manual intervention. Includes complex linkage-to-care cascade funnels, CPR calculations, and automated data quality audits to flag statistical anomalies before database entry.")
        st.link_button("View FHSIS Dashboard", "https://abra-fhsis.streamlit.app/")
        
    # --- VACCINE INVENTORY ---
    with st.container(border=True):
        st.header("Vaccine Logistics & Inventory Matrix")
        st.markdown("<span class='tech-stack'>Python • Streamlit • Pandas • Google Cloud APIs</span>", unsafe_allow_html=True)
        st.write("Transformed complex, error-prone 2D spreadsheet matrices into a searchable, relational logistics database. Tracks cold chain stock limits, batch expiries, and alerts administrators to critical stockouts across the provincial network.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Tier 2: Software Engineering")
    
    # --- SOFTWARE PROJECTS ---
    c_sw1, c_sw2 = st.columns(2)
    with c_sw1:
        with st.container(border=True):
            st.header("Gesture Control Engine")
            st.markdown("<span class='tech-stack'>Python • OpenCV • MediaPipe • PyAutoGUI</span>", unsafe_allow_html=True)
            st.write("Compiled a standalone Python computer vision program featuring zero-latency hand tracking and facial detection to emulate complete mouse controls and secure user inputs via standard webcams.")
    with c_sw2:
        with st.container(border=True):
            st.header("Mobile Station Mapper")
            st.markdown("<span class='tech-stack'>React Native • Expo • Google Maps API</span>", unsafe_allow_html=True)
            st.write("Programmed a mobile iOS/Android application utilizing GPS mapping arrays to track routes, locate gasoline stations, and calculate real-time fuel parameters for motorcycle touring.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Tier 3: Frontend Design & Multimedia")
    
    with st.container(border=True):
        st.markdown("##### Vector Cartography & Public Health Layouts")
        st.write("Beyond code, I maintain a strong competency in UI/UX and graphic design. I conceptualize and design high-impact vector maps, executive PowerPoint decks, and large-scale print layouts (Tarpaulins) for official DRRM-H planning and DOH regional health events using Canva and Adobe Premiere Pro.")

# ==========================================
# PAGE 3: PROFESSIONAL EXPERIENCE
# ==========================================
elif st.session_state.page == "experience":
    st.title(":material/work_history: Professional Experience")
    st.write("A timeline of my professional roles, highlighting my transition from financial data operations to lead public health database engineering.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown('<div class="job-title">Data Controller III</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-company">Department of Health (DOH) CHD CAR - Provincial DOH Office Abra</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-date">2021 – Present</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Database Architecture & Aggregation:** Lead the consolidation, cleaning, and administration of massive public health datasets across 27 municipalities, tracking Covid-19, supplementary, and routine immunization programs.
        * **ETL & Automation:** Engineered automated reporting workflows using Python to replace highly manual Excel operations, drastically reducing reporting latency and eliminating data-entry redundancies.
        * **Data Integrity & Auditing:** Serve as the final technical gatekeeper for regional reporting, conducting rigorous data quality audits to enforce strict statistical accuracy and data privacy compliance.
        * **Systems Deployment:** Set the provincial standard for digital reporting by consistently achieving first-in-region submission metrics out of six provinces.
        """)

    with st.container(border=True):
        st.markdown('<div class="job-title">Junior Microfinance Officer</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-company">ASA Philippines Foundation, Inc.</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-date">2018 – 2021</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Financial Data Operations:** Oversaw the full accounting cycle, managing initial data collection, document processing, and the closing of strict financial ledgers.
        * **Risk & Portfolio Management:** Executed precise audits on client loan portfolios to minimize institutional risk and ensure compliance with microfinance regulations.
        * **Award Recognition:** Awarded *Employee of the Month*, *Best in Loan Portfolio*, and *Best in Recruitment* for maintaining flawless ledger accuracy and exceeding key performance indicators.
        """)
        
    with st.container(border=True):
        st.markdown('<div class="job-title">Stock Clerk</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-company">SM Supermarket Baguio</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-date">2018</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Logistics & Inventory Management:** Maintained digital and physical stock databases to ensure accurate tracking, proper stock rotation, and real-time inventory counts.
        """)

    with st.container(border=True):
        st.markdown('<div class="job-title">Bachelor of Science in Information Technology</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-company">Divine Word College of Bangued</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-date">2014 – 2018</div>', unsafe_allow_html=True)
        st.write("Graduated with a core focus on programming, database management, systems analysis, and network architecture.")