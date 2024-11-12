# main.py
import streamlit as st
from utils.file_processing import extract_text_from_pdf, load_best_practices
from utils.llm_helpers import risk_classification, perform_rra, security_review

st.title("Tech Spec Analysis with LLMs")

# Load best practices directory
best_practices = load_best_practices("best_practices")

# Step 1: File upload
uploaded_file = st.file_uploader("Upload your tech spec (PDF)", type=["pdf"])

if uploaded_file:
    # Parse content
    parsed_content = extract_text_from_pdf(uploaded_file)
    
    # Analysis results
    with st.spinner("Performing analysis..."):
        risk_classification_result = risk_classification(parsed_content)
        rra_result = perform_rra(parsed_content)
        security_review_result, best_practices_citations = security_review(parsed_content, best_practices)

    # Display consolidated results
    st.header("Consolidated Analysis Report")
    
    st.subheader("1. Risk Classification")
    st.write(risk_classification_result)

    st.subheader("2. Rapid Risk Assessment (RRA)")
    st.write(rra_result)
    st.caption("Metric: Based on Mozilla’s Rapid Risk Assessment guide")

    st.subheader("3. Security Review")
    st.write(security_review_result)

    if best_practices_citations:
        st.subheader("Citations from Best Practices Directory")
        for summary, doc_name in best_practices_citations:
            st.write(f"- **{doc_name}**: {summary}")
