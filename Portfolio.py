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



st.title("Welcome!!")

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

# Profile Section
st.markdown("<h1 style='text-align: center;'>I'm Shakthi J</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 15px;'>Bioinformatics Researcher | Computational Biologist | AI-Driven Problem Solver</h2>", unsafe_allow_html=True)

# Profile Image and About Me Side-by-Side
col1, col2 = st.columns([1, 4], gap="small")  # Slightly adjusted width ratio

with col1:
    st.image("https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/DSC_1530.jpg", width=160)  # Slightly smaller image

with col2:
    st.markdown("""
    <h3>🚀 About Me</h3>
    <p>
    🌟 <b>Dedicated MSc Bioinformatics candidate</b> passionate about <b>scientific discovery & healthcare innovation</b>.<br>
    🔬 Skilled in <b>NGS, computational analysis, and bioinformatics pipeline development</b>.<br>
    🤖 Passionate about <b>AI/ML-driven</b> innovations in healthcare.<br>
    ⚙️ Experienced in <b>managing large-scale genomic projects</b> in <b>Linux-based environments</b>.<br>
    💡 Passionate about developing <b>interactive bioinformatics apps</b> to simplify complex analyses.
    </p>
    """, unsafe_allow_html=True)

st.divider()


# 🔹 Experience Section with Company Logo
st.markdown("<h3>💼 Experience</h3>", unsafe_allow_html=True)

for role, company, timeline, details, company_img in [
    ("Computational Biology Intern", "Biocon Ltd", "September 2025 - Present", [
        "Assisting **Bioinformatics team in API R&D fermentation department**.",
        "Learning to conduct research in an industrial setting with focus on **R&D methodologies**.",
        "Supporting ongoing projects under senior supervision and contributing to **data analysis workflows**.",
        "Working on **Linux and computational biology tools** for large-scale data handling.",
        "Gaining exposure to **clinical research and bioinformatics applications** in drug development."
    ], "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/Biocon.jpg"),  # Add Biocon logo

    ("Bioinformatics Research Intern", "Institute of Bioinformatics and Applied Biotechnology (IBAB)", "February 2025 - June 2025", [
    "Performed **comparative analysis of 16S rRNA and Whole Genome Shotgun (WGS) metagenomic datasets** using open-source tools.",
    "Gained hands-on experience with pipelines involving **QIIME2 for 16S** and **Kraken2 and Bracken for WGS** analysis.",
    "Assessed strengths and limitations of both approaches in terms of **taxonomic resolution, functional profiling, and computational requirements**.",
    "Developed and optimized workflows for preprocessing, classification, and diversity analysis of metagenomic data.",
    "Worked on **Google Colab and Linux-based environments** for reproducible, scalable workflows.",
    "Documented and presented findings through internal reviews, highlighting key differences in microbial identification capabilities between 16S and WGS."
], "https://raw.githubusercontent.com/Shakthi-J/Shakthi_J_Portfolio/main/IBAB-logo.png"),

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
    for skill in ["🧬 Next-Generation Sequencing (NGS)", "🧬 Nextflow", "🔍 Clinical Data Analysis", "🧪 Pipeline Development", "🧭 Molecular Docking", "💊 Drug Discovery & Interaction", "📊 Biostatistics", "🔬 Data Analysis"]:
        st.markdown(f"- {skill}")

with col3:
    st.markdown("<h4>🌟 Soft Skills</h4>", unsafe_allow_html=True)
    for skill in ["🗣 Communication", "🤝 Teamwork", "🤖 Individual Player", "📖 Scientific Literature", "🎯 Problem Solving", "🔄 Flexible"]:
        st.markdown(f"- {skill}")

st.divider()

# Projects Section
st.markdown("<h3>🚀 Projects</h3>", unsafe_allow_html=True)
projects = [
    ("Metagenome Analysis App Development", "Present",
     "Developed a **Streamlit-based web app** integrated with **Google Colab** to simplify microbiome data analysis for researchers and small labs. Automated sample processing, taxonomic classification, and result visualization while ensuring efficient storage and accessibility.",
     "Streamlit, Google Colab, Linux, Shell Scripting, Kraken2"),
    
    ("16S rRNA Analysis on Gut Microbiota in Hypothyroidism", "Dec 2024 - Feb 2025",
     "Led a study comparing microbial diversity and functional analysis in **16S rRNA sequences** of hypothyroid and healthy pregnant women. Identified taxonomic variations and metabolic pathways to understand the gut microbiome's role in hypothyroidism.",
     "QIIME2, Mothur, FastQC and MultiQC, Kraken2, Microsoft Excel, LEfSe, PICRUSt2, Python (Pandas, Matplotlib, Seaborn), Galaxy"),
    
    ("AI/ML-Based Classification of Lung Cancer Using Gene Expression Data from Kaggle", "Nov 2024 - Dec 2024",
     "Implemented **AI/ML techniques and Biostatistics** to classify lung cancer subtypes using the **TCGA-LUSC dataset**. Applied **PCA and machine learning models** to extract significant features, achieving high classification accuracy.",
     "Python (scikit-learn, Pandas, NumPy, Matplotlib, Seaborn), PCA, SVM, Random Forest, Logistic Regression, TCGA database"),
    
    ("Ribosome QSAR Analysis Using ChEMBL Database", "Sep 2024 - Oct 2024",
     "Analyzed **ribosome-targeting compounds** using **QSAR modeling** to identify potential therapeutic candidates. Evaluated molecular properties, enhanced compound screening reliability, and supported translational medicine research.",
     "ChEMBL, RDKit, AutoDock, Python, QSAR modeling, Chemoinformatics tools"),
    
    ("80S Ribosome Docking Project with Psychiatric Drugs", "Aug 2024 - Nov 2024",
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


# 🔹 Education Section with College Images
st.markdown("<h3>🎓 Education</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("GCU.jpg", width=300)  # First college picture
    st.markdown("""
    - **MSc in Bioinformatics (2023-2025)** - Garden City University |84.74%|
    - **BSc in Biotechnology, Biochemistry & Genetics (2020-2023)** - Garden City University |81.7%|  
    """)

with col2:
    st.image("St. Joseph's Indian Composite PU College.png", width=500)  # Second college picture
    st.markdown(""" 
    - **Pre-University education in Science - PCMB (2018-2020)** - St. Joseph's Indian Composite PU College |72.3%|  
    """)

st.divider()


# ✅ Show Certifications
def show_certifications():
    st.header("📜 Certifications")

    certifications = [
        {
            "title": "Gut Check: Exploring Your Microbiome",
            "provider": "University of Colorado Boulder on Coursera",
            "url": "https://coursera.org/share/8d61040ede8f82ce0221e1f5840a85d4"
        },
        {
            "title": "Hands-on Introduction to Linux Commands and Shell Scripting",
            "provider": "IBM on Coursera",
            "url": "https://coursera.org/share/eecb07d0bc27f873aa3aac84c98ed254"
        },
        {
            "title": "Introduction to Small Molecule Drug Discovery & Development",
            "provider": "University of California San Diego on Coursera",
            "url": "https://coursera.org/share/b5971c5f66c00c016f7e2440380b1d03"
        },
        {
            "title": "Finding Hidden Messages in DNA (Bioinformatics I)",
            "provider": "University of California San Diego on Coursera",
            "url": "https://coursera.org/share/6a4d4c29aafb290b3557fec8c73ecbf6"
        },
        {
            "title": "Managing Stress and Time",
            "provider": "University of California, Davis on Coursera",
            "url": "https://coursera.org/share/5f9aa5c6750b886dabf576846c00f438"
        }
    ]

    for cert in certifications:
        st.markdown(f"""
        ✓ **{cert['title']}**  
        _Offered by_ {cert['provider']}  
        📎 [Certificate Link]({cert['url']})
        """)

# ✅ Call the function
show_certifications()


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

# 📄 Resume Section
st.markdown("<h3>📄 Resume</h3>", unsafe_allow_html=True)

import os

resume_path = "SHAKTHI_J_Resume.pdf"  # Make sure this is the correct local file name

if os.path.exists(resume_path):
    with open(resume_path, "rb") as file:
        resume_data = file.read()

    st.download_button(
        label="📥 Download My Resume (PDF)",
        data=resume_data,
        file_name="SHAKTHI_J_Resume.pdf",
        mime="application/pdf"
    )
else:
    st.warning("📂 Resume file not found in local folder.")
    st.markdown("""
    👉 [Click here to view/download from GitHub](https://github.com/Shakthi-J/Shakthi_J_Portfolio/raw/main/SHAKTHI_J_Resume.pdf)
    """, unsafe_allow_html=True)



# Optional Static Contact Info (Below Form)
st.markdown("""
---
**📧 Email:** [shakthipostbox@gmail.com](mailto:shakthipostbox@gmail.com)  
**🔗 LinkedIn:** [linkedin.com/in/shakthij](https://www.linkedin.com/in/shakthij)  
**🌐 GitHub:** [github.com/Shakthi-J](https://github.com/Shakthi-J)  
**📍 Location:** Bengaluru, India
""")

# Footer
st.markdown("**Thanks for Visiting!!**")
