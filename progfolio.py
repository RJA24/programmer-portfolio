# MUST BE FIRST
import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Space Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="🚀")

# --- DATA & ASSETS ---
df = pd.DataFrame(dict(
    r=[90, 85, 80, 75, 85, 85, 85],
    theta=['Python (AI-Assisted)','Data Tracking','Video Editing','Canva Design','NIP Automation', 'IT & Admin Support', 'QA & Product Strategy'],
    Details=[
        'Building Streamlit apps & automating workflows via AI',
        'Real-time dashboards & advanced Google Sheets auditing',
        'Premiere Pro & CapCut for YouTube, TikTok, & Reels',
        'High-impact visual assets, mapping, & event collateral',
        'Streamlining public health reporting & data systems',
        'Hardware troubleshooting, presentation design, & formatting',
        'End-to-end app testing, edge-case debugging, & UI/UX auditing'
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
    line_color='#4cc9f0', 
    fillcolor='rgba(76, 201, 240, 0.3)',
    mode='lines+markers', 
    marker=dict(size=10, color='#BC13FE', line=dict(color='white', width=2)),
    hovertemplate='<b>%{theta}</b><br><br>%{customdata[0]}<extra></extra>'
)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="white",
    polar=dict(
        bgcolor='rgba(0,0,0,0)', 
        radialaxis=dict(visible=False),
        angularaxis=dict(linewidth=1, linecolor='rgba(255,255,255,0.2)')
    ),
    margin=dict(l=40, r=40, t=20, b=20),
    height=350,
    hoverlabel=dict(
        bgcolor="#16213e",
        font_size=14,
        font_family="sans-serif",
        bordercolor="#BC13FE"
    )
)

# --- RESUME SETUP ---
try:
    with open("resume.pdf", "rb") as pdf_file:
        resume_bytes = pdf_file.read()
except FileNotFoundError:
    resume_bytes = b"Please upload your resume.pdf to the repository to enable this download."

# --- COSMIC CSS ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0D0221 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    [data-testid="stSidebar"] { background-color: rgba(26, 26, 46, 0.8); }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .floating-img { animation: float 4s ease-in-out infinite; }
    
    .typing-text {
        overflow: hidden;
        border-right: 3px solid #BC13FE;
        white-space: nowrap;
        animation: typing 3.5s steps(45, end) forwards, blink 0.8s step-end infinite;
        font-size: 1.7rem;
        font-weight: bold;
        color: #4cc9f0;
        margin-top: -10px;
        margin-bottom: 15px;
        max-width: fit-content;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink {
        from, to { border-color: transparent; }
        50% { border-color: #BC13FE; }
    }
    
    /* UNIVERSAL DARK GLASS EFFECT FOR ALL CONTAINERS */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(0, 0, 0, 0.4) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        padding: 20px !important;
    }
    
    /* FAQ EXPANDER & TABS STYLING */
    [data-testid="stExpander"] {
        background: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(76, 201, 240, 0.3) !important;
        border-radius: 10px !important;
    }
    [data-testid="stExpander"] summary {
        color: #4cc9f0 !important;
        font-weight: bold;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(188, 19, 254, 0.2);
        border-bottom: 2px solid #BC13FE;
        color: #4cc9f0 !important;
    }
    
    /* RADAR SPIN ANIMATION */
    @keyframes radar-spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* ENSURE CHART SITS ON TOP OF BEAM */
    [data-testid="stPlotlyChart"] {
        position: relative;
        z-index: 10;
        background: transparent !important;
    }
    
    h1, h2, h3 { color: #4cc9f0 !important; text-shadow: 0 0 15px rgba(76, 201, 240, 0.6); }
    
    .stButton>button, [data-testid="stDownloadButton"] button { 
        background: linear-gradient(45deg, #7209b7, #3f37c9); 
        color: white; 
        border-radius: 50px; 
        border: none;
        padding: 10px 20px;
        transition: 0.3s ease;
    }
    .stButton>button:hover, [data-testid="stDownloadButton"] button:hover {
        box-shadow: 0 0 20px rgba(114, 9, 183, 0.7);
        color: white;
    }

    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    
    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 5px;
        transition: 0.3s;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        background: rgba(76, 201, 240, 0.2);
    }
    
    .project-list {
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .job-title {
        color: #BC13FE !important;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .job-date {
        color: #a9d6e5;
        font-style: italic;
        margin-bottom: 15px;
    }
    
    .quote-box {
        border-left: 4px solid #BC13FE;
        padding-left: 15px;
        margin-top: 10px;
        margin-bottom: 10px;
        font-style: italic;
        color: #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2026/2026462.png", width=80)
    st.markdown("### 📡 Mission Control")
    
    page = st.radio("Select Sector:", ["🏠 Basecamp (Home)", "🛸 Mission Logs (Projects)", "🧑‍🚀 Tour of Duty (Experience)"])
    
    st.markdown("---")
    st.markdown("### 🔗 Comm Links")
    st.markdown("📫 [Email](mailto:ronjay.1204@gmail.com)")
    st.markdown("🐙 [GitHub](https://github.com/RJA24)")
    st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/ron-jay-ayup-a1824b3b3)")
    st.markdown("▶️ [YouTube](https://www.youtube.com/@JangTVyt)")
    st.markdown("🎵 [TikTok](https://www.tiktok.com/@jangtv_)")

# ==========================================
# PAGE 1: HOME (BASECAMP)
# ==========================================
if page == "🏠 Basecamp (Home)":
    
    # 1. PROFILE & INTRO
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/Profile.png?raw=true" 
                class="floating-img"
                style="border-radius: 50%; border: 4px solid #4cc9f0; width: 260px; height: 260px; object-fit: cover; box-shadow: 0 0 30px rgba(76, 201, 240, 0.5);">
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p style="color:#BC13FE; letter-spacing:3px; font-weight:bold; margin-bottom:0px;">A MESSAGE FROM EARTH</p>', unsafe_allow_html=True)
        st.title("Ron Jay C. Ayup")
        
        st.markdown('<div class="typing-text">🌌 Tech-Forward Virtual Assistant & Data Analyst</div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Mission Overview:** I am a highly adaptable professional bridging the gap between complex data and compelling digital media. With a solid foundation in health data management, I specialize in transforming raw numbers into actionable insights and engaging content. Whether I'm orchestrating AI-assisted Python scripts, designing high-impact visual campaigns in Canva, or editing dynamic video content across platforms, I bring a unique, multi-disciplinary approach to problem-solving. I'm actively seeking Virtual Assistant roles where I can leverage my blend of analytical precision and creative storytelling to help teams operate at warp speed.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button("Download Mission Log (Resume)", data=resume_bytes, file_name="Ron_Jay_Ayup_Resume.pdf", mime="application/pdf")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. VIDEO INTRO & ACCOLADES
    v_col1, v_col2 = st.columns([1, 1])
    with v_col1:
        with st.container(border=True):
            st.subheader("📹 Incoming Transmission")
            st.video("https://www.youtube.com/watch?v=EZGyf0IJv3c") 
            st.caption("*^ Press play for a quick overview of my skills, experience, and how I can add value to your team! - Test Video*")

    with v_col2:
        with st.container(border=True):
            st.subheader("🏆 Commendations & Accolades")
            st.write("A track record of setting benchmarks and exceeding expectations.")
            
            st.markdown("""
            <div class="quote-box">
            "Consistently ranked as the <b>first to report</b> critical data to the Regional Office out of six provinces and one city, setting the absolute standard for timely submissions." <br>
            <i>— Department of Health (DOH) CHD CAR</i>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="quote-box" style="border-left-color: #4cc9f0;">
            🏅 <b>Employee of the Month</b> <br>
            🏅 <b>Best in Loan Portfolio</b> <br>
            🏅 <b>Best in Recruitment</b> <br>
            <i>— ASA Philippines Foundation, Inc.</i>
            </div>
            """, unsafe_allow_html=True)
            
    # 3. CORE VA SERVICES & TECH STACK
    with st.container(border=True):
        st.header("🛠️ Core VA Services")
        
        s1, s2 = st.columns(2)
        with s1:
            st.markdown("### 📊 Data & Dashboards")
            st.write("Google Sheets automation, real-time data tracking (like NIP workflows), and transforming raw data into clear, interactive Streamlit/Plotly dashboards.")
            
            st.markdown("### 🎬 Multimedia Magic")
            st.write("End-to-end video editing using Premiere Pro and CapCut for YouTube, TikTok, and Reels, plus eye-catching graphic design via Canva.")
            
        with s2:
            st.markdown("### 🤖 AI-Powered Support")
            st.write("Leveraging AI tools to vibe-code custom solutions, streamline repetitive tasks, and bring tech-forward efficiency to daily administrative operations.")
            
            st.markdown("### 🖥️ IT & Admin 'All-Arounder'")
            st.write("The go-to troubleshooter for computer hardware, complex document layout formatting, and crafting high-stakes PowerPoint presentations and official event certificates.")
            
        st.markdown("---")
        st.markdown("<h4 style='text-align: center; color: #a9d6e5;'>🪐 Tech Stack Orbit</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
            <img src="https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white">
            <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white">
            <img src="https://img.shields.io/badge/Premiere_Pro-9999FF?style=for-the-badge&logo=adobe-premiere-pro&logoColor=white">
            <img src="https://img.shields.io/badge/CapCut-000000?style=for-the-badge&logo=capcut&logoColor=white">
        </div>
        """, unsafe_allow_html=True)

    # 4. SKILL UNIVERSE & CONTACT FORM
    c1, c2 = st.columns([1, 1])
    with c1:
        with st.container(border=True):
            st.subheader("📊 Skill Universe")
            
            st.markdown("""
            <div style="position: relative; width: 100%; height: 0px; display: flex; justify-content: center; z-index: 0;">
                <div style="position: absolute; top: 28px; width: 310px; height: 310px; border-radius: 50%; background: conic-gradient(from 0deg, transparent 70%, rgba(188, 19, 254, 0.7) 100%); animation: radar-spin 4s infinite linear; pointer-events: none;"></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.plotly_chart(fig, use_container_width=True)

    with c2:
        with st.container(border=True):
            st.subheader("📬 Contact the Bridge")
            
            contact_form = """
            <form action="https://formsubmit.co/ronjay.1204@gmail.com" method="POST">
                 <input type="hidden" name="_captcha" value="false">
                 <input type="hidden" name="_next" value="https://my-professional-portfolio-fkegz9fuu9hgkdzjfbbshm.streamlit.app/">
                 <input type="hidden" name="_autoresponse" value="Thanks for reaching out! I have received your message and will get back to you as soon as I can.">
                 <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; background: rgba(255, 255, 255, 0.1); color: white;">
                 <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; background: rgba(255, 255, 255, 0.1); color: white;">
                 <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 100px; background: rgba(255, 255, 255, 0.1); color: white;"></textarea>
                 <button type="submit" style="padding: 10px 20px; border-radius: 50px; background: linear-gradient(45deg, #7209b7, #3f37c9); color: white; border: none; cursor: pointer; width: 100%; transition: 0.3s ease;">Send Signal 🛸</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)
            
    # 5. MISSION BRIEFING (FAQ)
    with st.container(border=True):
        st.subheader("📋 Mission Briefing (FAQ)")
        
        with st.expander("🌍 What are your core working hours and timezone?"):
            st.write("I am based in the Philippines (GMT+8). However, as a Virtual Assistant, I offer highly flexible working hours. I am more than happy to overlap with your team's local timezone to ensure seamless real-time communication when needed.")
            
        with st.expander("⏱️ What is your typical turnaround time?"):
            st.write("For standard data reporting, dashboard updates, and short-form video edits (TikTok/Reels), I typically deliver within 24 to 48 hours. For more complex automations or long-form video editing, I will provide a clear timeline upfront and ensure you get daily progress updates.")
            
        with st.expander("📡 How do we communicate during a project?"):
            st.write("Clear and proactive communication is my top priority. I am highly responsive via Email, Slack, Microsoft Teams, WhatsApp, or Zoom—whichever platform integrates best into your existing workflow.")
            
        with st.expander("🤖 How exactly do you use AI to assist your workflows?"):
            st.write("I leverage AI as a force multiplier. I use it to rapidly generate 'vibe-coded' Python scripts for repetitive tasks, construct complex Google Sheets formulas, troubleshoot data errors instantly, and ideate creative hooks for video content. This allows me to work faster and deliver higher-quality results to you.")

# ==========================================
# PAGE 2: PROJECTS (MISSION LOGS)
# ==========================================
elif page == "🛸 Mission Logs (Projects)":
    st.title("🛸 Mission Logs & Deep Space Projects")
    st.write("A detailed archive of my data monitoring systems, visual design layouts, public health tracking architecture, and video content.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- ABRA FHSIS COMMAND CENTER (UPDATED) ---
    with st.container(border=True):
        fhsis_col1, fhsis_col2 = st.columns([1, 2])
        with fhsis_col1:
            st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
        with fhsis_col2:
            st.header("Abra FHSIS Command Center")
            st.markdown("**Role:** Lead Data Developer / Data Controller III")
            st.markdown("**Tech Stack:** `Python` • `Streamlit` • `Pandas` • `Plotly Express` • `Supabase (PostgreSQL)`")
            st.write("Architected, developed, and deployed a robust, enterprise-grade reporting engine. It automatically ingests, cleans, and visualizes Field Health Services Information System (FHSIS) data across 27 Rural Health Units (RHUs). Recently upgraded with intelligent ETL parsers that auto-heal DOH formatting errors, supporting multiple years including dynamic 2026 templates.")
            st.link_button("Launch FHSIS Dashboard 🚀", "https://abra-fhsis.streamlit.app/")

        with st.expander("🎯 View Technical Achievements & Business Impact"):
            st.markdown("""
            **Key Contributions & Technical Achievements:**
            * **Massive Scale & Modularity:** Scaled the application to track 27 multi-sheet modules including Child Immunization, NCD, WASH, Maternal Health, Family Planning, and Mortality & Injuries.
            * **Dynamic Linkage-to-Care Cascades:** Engineered complex funnel charts and waterfall pipelines that intelligently adapt to available data (e.g., detecting new HIV indicators for 2026), providing instant visual feedback on patient drop-off rates and medical cascades.
            * **Auto-Healing ETL Pipeline:** Built a robust Python/Pandas extraction engine that automatically reads messy government Excel templates. The system dynamically standardizes headers, intelligently bypasses blank data, and 'auto-heals' DOH formatting errors and typos with zero manual intervention.
            * **Advanced Interactive Analytics:** Designed comprehensive dashboards featuring geospatial heatmaps, automated Family Planning (CPR) calculations, and Year-over-Year (YoY) comparison engines.
            * **Automated Quality Assurance:** Developed an algorithmic Data Quality Audit system that silently scans incoming data to flag statistical anomalies—such as >100% coverage rates or negative patient dropout rates—ensuring strict reporting integrity.
            * **Master Export & Cloud Storage:** Implemented a one-click Master Regional Export feature that seamlessly compiles a year's worth of data into official Excel formatting, powered by a persistent Supabase backend with automated backup/restore functionality.

            **Business Impact:**
            Transformed a fragmented, highly manual monthly reporting workflow into a fully automated, real-time dashboard. The system empowers health officials to instantly identify high-risk demographic hotspots, track multi-year growth, and generate boardroom-ready reports in seconds.
            """)

        with st.expander("🎯 View QA & Product Strategy Highlights"):
            st.markdown("""
            Beyond core data engineering, I actively lead end-to-end Quality Assurance (QA) and Product Strategy for this application to ensure enterprise-grade reliability.

            **Key Competencies Demonstrated:**
            * 🧠 **Edge-Case Logic & Data Integrity:** Identified critical visualization breaks (e.g., funnel chart logic failures during dynamic user filtering) and engineered smart UI fallbacks to protect data integrity.
            * 📏 **UI/UX & Pixel-Perfect Auditing:** Diagnosed and resolved complex CSS Flexbox alignment issues and native framework spacing bugs to achieve strict, professional visual standards.
            * 🌐 **Cross-Environment Auditing:** Conducted rigorous testing outside the standard web UI, including custom print-engine rendering (`@media print` CSS) to ensure digital dashboards convert flawlessly to physical executive reports.
            * 🚀 **Product Strategy & Vision:** Continuously aligned application architecture, copy, and branding with high-level executive use cases, ensuring the tool solves actual business problems rather than just displaying data.
            """)

    # --- NEW: SIA 2026 DASHBOARD ---
    with st.container(border=True):
        sia_col1, sia_col2 = st.columns([1, 2])
        with sia_col1:
            st.image("https://images.unsplash.com/photo-1615461066841-6116e61058f4?q=80&w=2000&auto=format&fit=crop", use_container_width=True)
        with sia_col2:
            st.header("SIA 2026 Dashboard")
            st.write("A rapid-response real-time tracking application currently in development, designed specifically for the 2026 Supplemental Immunization Activity (SIA) campaign. Built to monitor daily vaccination targets, generate geospatial coverage maps, and rapidly identify zero-dose children across the province.")
            st.markdown("**Core Engines:** `Python` • `Streamlit` • `Pandas` • `Plotly`")
            st.link_button("Launch SIA 2026 App 🚀", "https://abrasia2026.streamlit.app/") # Update this link when ready!

    # --- EXISTING: VACCINE INVENTORY COMMAND CENTER ---
    with st.container(border=True):
        p0_col1, p0_col2 = st.columns([1, 2])
        with p0_col1:
            st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/Capture.PNG?raw=true", use_container_width=True)
        with p0_col2:
            st.header("Abra PHO Vaccine Inventory Command Center")
            st.write("A secure, real-time logistics web application transforming complex 2D spreadsheet matrices into a searchable database for tracking cold chain stock, expiries, and critical stockouts across 27 municipalities.")
            st.markdown("**Core Engines:** `Python` • `Streamlit` • `Pandas` • `Plotly` • `Google Sheets API`")
            st.link_button("Launch Command Center 🚀", "https://abra-physical-inventory-wtrwyrwm6a9fq9ajknnzbd.streamlit.app")

    # --- EXISTING: ABRA SBI DASHBOARD ---
    with st.container(border=True):
        p1_col1, p1_col2 = st.columns([1, 2])
        with p1_col1:
            st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
        with p1_col2:
            st.header("Abra SBI Dashboard")
            st.write("A real-time geospatial monitoring system built to track provincial vaccination coverage, synthesizing complex data for rapid decision making.")
            st.markdown("**Core Engines:** `Python` • `Streamlit` • `Plotly` • `Google API`")
            st.link_button("Launch Dashboard 🚀", "https://abra-sbi-dashboard-5uubqi6rcsqdknxudevhrv.streamlit.app/")

    # --- NIP DATA TRACKING WITH METRICS ---
    with st.container(border=True):
        st.header("📊 NIP Data Tracking & Automation")
        st.write("Engineered comprehensive Google Sheet trackers to monitor, evaluate, and manage National Immunization Program (NIP) activities, streamlining data collection for vital public health initiatives.")
        st.markdown("**Core Engines:** `Google Sheets` • `Data Management` • `NIP Tracking` • `Data Validation`")
        
        st.markdown("<br>", unsafe_allow_html=True)
        met1, met2, met3 = st.columns(3)
        met1.metric(label="Province Monitored", value="Abra", delta="Target Region", delta_color="off")
        met2.metric(label="Municipalities Tracked", value="27", delta="100% Coverage", delta_color="normal")
        met3.metric(label="Data Accuracy", value="100%", delta="Regularly Audited", delta_color="normal")
        st.markdown("<br>", unsafe_allow_html=True)
        
        nip_c1, nip_c2 = st.columns(2)
        with nip_c1:
            st.markdown("### 💉 Immunization Campaigns")
            st.markdown("""
            <div class="project-list">
            • School Based Immunization Tracker (2024 & 2025) <br>
            • bOPV Supplemental Immunization Activity (2023 & 2024) <br>
            • MR Supplemental Immunization Activity (2023 & 2024)
            </div>
            """, unsafe_allow_html=True)
        with nip_c2:
            st.markdown("### 📋 Logistics & Outbreak Response")
            st.markdown("""
            <div class="project-list">
            • COVID-19 Vaccination Tracker <br>
            • Flu Vaccination Tracker <br>
            • Vaccine Physical Inventory Tracker <br>
            • <i>And many more custom surveillance tools...</i>
            </div>
            """, unsafe_allow_html=True)

    # --- CANVA DESIGN GALLERY ---
    with st.container(border=True):
        st.header("🎨 Visual Design & Cartography Gallery")
        st.write("Conceptualized and designed high-impact visual assets and maps for critical public health initiatives and disaster risk reduction programs.")
        st.markdown("**Core Engines:** `Canva` • `Graphic Design` • `Cartography`")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interactive Image Gallery using Tabs
        tab1, tab2, tab3, tab4 = st.tabs(["🏥 Health Events", "🗺️ Cartography & Maps", "🚨 DRRM-H Plan Layouts", "🎉 Celebrations & Collateral"])
        
        with tab1:
            # Using spacer columns to shrink the single image
            t1_spacer1, t1_main, t1_spacer2 = st.columns([1, 2, 1])
            with t1_main:
                st.markdown("<h4 style='text-align: center; color: #a9d6e5;'>First Aid Training Tarpaulin</h4>", unsafe_allow_html=True)
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/PHO%20BLS%20SFA.png?raw=true&auto=format&fit=crop", caption="Basic Life Support Tarpaulin")
                
        with tab2:
            # Using spacer columns to frame the map nicely
            t2_spacer1, t2_main, t2_spacer2 = st.columns([1, 3, 1])
            with t2_main:
                st.markdown("<h4 style='text-align: center; color: #a9d6e5;'>High Resolution Health Facility Map of Abra</h4>", unsafe_allow_html=True)
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/ABRA.png?raw=true&auto=format&fit=crop", caption="Health Facility Map")
            
        with tab3:
            st.markdown("#### 2026-2028 DRRM-H Plan Layouts")
            st.write("*Includes the Cover Page, Pre-planning, and Finalization Tarpaulins.*")
            
            # Using 3 columns evenly divides and shrinks the 3 DRRM-H assets
            drrm1, drrm2, drrm3 = st.columns(3)
            with drrm1:
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/2026-2028.png?raw=true&auto=format&fit=crop", caption="DRRM-H Cover Page")
            with drrm2:
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/Pre-planning.png?raw=true&auto=format&fit=crop", caption="Pre-planning Tarpaulin")
            with drrm3:
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/Finalization.png?raw=true&auto=format&fit=crop", caption="Finalization Tarpaulin")
            
        with tab4:
            st.write("*Beyond large-scale layouts, I am the designated creator for all official event certificates, PowerPoint presentation decks, and document layouts used during Provincial Health Office activities.*")
            
            # Using spacer columns to slightly shrink the 2 images
            t4_sp1, gal3, gal4, t4_sp2 = st.columns([0.5, 2, 2, 0.5])
            with gal3:
                st.markdown("<h4 style='text-align: center; color: #a9d6e5;'>Hearts Month Celebration 2026</h4>", unsafe_allow_html=True)
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/Hearts.png?raw=true&auto=format&fit=crop", caption="Heart Smart Celebration Tarpaulin")
            with gal4:
                st.markdown("<h4 style='text-align: center; color: #a9d6e5;'>National Oral Health Month 2026</h4>", unsafe_allow_html=True)
                st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/Facebook%20post.png?raw=true&auto=format&fit=crop", caption="Oral Health Tarpaulin")

    with st.container(border=True):
        st.header("🎬 Video Production & Content Creation")
        st.write("Editing, directing, and producing highly engaging multimedia content tailored for varying social media algorithms and audiences.")
        st.markdown("**Core Engines:** `Premiere Pro` • `CapCut` • `After Effects` • `Filmora` • `PowerDirector`")
        st.markdown("<br>", unsafe_allow_html=True)
        
        vid_c1, vid_c2 = st.columns(2)
        with vid_c1:
            st.markdown("### 📱 Distribution Platforms")
            st.markdown("""
            <div class="project-list">
            • YouTube Content <br>
            • TikTok Shorts <br>
            • Facebook Reels & Long-form Video
            </div>
            """, unsafe_allow_html=True)
        with vid_c2:
            st.markdown("### ✂️ Editorial Toolkit")
            st.markdown("""
            <div class="project-list">
            • Advanced Timeline Editing & Transitions <br>
            • Motion Graphics & Basic VFX <br>
            • Multi-platform Format Optimization
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# PAGE 3: EXPERIENCE (TOUR OF DUTY)
# ==========================================
elif page == "🧑‍🚀 Tour of Duty (Experience)":
    st.title("🧑‍🚀 Tour of Duty & Career Orbit")
    st.write("A timeline of my professional experience, showcasing my background in data management, financial operations, and public health tracking.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown('<h2 class="job-title">Data Controller III</h2>', unsafe_allow_html=True)
        st.markdown('**Department of Health (DOH) CHD CAR - Provincial DOH Office Abra**')
        st.markdown('<div class="job-date">2021 – Present</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Data Systems & Scale:** Managed, analyzed, and consolidated vaccination-related data across all 27 municipalities of Abra for Covid-19, supplementary, and routine immunization programs.
        * **Performance Benchmark:** Consistently ranked as the first to report vaccination data to the Regional Office out of six provinces and one city, setting the standard for timely submissions.
        * **Data Integrity:** Conducted regular audits to verify data accuracy, provided expert technical support to data managers, and ensured strict compliance with data privacy regulations.
        * **All-Around IT & Admin Support:** Acted as the go-to technical resource—troubleshooting computer hardware, formatting complex document layouts, and designing official event certificates and PowerPoint presentations for all provincial health activities.
        * **Public Health Support:** Prepared data reports, generated vaccination certificates, and supported quality management system (QMS) implementation.
        """)

    with st.container(border=True):
        st.markdown('<h2 class="job-title">Junior Microfinance Officer</h2>', unsafe_allow_html=True)
        st.markdown('**ASA Philippines Foundation, Inc.**')
        st.markdown('<div class="job-date">2018 – 2021</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Financial Operations:** Oversaw the full accounting cycle, from initial data collection and document preparation to report generation and closing financial records.
        * **Client Management:** Delivered exceptional customer service by processing loan applications efficiently and communicating terms clearly to applicants.
        * **Award Recognition:** Honored with multiple internal awards including *Employee of the Month*, *Best in Loan Portfolio*, and *Best in Recruitment* for consistently exceeding performance metrics.
        """)
        
    with st.container(border=True):
        st.markdown('<h2 class="job-title">Stock Clerk</h2>', unsafe_allow_html=True)
        st.markdown('**SM Supermarket Baguio**')
        st.markdown('<div class="job-date">2018</div>', unsafe_allow_html=True)
        st.markdown("""
        * **Logistics & Inventory:** Efficiently managed inventory storage ensuring accurate tracking, easy access, and proper stock rotation.
        * **Operations Support:** Maintained hazard-free environments, shelved new merchandise according to standards, and actively assisted customers on the floor.
        """)

    with st.container(border=True):
        st.header("🎓 Academic Training")
        st.markdown("**Bachelor of Science in Information Technology**")
        st.markdown("Divine Word College of Bangued | *2014 – 2018*")
        st.write("Graduated with a solid foundation in IT concepts, systems analysis, programming, database management, and network security.")
