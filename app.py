import streamlit as st

st.set_page_config(page_title="Tempus Sales Copilot", page_icon="🧬", layout="wide")

st.title("🧬 Tempus Sales Copilot")
st.caption("Empowering field representatives with instant, data-backed pre-meeting insights.")
st.markdown("---")

# Sidebar Data Ingestion Layer
st.sidebar.header("📁 Data Ingestion Layer")
st.sidebar.info("Upload free-tooling mock datasets to ground the GenAI model context.")

uploaded_market = st.sidebar.file_uploader("Upload Market Intelligence (CSV)", type=["csv"])
uploaded_crm = st.sidebar.file_uploader("Upload CRM Notes (TXT)", type=["txt"])
uploaded_kb = st.sidebar.file_uploader("Upload Knowledge Base (MD)", type=["md"])

st.subheader("👨‍⚕️ Physician Briefing Generator")

# Comprehensive dataset mapping for all 5 mock providers
physician_data = {
    "Dr. Amanda Smith (Breast Cancer)": {
        "score": "92/100",
        "tag": "High-Volume Target",
        "why": "* Est. Patient Volume: 140/year.\n* Highly interested in clinical trial matching speed.\n* Currently uses standard in-house IHC testing.",
        "friction": "**CRM Note:** Complained that genomic test turnaround times took too long last quarter (4 weeks), delaying therapy choices.",
        "objection": "*\"Dr. Smith, I hear you loud and clear—waiting 4 weeks for genomic insights while a patient waits for therapy is completely unacceptable. That is exactly why we optimized the **Tempus xT panel**. By pairing targeted DNA sequencing with Whole Transcriptome RNA sequencing, we deliver comprehensive profiles with an industry-leading turnaround time of **9-11 calendar days** from receipt, cutting your historic wait time in half.\"*",
        "script": "*\"Hi Dr. Smith, I know matching your breast cancer patients to clinical trials quickly is a top priority, but long turnaround times have held you back. Tempus xT completely solves that by delivering full DNA and RNA co-amplification profiling in just 9 to 11 calendar days. I'd love to drop off a 2-page validation study showing how our speed can help you confidently select target therapies sooner.\"*"
    },
    "Dr. Robert Chen (Colorectal Cancer)": {
        "score": "88/100",
        "tag": "Growth Account",
        "why": "* Est. Patient Volume: 95/year.\n* Frequently encounters tissue sample scarcity.\n* Currently heavily reliant on Competitor X.",
        "friction": "**CRM Note:** Mentioned at a recent conference that tissue sample scarcity often prevents successful sequencing for his advanced colorectal patients.",
        "objection": "*\"Dr. Chen, hitting a 'tissue wall' with traditional panels shouldn't lock your advanced colorectal patients out of comprehensive profiling. The **Tempus xF Liquid Biopsy** requires only a simple peripheral blood draw (2 tubes) and evaluates a 105-gene cfDNA assay, bypassing tissue scarcity completely while delivering results in **6-8 calendar days**.\"*",
        "script": "*\"Hi Dr. Chen, I remember you mentioning the frustration of tissue scarcity preventing successful sequencing for your colorectal cases. Tempus has a direct solution: our xF Liquid Biopsy. It yields a comprehensive 105-gene profile from a basic blood draw in just 6 to 8 days. Can we look at 2 or 3 of your current patients who couldn't get standard tissue results to see if xF is a fit?\"*"
    },
    "Dr. Sarah Jenkins (Lung Cancer - NSCLC)": {
        "score": "98/100",
        "tag": "Priority Alpha Target",
        "why": "* Est. Patient Volume: 180/year.\n* Deeply academic oncologist who publishes frequently.\n* Demands comprehensive profiling (CGP) over small hotspot panels.",
        "friction": "**CRM Note:** Strictly requires comprehensive genomic profiling rather than small hotspots, but runs into tissue walls where biopsy samples are insufficient.",
        "objection": "*\"Dr. Jenkins, I understand that running into tissue scarcity with traditional panels stalls patient care. That’s exactly why we developed the **Tempus xF Liquid Biopsy**. It provides a comprehensive 105-gene assay with an industry-leading turnaround time of **6-8 calendar days** from lab receipt, completely bypassing tissue sample limitations while maintaining the clinical depth you require.\"*",
        "script": "*\"Hi Dr. Jenkins, I’ve been following your recent publications on NSCLC. I know tissue scarcity frequently limits your ability to run traditional sequencing. Tempus is radically changing that. Our xF Liquid Biopsy panel delivers a 105-gene profiling assay from a basic blood draw in just 6 to 8 days. Plus, with our Tempus ONE assistant, you can text or query clinical trial matching right from the clinic floor. I'd love to schedule 5 minutes to show you how this can expand options for your advanced lung patients.\"*"
    },
    "Dr. Michael Patel (General Oncology)": {
        "score": "75/100",
        "tag": "Nurture Account",
        "why": "* Est. Patient Volume: 60/year.\n* Overwhelmed by changing territories and new drug approvals.\n* Needs concise, bite-sized clinical evidence to change habits.",
        "friction": "**CRM Note:** Overwhelmed by industry noise and changing logistics. Needs concise, bite-sized clinical evidence on 'Why Tempus, Why Now?' to disrupt routine habits.",
        "objection": "*\"Dr. Patel, keeping up with rapid new drug approvals shouldn't add to your daily cognitive load. Tempus streamlines this by integrating **Tempus ONE** right onto the clinic floor. It’s a voice and text-activated assistant that lets you instantly query test results, structural variants, and real-time clinical trial matching options directly between patient visits.\"*",
        "script": "*\"Hi Dr. Patel, I know how overwhelming it is to track the constant stream of new targeted drug approvals alongside shifting territory changes. Tempus is built to simplify your workflow. Beyond our rapid 9-11 day xT genomic testing, we equip your clinic with Tempus ONE—a voice assistant that lets you text or ask for trial matches right on the floor. I'd love to bring you a coffee next Tuesday and show you a 60-second demo of how it saves time.\"*"
    }
}

selected_physician = st.selectbox("Choose a target provider for your upcoming meeting:", ["Select a physician..."] + list(physician_data.keys()))

if selected_physician != "Select a physician...":
    name = selected_physician.split(" (")[0]
    data = physician_data[selected_physician]
    
    st.markdown(f"### 📋 Copilot Briefing: **{name}**")
    
    if st.button("Generate Actionable Insights"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Ranked Impact Score", value=data["score"], delta=data["tag"])
            st.markdown("**Why Prioritize:**")
            st.markdown(data["why"])
        with col2:
            st.error("⚠️ Active CRM Friction Point")
            st.markdown(data["friction"])
            
        st.markdown("---")
        tab1, tab2 = st.tabs(["🎯 Objection Handler", "🗣️ 30-Second Meeting Script"])
        
        with tab1:
            st.subheader("Data-Backed Objection Handler")
            st.info(data["objection"])
            st.caption("Source Metrics: tempus_kb.md (Tempus Oncology Portfolio)")
            
        with tab2:
            st.subheader("The 30-Second Elevator Pitch")
            st.success(data["script"])
