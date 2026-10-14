"""Ron Jay C. Ayup — Streamlit Developer Portfolio.

Run locally: streamlit run progfolio.py
Requires: streamlit, pandas, plotly (see requirements.txt).
"""

import smtplib
from email.mime.text import MIMEText
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# Streamlit configuration must precede all other Streamlit calls.
st.set_page_config(
    page_title="Ron Jay C. Ayup | Developer Portfolio",
    page_icon=":material/code:",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent

# -----------------------------------------------------------------------------
# Visual theme
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        background-attachment: fixed;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, .97);
        border-right: 1px solid rgba(255, 255, 255, .07);
    }
    [data-testid="stHeader"] { background: transparent; }
    footer { visibility: hidden; }

    h1 { color: #f8fafc !important; font-weight: 800 !important; letter-spacing: -.5px; }
    h2, h3 { color: #f8fafc !important; font-weight: 700 !important; }
    h4 { color: #cbd5e1 !important; }
    p, li { color: #cbd5e1; line-height: 1.7; }

    /* Navigation */
    section[data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 8px 12px !important;
        transition: background .2s ease !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(14, 165, 233, .12) !important;
    }
    section[data-testid="stSidebar"] .stButton > button div[data-testid="stMarkdownContainer"] {
        display: flex !important;
        justify-content: flex-start !important;
        width: 100% !important;
    }
    section[data-testid="stSidebar"] .stButton > button p {
        color: #cbd5e1 !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        text-align: left !important;
        margin: 0 !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover p { color: #38bdf8 !important; }

    /* Glassy cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(30, 41, 59, .35) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, .09) !important;
        border-radius: 14px !important;
        padding: 16px !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, .13);
    }
    .typing-text {
        display: inline-block;
        overflow: hidden;
        max-width: 100%;
        border-right: 3px solid #0ea5e9;
        white-space: nowrap;
        animation: typing 3.5s steps(43, end) forwards, blink .8s step-end infinite;
        font-size: clamp(1rem, 2vw, 1.4rem);
        font-weight: 600;
        color: #38bdf8;
        margin-top: -12px;
        margin-bottom: 16px;
    }
    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { from, to { border-color: transparent; } 50% { border-color: #0ea5e9; } }

    .tech-pill {
        display: inline-block;
        background: rgba(14, 165, 233, .12);
        border: 1px solid rgba(14, 165, 233, .28);
        color: #7dd3fc;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: .84rem;
        margin: 0 5px 8px 0;
        font-weight: 500;
    }
    .tech-stack {
        display: block;
        color: #7dd3fc;
        font-size: .91rem;
        font-weight: 500;
        line-height: 1.7;
        margin: 0 0 14px;
    }
    .project-status {
        display: inline-block;
        color: #cbd5e1;
        background: rgba(56, 189, 248, .10);
        border: 1px solid rgba(56, 189, 248, .24);
        padding: 4px 11px;
        border-radius: 99px;
        font-size: .82rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .job-title { color: #f8fafc; font-size: 1.35rem; font-weight: 750; }
    .job-company { color: #7dd3fc; font-weight: 600; margin-top: 4px; }
    .job-date { color: #94a3b8; font-size: .9rem; margin: 2px 0 14px; }

    .stButton > button[kind="primary"], [data-testid="stDownloadButton"] button {
        background: #0ea5e9 !important;
        color: white !important;
        border: 0 !important;
        border-radius: 7px !important;
        font-weight: 600 !important;
    }
    .stButton > button[kind="primary"] *, [data-testid="stDownloadButton"] button * {
        color: white !important;
    }
    .stButton > button[kind="primary"]:hover, [data-testid="stDownloadButton"] button:hover {
        background: #0284c7 !important;
    }
    @media (max-width: 640px) {
        .typing-text { font-size: 1rem; letter-spacing: -.3px; }
        h1 { font-size: 2rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def pills(values):
    """Display trusted, locally defined technology labels."""
    from html import escape

    spans = "".join(f'<span class="tech-pill">{escape(value)}</span>' for value in values)
    st.markdown(f'<div style="margin-bottom: 8px">{spans}</div>', unsafe_allow_html=True)


def project_card(title, stack, summary, highlights=None, status=None, url=None, note=None):
    """Consistent project presentation with optional context and external link."""
    from html import escape

    with st.container(border=True):
        st.subheader(title)
        if status:
            st.markdown(
                f'<span class="project-status">{escape(status)}</span>',
                unsafe_allow_html=True,
            )
        st.markdown(
            f'<span class="tech-stack">{escape(stack)}</span>',
            unsafe_allow_html=True,
        )
        st.write(summary)
        if highlights:
            st.markdown(f"**Key capabilities:** {highlights}")
        if url:
            st.link_button("View Project", url, icon=":material/open_in_new:")
        if note:
            st.caption(note)


def experience_card(position, organization, dates, responsibilities):
    from html import escape

    with st.container(border=True):
        st.markdown(
            f'<div class="job-title">{escape(position)}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="job-company">{escape(organization)}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="job-date">{escape(dates)}</div>',
            unsafe_allow_html=True,
        )
        for heading, detail in responsibilities:
            st.markdown(f"- **{heading}:** {detail}")


# -----------------------------------------------------------------------------
# Sidebar navigation
# -----------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

with st.sidebar:
    st.markdown("### :material/dashboard: Navigation")
    if st.button("Home / About Me", icon=":material/person:", use_container_width=True):
        st.session_state.page = "home"
    if st.button("Projects & Apps", icon=":material/terminal:", use_container_width=True):
        st.session_state.page = "projects"
    if st.button("Professional Experience", icon=":material/work_history:", use_container_width=True):
        st.session_state.page = "experience"

    st.divider()
    st.markdown("### :material/link: Connect")
    st.markdown(":material/mail: [Email](mailto:ronjay.1204@gmail.com)")
    st.markdown(":material/code: [GitHub](https://github.com/RJA24)")
    st.markdown(":material/work: [LinkedIn](https://www.linkedin.com/in/ron-jay-ayup-a1824b3b3)")


# -----------------------------------------------------------------------------
# HOME
# -----------------------------------------------------------------------------
if st.session_state.page == "home":
    col_profile, col_intro = st.columns([1, 2.5], gap="large")
    with col_profile:
        profile_path = BASE_DIR / "Profile.png"
        if profile_path.exists():
            st.image(str(profile_path), width=260)
        else:
            st.info("Profile image unavailable.")

    with col_intro:
        st.title("Ron Jay C. Ayup")
        st.markdown(
            '<div class="typing-text">Full-Stack Programmer &amp; Data Analyst</div>',
            unsafe_allow_html=True,
        )
        st.write(
            "I am a software developer and data analyst specializing in practical, "
            "end-to-end data systems, automation, and interactive web applications. "
            "My background in public health data management helps me turn fragmented "
            "reports and manual workflows into reliable digital tools."
        )
        st.write(
            "I design Streamlit dashboards, build data-cleaning and reporting pipelines, "
            "work with relational databases and spreadsheet integrations, and deliver "
            "custom software for real operational needs. My work ranges from provincial "
            "health information systems to a paid document retrieval solution for a client."
        )
        resume_path = BASE_DIR / "resume.pdf"
        if resume_path.exists():
            st.download_button(
                "Download Resume (PDF)",
                data=resume_path.read_bytes(),
                file_name="Ron_Jay_Ayup_Resume.pdf",
                mime="application/pdf",
                icon=":material/download:",
                type="primary",
            )

    st.write("")
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        with st.container(border=True):
            st.subheader(":material/radar: Core Competencies")
            skills = pd.DataFrame(
                {
                    "r": [90, 85, 80, 85, 75, 80],
                    "theta": [
                        "Data Engineering & ETL",
                        "Full-Stack Development",
                        "Geospatial Mapping",
                        "Database Administration",
                        "Mobile App Development",
                        "UI/UX & Frontend",
                    ],
                    "Details": [
                        "Automated parsers and data pipelines with Pandas",
                        "End-to-end web applications using Python and Streamlit",
                        "Plotly maps, GeoJSON, and geographic data transformation",
                        "Working with relational databases and Google Sheets",
                        "Cross-platform mobile development with React Native and Expo",
                        "Interactive reports, dashboards, and accessible interfaces",
                    ],
                }
            )
            fig = px.line_polar(
                skills,
                r="r",
                theta="theta",
                line_close=True,
                hover_data={"r": False, "theta": False, "Details": True},
            )
            fig.update_traces(
                fill="toself",
                line_color="#0ea5e9",
                fillcolor="rgba(14, 165, 233, 0.2)",
                mode="lines+markers",
                marker=dict(size=8, color="#38bdf8"),
                hovertemplate="<b>%{theta}</b><br>%{customdata[0]}<extra></extra>",
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#f8fafc",
                polar=dict(
                    bgcolor="rgba(0,0,0,0)",
                    radialaxis=dict(visible=False),
                    angularaxis=dict(linecolor="rgba(255,255,255,0.15)"),
                ),
                margin=dict(l=35, r=35, t=15, b=20),
                height=350,
            )
            st.plotly_chart(fig, use_container_width=True)

        with st.container(border=True):
            st.subheader(":material/contact_mail: Contact Me")
            with st.form("contact_form", clear_on_submit=True):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Your Message", height=120)
                submitted = st.form_submit_button(
                    "Send Message", type="primary", use_container_width=True
                )

            if submitted:
                if not name.strip() or not email.strip() or not message.strip():
                    st.warning("Please fill out all fields before sending.")
                elif "@" not in email or "." not in email.split("@")[-1]:
                    st.warning("Please enter a valid email address.")
                else:
                    try:
                        smtp_user = st.secrets["EMAIL_USER"]
                        smtp_password = st.secrets["EMAIL_PASS"]
                        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                        msg = MIMEText(body)
                        msg["Subject"] = f"New Portfolio Message from {name}"
                        msg["From"] = smtp_user
                        msg["To"] = "ronjay.1204@gmail.com"
                        msg["Reply-To"] = email.strip()
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20) as server:
                            server.login(smtp_user, smtp_password)
                            server.sendmail(smtp_user, [msg["To"]], msg.as_string())
                        st.success("Message sent successfully. Thank you!")
                    except Exception:
                        st.error(
                            "The contact form is temporarily unavailable. "
                            "Please email me using the link in the sidebar."
                        )

    with col_right:
        with st.container(border=True):
            st.subheader(":material/memory: Technical Stack")
            st.markdown("#### Languages & Frameworks")
            pills(["Python", "Streamlit", "React Native", "Expo", "SQL", "JavaScript"])
            st.markdown("#### Data Engineering & Analytics")
            pills(["Pandas", "Plotly Express", "OpenCV", "MediaPipe", "ETL Pipelines"])
            st.markdown("#### Databases & Infrastructure")
            pills(["PostgreSQL", "Supabase", "Google Sheets API", "Git / GitHub"])
            st.markdown("#### Design & Multimedia")
            pills(["Canva", "Figma", "Premiere Pro", "UI/UX Auditing"])

        with st.container(border=True):
            st.subheader(":material/forum: Frequently Asked Questions")
            with st.expander("Working hours and timezone?"):
                st.write(
                    "I am based in the Philippines (GMT+8) and can coordinate "
                    "across time zones for project-based work."
                )
            with st.expander("How do you handle data privacy and security?"):
                st.write(
                    "I bring a public-health data management background to projects "
                    "that require careful access controls, responsible data handling, "
                    "and secure storage of credentials."
                )
            with st.expander("Can you handle end-to-end development?"):
                st.write(
                    "Yes. I can work from requirements and data workflows through "
                    "implementation, testing, deployment, training, and troubleshooting."
                )
            with st.expander("Approach to AI-assisted coding?"):
                st.write(
                    "I use AI to speed up prototyping, debugging, and documentation "
                    "while remaining responsible for reviewing and testing the final result."
                )


# -----------------------------------------------------------------------------
# PROJECTS & APPS
# -----------------------------------------------------------------------------
elif st.session_state.page == "projects":
    st.title(":material/code_blocks: Projects & Applications")
    st.write(
        "Selected public health systems, delivered client applications, "
        "software engineering projects, and data visualization work."
    )
    st.write("")
    st.markdown("### Tier 1: Enterprise Data Systems & Client Solutions")

    project_card(
        title="Abra NIP Monitoring Information System",
        status="Provincial Public Health System | 27 RHUs",
        stack="Python • Streamlit • Pandas • Excel Reporting • Data Validation • Dashboard Analytics",
        summary=(
            "Designed and developed a provincial immunization monitoring information system "
            "supporting the 27 Rural Health Units (RHUs) of Abra. Combines campaign "
            "configuration, immunization data reporting, monitoring, and administrative "
            "workflows in one platform."
        ),
        highlights=(
            "Role-based access for RHU users and administrators; an offline-first "
            "School-Based Immunization (SBI) Excel workbook organized by activity date, "
            "school, and grade; upload and correction workflows; campaign submission "
            "and finalization monitoring; data quality checks and VaccTrack reconciliation."
        ),
        note="Operational health reporting system; private records and credentials are not shown.",
    )

    project_card(
        title="SSS Auto FOD — Document Archiving & Retrieval System",
        status="Paid Freelance Client Project | SSS Bangued Branch",
        stack="Python • Excel Processing • Document Indexing • Local Data Storage • Windows Deployment",
        summary=(
            "Built and delivered a custom document archiving and retrieval solution for "
            "the Social Security System (SSS) Bangued Branch. The software turns "
            "transmittal spreadsheets into searchable, organized records and helps staff "
            "find physical documents through their assigned storage locations."
        ),
        highlights=(
            "Transmittal import and document classification; searchable records; "
            "warehouse and shelf visualization; document retrieval workflow; "
            "duplicate-transmittal detection; local installation and client support."
        ),
        note="Commercially delivered as a private client solution; source code and client data are not publicly shared.",
    )

    project_card(
        title="Abra PESU Surveillance Portal",
        stack="Python • Streamlit • Pandas • Plotly • Google Sheets API • Cryptography",
        summary=(
            "Engineered an epidemiological surveillance portal to support provincial "
            "monitoring of communicable diseases, including dengue and tuberculosis, "
            "with interactive visualizations and data-management workflows."
        ),
        highlights=(
            "Role-based access; automated reporting summaries; year-over-year "
            "comparisons; epidemiological data cleaning; and Plotly geospatial "
            "visualizations using custom GeoJSON boundaries."
        ),
    )

    project_card(
        title="National Immunization Program: SIA 2026 Command Center",
        stack="Python • Streamlit • Supabase (PostgreSQL) • AgGrid • Plotly Express",
        summary=(
            "Developed a provincial monitoring dashboard for the 2026 Measles-Rubella "
            "and Vitamin A campaign, with a reporting database and visualizations "
            "for local health program monitoring."
        ),
        highlights=(
            "Campaign data uploads, RHU reporting summaries, VaccTrack comparison, "
            "discrepancy checking, daily tallies, and map-based presentation."
        ),
    )

    project_card(
        title="Abra FHSIS Command Center",
        stack="Python • Streamlit • Pandas • Plotly Express",
        summary=(
            "Built a modular reporting and visualization tool for Field Health Services "
            "Information System (FHSIS) data, reducing manual spreadsheet cleanup."
        ),
        highlights=(
            "Automated data ingestion, resilient header standardization, "
            "indicator summaries, and data quality checks."
        ),
        url="https://abra-fhsis.streamlit.app/",
    )

    project_card(
        title="Vaccine Logistics & Inventory Matrix",
        stack="Python • Streamlit • Pandas • Google Sheets API",
        summary=(
            "Converted hard-to-read vaccine inventory spreadsheets into a searchable "
            "dashboard for provincial logistics tracking."
        ),
        highlights="Stock visibility, vaccine batch expiry tracking, and stockout monitoring.",
    )

    st.write("")
    st.markdown("### Tier 2: Software Engineering")
    sw_left, sw_right = st.columns(2, gap="medium")
    with sw_left:
        project_card(
            title="Gesture Control Engine",
            stack="Python • OpenCV • MediaPipe • PyAutoGUI",
            summary=(
                "Built a webcam-based computer vision prototype that tracks hand "
                "gestures to control common mouse actions."
            ),
        )
    with sw_right:
        project_card(
            title="Mobile Station Mapper",
            stack="React Native • Expo • Google Maps API",
            summary=(
                "Developed a mobile mapping prototype for finding fuel stations "
                "and supporting motorcycle route planning."
            ),
        )

    st.write("")
    st.markdown("### Tier 3: Frontend Design & Multimedia")
    with st.container(border=True):
        st.subheader("Vector Cartography & Public Health Layouts")
        st.write(
            "I also work on interface design, print-ready geographic maps, "
            "PowerPoint presentations, and large-format event materials for "
            "public health programs using Canva and multimedia tools."
        )


# -----------------------------------------------------------------------------
# PROFESSIONAL EXPERIENCE
# -----------------------------------------------------------------------------
elif st.session_state.page == "experience":
    st.title(":material/work_history: Professional Experience")
    st.write(
        "A timeline of my professional roles and independent software development work."
    )
    st.write("")

    experience_card(
        position="Freelance Software Developer",
        organization="Self-Employed | Client: Social Security System (SSS), Bangued Branch",
        dates="July 2026 – Present | Project-Based / Freelance",
        responsibilities=[
            (
                "Paid Client Delivery",
                "Designed, developed, and delivered the SSS Auto FOD document archiving "
                "and retrieval system as an independent software-development engagement.",
            ),
            (
                "Workflow Automation",
                "Implemented Excel transmittal imports, record organization, "
                "document classification, and duplicate detection.",
            ),
            (
                "Document Search & Retrieval",
                "Developed record search, storage-location lookup, and visual shelf tracking "
                "to support physical file retrieval.",
            ),
            (
                "Deployment & Client Support",
                "Set up the application for local Windows use, performed troubleshooting "
                "and refinements, and prepared user guidance.",
            ),
        ],
    )

    experience_card(
        position="Data Controller III",
        organization="Department of Health (DOH) CHD CAR — Provincial DOH Office of Abra",
        dates="2021 – Present",
        responsibilities=[
            (
                "Data Consolidation",
                "Consolidate, clean, and maintain public health datasets from 27 RHUs "
                "for routine and supplemental immunization and disease surveillance.",
            ),
            (
                "Reporting & Automation",
                "Develop automated dashboards, reporting workflows, and data-cleaning "
                "tools using Python and spreadsheets.",
            ),
            (
                "Quality Assurance",
                "Validate submissions, reconcile reporting discrepancies, and provide "
                "technical assistance to local reporting staff.",
            ),
            (
                "Systems Development",
                "Designed and improved provincial monitoring tools including the "
                "Abra NIP Monitoring Information System and the Abra PESU dashboard.",
            ),
        ],
    )

    experience_card(
        position="Junior Microfinance Officer",
        organization="ASA Philippines Foundation, Inc.",
        dates="2018 – 2021",
        responsibilities=[
            (
                "Financial Data Operations",
                "Managed client records, financial document processing, and ledger reporting.",
            ),
            (
                "Portfolio Management",
                "Reviewed loan portfolios and maintained accurate collection records.",
            ),
            (
                "Recognition",
                "Received Employee of the Month, Best in Loan Portfolio, "
                "and Best in Recruitment awards.",
            ),
        ],
    )

    experience_card(
        position="Stock Clerk",
        organization="SM Supermarket Baguio",
        dates="2018",
        responsibilities=[
            (
                "Inventory Control",
                "Maintained physical and digital stock records, performed stock counts, "
                "and supported stock rotation.",
            ),
        ],
    )

    with st.container(border=True):
        st.markdown('<div class="job-title">Bachelor of Science in Information Technology</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-company">Divine Word College of Bangued</div>', unsafe_allow_html=True)
        st.markdown('<div class="job-date">2014 – 2018</div>', unsafe_allow_html=True)
        st.write(
            "Coursework focused on programming, databases, systems analysis, "
            "and computer networking."
        )
