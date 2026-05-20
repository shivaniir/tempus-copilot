import streamlit as st

st.set_page_config(page_title="Tempus Sales Copilot", page_icon="🧬", layout="wide")

st.title("🧬 Tempus Sales Copilot")
st.caption("Empowering field representatives with instant, data-backed pre-meeting insights.")
st.markdown("---")

st.sidebar.header("📁 Data Ingestion Layer")
st.sidebar.info("Upload free-tooling mock datasets to ground the GenAI model context.")

uploaded_market = st.sidebar.file_uploader("Upload Market Intelligence (CSV)", type=["csv"])
uploaded_crm = st.sidebar.file_uploader("Upload CRM Notes (TXT)", type=["txt"])
uploaded_kb = st.sidebar.file_uploader("Upload Knowledge Base (MD)", type=["md"])

st.subheader("👨‍⚕️ Physician Briefing Generator")

physician_options = [
    "Select a physician...",
    "Dr. Amanda Smith (Breast Cancer)",
    "Dr. Robert Chen (Colorectal Cancer)",
    "Dr. Sarah Jenkins (Lung Cancer - NSCLC)",
    "Dr. Michael Patel (General Oncology)"
]

selected_physician = st.selectbox("Choose a target provider for your upcoming meeting:", physician_options)

if selected_physician != "Select a physician...":
    name = selected_physician.split(" (")[0]
    st.markdown(f"### 📋 Copilot Briefing: **{name}**")
    
    if st.button("Generate Actionable Insights"):
        if "Sarah Jenkins" in selected_physician:
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Ranked Impact Score", value="98/100", delta="Priority Alpha Target")
                st.markdown("""
                **Why Prioritize:**
                * High potential patient volume (180/year).
                * Deeply academic oncologist who values comprehensive profiling.
                * Facing structural 'tissue walls'—perfect candidate for Tempus xF.
                """)
            with col2:
                st.error("⚠️ Active CRM Friction Point")
                st.markdown("""
                **CRM Note:** Frequently encounters insufficient tissue samples during solid tumor biopsies, halting traditional hotspot sequencing.
                """)
                
            st.markdown("---")
            tab1, tab2 = st.tabs(["🎯 Objection Handler", "🗣️ 30-Second Meeting Script"])
            
            with tab1:
                st.subheader("Data-Backed Objection Handler")
                st.info("""
                *"Dr. Jenkins, I understand that running into a tissue wall with traditional panels stalls patient care. That’s exactly why we developed the **Tempus xF Liquid Biopsy**. It requires only a simple peripheral blood draw and provides a comprehensive 105-gene assay with an industry-leading turnaround time of **6-8 calendar days** from lab receipt, completely bypassing tissue scarcity constraints."*
                """)
                st.caption("Source Metrics: tempus_kb.md (Tempus Oncology Portfolio)")
                
            with tab2:
                st.subheader("The 30-Second Elevator Pitch")
                st.success("""
                *"Hi Dr. Jenkins, I’ve been following your recent publications on NSCLC. I know tissue scarcity frequently limits your ability to run traditional sequencing. Tempus is radically changing that. Our xF Liquid Biopsy panel delivers a 105-gene profiling assay from a basic blood draw in just 6 to 8 days. Plus, with our Tempus ONE assistant, you can text or query clinical trial matching right from the clinic floor. I'd love to schedule 5 minutes to show you how this can expand options for your advanced lung patients."*
                """)
        else:
            st.warning("Prototype Demo Mode: Select 'Dr. Sarah Jenkins' to view the complete integrated data synthesis walkthrough.")