import streamlit as st

# ✅ Set layout to adjust automatically
st.set_page_config(page_title="Shakthi J - Portfolio", page_icon="🔬", layout="wide")
st.markdown("""
    <style>
    /* Set Background Color for Main Content */
    .main {
        background-color: #F5F5DC !important; /* Beige */
        color: #5A3E36 !important; /* Dark Brown Text */
    }

    /* Change Sidebar Background */
    .st-emotion-cache-1gulkj5 {  
        background-color: #EDE0D4 !important; /* Lighter Beige */
    }

    /* Adjust Overall Page */
    html, body, [class*="st-emotion-cache"]  {
        background-color: #F5F5DC !important; /* Beige */
        color: #5A3E36 !important; /* Dark Brown */
    }
    
    /* Change Font Colors for Different Sections */
    h1, h2, h3, h4, p, li {
        color: #5A3E36 !important; /* Dark Brown */
    }

    /* Change Expander Background */
    .st-emotion-cache-1wbqyqz {
        background-color: #EADBC8 !important; /* Soft Cream */
        border-radius: 10px; /* Rounded corners */
        padding: 10px;
    }

    /* Improve Button Styling */
    .stButton>button {
        background-color: #D4A373 !important; /* Warm Beige */
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 8px 16px !important;
    }

    /* Center Align Text in Mobile */
    @media (max-width: 768px) {
        h1 { text-align: center !important; }
        h2 { text-align: center !important; }
        .stMarkdown {
            text-align: left !important;
        }
    }
    </style>
""", unsafe_allow_html=True)



st.title("Welcome to My Portfolio")

# ✅ Custom CSS for Adaptive Design
st.markdown("""
    <style>
    /* General font scaling */
    h1 { font-size: 58px !important; }
    h2 { font-size: 30px !important; }
    h3 { font-size: 26px !important; }
    h4 { font-size: 22px !important; }
    p, li { font-size: 18px !important; }

    /* Responsive adjustments */
    @media (max-width: 768px) { 
        h1 { font-size: 28px !important; text-align: center; }
        h2 { font-size: 24px !important; text-align: center; }
        h3 { font-size: 22px !important; }
        h4 { font-size: 20px !important; }
        p, li { font-size: 16px !important; }

         /* Keep images centered, but text left-aligned */
        .stImage {
            text-align: center !important;
        }

        .stMarkdown {
            text-align: left !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Profile Section
st.markdown("<h1 style='text-align: center;'>🚀 Shakthi J</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 15px;'>Bioinformatics Researcher |Computational Biologist | AI-Driven Problem Solver</h2>", unsafe_allow_html=True)

# ✅ Profile Image - Adjust for Mobile & Laptop
col1, col2 = st.columns([1, 6], gap="small")  # Reduce width ratio & gap
with col1:
    st.image("https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/DSC_1530.jpg", width=200)  # Adjust size manually

with col2:
    st.markdown("""
        - 📍 **Location:** Halasuru, Bengaluru, India  
        - 📧 **Email:** [shakthipostbox@gmail.com](mailto:shakthipostbox@gmail.com)  
        - 🔗 **LinkedIn:** [Shakthi J](https://www.linkedin.com/in/shakthij)  
        - 📞 **Phone:** +91 7337810224  
    """)


st.divider()

# ✅ About Me Section
st.markdown("<h3>🚀 About Me</h3>", unsafe_allow_html=True)
st.markdown("""
🌟 **Dedicated MSc Bioinformatics candidate** passionate about **scientific discovery & healthcare innovation**.  
🔬 Skilled in **NGS, molecular docking, computational analysis, and bioinformatics pipeline development**.  
🤖 Passionate about **AI/ML-driven** innovations in healthcare.  
⚙️ Experienced in **managing large-scale genomic projects** in **Linux-based environments**.  
💡 Passionate about developing **interactive bioinformatics apps** to simplify complex analyses.
""")

st.divider()

# 🔹 Experience Section with Company Logo
st.markdown("<h3>💼 Experience</h3>", unsafe_allow_html=True)

for role, company, timeline, details, company_img in [
    ("Junior Bioinformatician", "Biokart Indian Pvt. Ltd", "April 2023 - August 2023", [
        "Managed clinical datasets using bioinformatics tools for actionable insights.",
        "Completed various bioinformatics projects, including **metagenomics analysis (16S and ITS), comparative (Control vs disease) analysis, RAPD analysis, and SNP (variant calling) analysis**.",
        "Worked proficiently on both **Windows and Ubuntu/Linux** platforms.",
        "Used **open-source tools** to analyze large datasets, visualize data, and generate insights.",
        "Gained hands-on experience in **project management, data handling, and meeting deadlines**.",
        "Skilled at working independently and collaboratively in a team environment.",
        "Passionate about learning and committed to continual improvement.",
        "Assisted with day-to-day operations, working efficiently and productively with all team members."
    ], "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/Biokart.png"),  # Company logo

    ("Bioinformatics Intern", "Biokart Indian Pvt. Ltd", "January 2023 - March 2023", [
        "Assisted in generating **metagenomics and SNP reports** relevant to disease studies.",
        "Conducted **phylogenetic analysis** contributing to clinical insights.",
        "Generated **16S and ITS metagenomic reports**.",
        "Performed **RAPD analysis and phylogenetic report generation**.",
        "Offered a **full-time position** after internship."
    ], "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/Biokart.png")  # Add the company logo here
]:  
    with st.expander(f"**{role} - {company}** *({timeline})*"):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(company_img, width=200)  # Display company logo
        with col2:
            for point in details:
                st.markdown(f"- {point}")

st.divider()



# Skills Section
st.markdown("<h3>🛠 Skills</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h4>⚙️ Technical Skills</h4>", unsafe_allow_html=True)
    for skill in ["🐍 Python & R", "💻 Linux Environment", "📊 Data Analysis & Visualization", "🤖 AI/ML", "🛠 Microsoft Office", "🌐 Open Source Software", "🐙 GitHub"]:
        st.markdown(f"- {skill}")

with col2:
    st.markdown("<h4>🧬 Bioinformatics</h4>", unsafe_allow_html=True)
    for skill in ["🧬 Next-Generation Sequencing (NGS)", "🔍 Clinical Data Analysis", "🧪 Pipeline Development", "🧭 Molecular Docking", "💊 Drug Discovery & Interaction", "📊 Biostatistics", "🔬 Data Analysis"]:
        st.markdown(f"- {skill}")

with col3:
    st.markdown("<h4>🌟 Soft Skills</h4>", unsafe_allow_html=True)
    for skill in ["🗣 Communication", "🤝 Teamwork", "📖 Scientific Literature", "🎯 Problem Solving", "🔄 Flexible"]:
        st.markdown(f"- {skill}")

st.divider()

# 🔹 Education Section with College Images
st.markdown("<h3>🎓 Education</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("GCU.jpg", width=300)  # First college picture
    st.markdown("""
    - **MSc in Bioinformatics (2023-2025 Expected)** - Garden City University |88% - Third Semester|
    - **BSc in Biotechnology, Biochemistry & Genetics (2020-2023)** - Garden City University |81.7%|  
    """)

with col2:
    st.image("St. Joseph's Indian Composite PU College.png", width=500)  # Second college picture
    st.markdown(""" 
    - **Pre-University education in Science - PCMB (2018-2020)** - St. Joseph's Indian Composite PU College |72.3%|  
    """)

st.divider()

# Projects Section
st.markdown("<h3>🚀 Projects</h3>", unsafe_allow_html=True)
projects = [
    ("Metagenome Analysis App Development", "Present",
     "Developed a **Streamlit-based web app** integrated with **Google Colab** to simplify microbiome data analysis for researchers and small labs. Automated sample processing, taxonomic classification, and result visualization while ensuring efficient storage and accessibility.",
     "Streamlit, Google Colab, Linux, Shell Scripting, Kraken2"),
    
    ("16S rRNA Analysis on Gut Microbiota in Hypothyroidism", "Present",
     "Led a study comparing microbial diversity and functional analysis in **16S rRNA sequences** of hypothyroid and healthy pregnant women. Identified taxonomic variations and metabolic pathways to understand the gut microbiome's role in hypothyroidism.",
     "QIIME2, Mothur, FastQC and MultiQC, Kraken2, Microsoft Excel, LEfSe, PICRUSt2, Python (Pandas, Matplotlib, Seaborn), Galaxy"),
    
    ("AI/ML-Based Classification of Lung Cancer Using Gene Expression Data from Kaggle", "Nov 2024 - Dec 2024",
     "Implemented **AI/ML techniques and Biostatistics** to classify lung cancer subtypes using the **TCGA-LUSC dataset**. Applied **PCA and machine learning models** to extract significant features, achieving high classification accuracy.",
     "Python (scikit-learn, Pandas, NumPy, Matplotlib, Seaborn), PCA, SVM, Random Forest, Logistic Regression, TCGA database"),
    
    ("Ribosome QSAR Analysis Using ChEMBL Database", "Sep 2024 - Dec 2024",
     "Analyzed **ribosome-targeting compounds** using **QSAR modeling** to identify potential therapeutic candidates. Evaluated molecular properties, enhanced compound screening reliability, and supported translational medicine research.",
     "ChEMBL, RDKit, AutoDock, Python, QSAR modeling, Chemoinformatics tools"),
    
    ("80S Ribosome Docking Project with Psychiatric Drugs", "Aug 2024 - Dec 2024",
     "Performed **molecular docking studies** on psychiatric drugs with the **80S ribosome**, integrating both **RNA and protein components**. Evaluated binding affinities to understand potential drug-target interactions.",
     "AutoDock, Chimera, Discovery Studio, Open Babel, Python (BioPython), PDB datasets"),
    
    ("Salmonella typhi Epitope-Based Vaccine Design", "July 2024 - Sep 2024",
     "Designed a **computational vaccine** against **Salmonella typhi** using **epitope prediction, molecular docking, and in-silico validation**. Identified potential immunogenic candidates for vaccine development.",
     "IEDB, VaxiJen, AutoDock, Chimera, Discovery Studio, Python (Pandas, NumPy), Peptide modeling tools"),
    
    ("Comparative Analysis of Chloroplast Genomes", "May 2023 - Aug 2023",
     "Mapped and analyzed **chloroplast genomes** across multiple plant species using **next-generation sequencing (NGS)**. Conducted phylogenetic analysis to study evolutionary divergence and functional gene variations.",
     "BLAST, MAFFT, MEGA, Python (Biopython, Pandas, Matplotlib), NGS tools, Phylogenetic Tree Construction tools")
]

for title, timeline, description, tools in projects:
    with st.expander(f"🎯 **{title}** *({timeline})*"):
        st.write(description)
        st.markdown(f"**🛠 Tools Used:** {tools}")

st.divider()

# Languages & Interests Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3>🌍 Languages</h3>", unsafe_allow_html=True)
    st.markdown("\n".join([f"- {lang}" for lang in ["English", "Hindi", "Kannada", "Tamil", "Telugu"]]))

with col2:
    st.markdown("<h3>🎯 Interests</h3>", unsafe_allow_html=True)
    st.markdown("\n".join([f"- {interest}" for interest in ["App Development", "Machine Learning", "Biomarker Discovery", "Personalized Medicine", "Big Data Analytics", "Power BI"]]))

st.divider()

# 🔹 Achievements Section with Personal & NCC Picture
st.markdown("<h3>🏆 Achievements</h3>", unsafe_allow_html=True)

achievements = [
    {"title": "5th Prize in Samatva 2nd Annual Lecture Competition",
     "description": """Presented on **'Unlocking the Secrets of Chloroplasts: A Next-Gen Sequencing Adventure'**.  
     📌 **Presentation at Samatva 2023**: Delivered a research-driven presentation on chloroplasts, highlighting key advancements in plant molecular biology and bioinformatics.  
     🎯 Engaged with an academic audience, effectively communicating complex scientific concepts.""",
     "event": "Manipal Institute of Regenerative Medicine, MAHE",
     "images": [
         {"path": "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/Samatva.jpeg", "width": 500},  # Custom width for image 1
         {"path": "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/Samatva_2.jpeg", "width": 450}  # Custom width for image 2
     ]},

    {"title": "National Cadet Corps (NCC) - Sergeant",
     "description": """Served as an NCC Sergeant, demonstrating leadership and discipline.  
     📌 **NCC Achievement**: Successfully completed NCC training, developing strong leadership, discipline, and teamwork skills.  
     🎯 Participated in various drills, camps, and social service activities, demonstrating commitment to national service and personal growth.""",
     "event": "2020 - 2023",
     "images": [
         {"path": "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/NCC_1.jpeg", "width": 300},  # Custom width for image 1
         {"path": "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/NCC_2.jpeg", "width": 400}  # Custom width for image 2
     ]}
]

for ach in achievements:
    with st.expander(f"🎖 **{ach['title']}**"):
        st.markdown(f"{ach['description']}  \n📍 *{ach['event']}*")

        # Create two columns for side-by-side images
        col1, col2 = st.columns(2)

        with col1:
            st.image(ach["images"][0]["path"], width=ach["images"][0]["width"])  # First image with custom width

        with col2:
            st.image(ach["images"][1]["path"], width=ach["images"][1]["width"])  # Second image with custom width

st.divider()



# References Section
st.markdown("<h3>📌 References</h3>", unsafe_allow_html=True)

for ref in [
    {"name": "Dr. L.A Rama Chandra Prasad", "designation": "Associate Professor, R&D Coordinator<br>Bioinformatics Program Coordinator",
     "institution": "Department of Life Sciences, Garden City University<br>Bengaluru-560049",
     "email": "ramachandra.prasad@gcu.edu.in", "phone": "+91 8618684623"},
    {"name": "Dr. V.G. Shanmuga Priya", "designation": "Associate Professor",
     "institution": "Department of Life Sciences, Garden City University<br>Bengaluru-560049",
     "email": "shanmuga.priya@gcu.edu.in", "phone": "+91 9480563489"}
]:
    st.markdown(f"""
    <div style="font-size:18px;">
    <b>{ref['name']}</b>  <br>
    {ref['designation']}  <br>
    {ref['institution']}  <br>
    📧 <a href="mailto:{ref['email']}">{ref['email']}</a>  <br>
    📞 {ref['phone']}  
    </div>
    <hr style="border: 1px solid #ddd;">
    """, unsafe_allow_html=True)


# Footer
st.markdown("🚀 **Portfolio built with Streamlit** | 📌 Last updated: 2025")

