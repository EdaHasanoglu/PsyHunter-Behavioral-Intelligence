import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="PsyHunter Intelligence", page_icon="🛡️", layout="wide")

# --- 2. CSS STYLING (ZERO GRAVITY DARK THEME) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Remove Top Padding */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 1rem !important;
    }
    
    /* Header Adjustment */
    h1 {
        margin-top: 0rem !important;
        padding-top: 0rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Hide Streamlit Default Header */
    header {
        visibility: hidden;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #333;
        padding-top: 2rem !important;
    }
    
    /* Force White Text in Sidebar */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Metric Boxes */
    div[data-testid="stMetricValue"] {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #aaaaaa !important;
    }
    
    /* Custom Report Box */
    .report-box {
        border: 1px solid #333;
        padding: 20px;
        border-radius: 10px;
        background-color: #0a0a0a;
        margin-bottom: 15px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #111;
        color: #00ff41;
        border: 1px solid #00ff41;
        border-radius: 5px;
        height: 50px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ff41;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. RISK DICTIONARY ---
RISK_LIBRARY = {
    "Financial_Fraud": ["money", "debt", "credit", "bank", "bill", "salary", "loan", "crypto", "bitcoin", "broke", "lost", "cash"],
    "Emotional_Crisis": ["hate", "angry", "kill", "die", "suicide", "death", "pain", "cry", "depressed", "lonely", "hopeless"],
    "Workplace_Burnout": ["tired", "exhausted", "quit", "boss", "overtime", "stress", "hate job", "mobbing", "burnout"],
    "High_Risk_Behavior": ["gamble", "bet", "casino", "poker", "drug", "alcohol", "drunk", "illegal", "hack", "steal"]
}

# --- 4. ANALYSIS ENGINE ---
def deep_scan(text):
    if not text: return 0, 0, 0, [], {}
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    text_lower = text.lower()
    
    score = 20 # Baseline Risk
    detected_tags = []
    category_counts = {}

    for category, words in RISK_LIBRARY.items():
        count = 0
        for word in words:
            if word in text_lower:
                count += 1
                # Weighted Scoring
                if category == "Emotional_Crisis": score += 20
                elif category == "High_Risk_Behavior": score += 25
                else: score += 10
        
        if count > 0:
            category_counts[category] = count
            detected_tags.append(f"{category.replace('_', ' ')}")

    # Negative Sentiment Penalty
    if polarity < -0.3: 
        score += 15
        detected_tags.append("Negative Sentiment")

    return min(score, 100), polarity, analysis.sentiment.subjectivity, detected_tags, category_counts

# --- 5. DATA INGESTION ---
def load_tracehunter_data():
    try:
        if os.path.exists("target_profile.json"):
            with open("target_profile.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    except:
        return None

# --- 6. UI LAYOUT ---

with st.sidebar:
    st.title("🛡️ PsyHunter v3.0")
    st.caption("INTEGRATED THREAT INTEL")
    st.markdown("---")
    
    st.subheader("PIPELINE CONTROL")
    if st.button("📥 IMPORT TRACE DATA"):
        data = load_tracehunter_data()
        if data:
            # Fallback for keys
            username = data.get("username") or data.get("target_id") or "Unknown"
            footprint = data.get("digital_footprint", "")
            
            st.session_state['input_text'] = footprint
            st.session_state['target_user'] = username
            st.session_state['run_scan'] = True
            st.success(f"LOADED: {username.upper()}")
        else:
            st.error("DATA FILE MISSING")
            
    st.markdown("---")
    st.markdown("**STATUS:** 🟢 ONLINE")

# Main Dashboard
st.title("👁️ Behavioral Threat Dashboard")
st.markdown(f"TARGET IDENTITY: **{st.session_state.get('target_user', 'WAITING FOR STREAM...').upper()}**")

col1, col2 = st.columns([1.5, 1])

with col1:
    user_text = st.text_area("DIGITAL FOOTPRINT STREAM", 
                            value=st.session_state.get('input_text', ""),
                            height=220, 
                            placeholder="> Waiting for TraceHunter data stream...")
    
    if st.button("🚀 INITIATE ANALYSIS SEQUENCE", type="primary"):
        st.session_state['run_scan'] = True

with col2:
    if st.session_state.get('run_scan') and user_text:
        risk, pol, subj, tags, cats = deep_scan(user_text)
        
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = risk,
            title = {'text': "VULNERABILITY SCORE", 'font': {'color': 'white', 'size': 16}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': "#ff0000" if risk > 70 else "#00ff41"},
                'bgcolor': "#111",
                'borderwidth': 2,
                'bordercolor': "#333",
                'steps': [
                    {'range': [0, 40], 'color': "#0d2b12"},
                    {'range': [40, 75], 'color': "#3d3000"},
                    {'range': [75, 100], 'color': "#3d0000"}]
            }
        ))
        fig.update_layout(height=260, margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
        st.plotly_chart(fig, use_container_width=True)

# Detailed Report
if st.session_state.get('run_scan') and user_text:
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='report-box'>", unsafe_allow_html=True)
        st.subheader("📊 PSYCHOMETRICS")
        st.metric("SENTIMENT", f"{pol:.2f}")
        st.metric("SUBJECTIVITY", f"{subj:.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='report-box'>", unsafe_allow_html=True)
        st.subheader("🚩 THREAT VECTORS")
        if tags:
            for tag in tags:
                st.markdown(f"❌ **{tag}**")
        else:
            st.markdown("✅ CLEAN PROFILE")
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='report-box'>", unsafe_allow_html=True)
        st.subheader("🎯 ACTION PLAN")
        if risk > 70:
            st.error("CRITICAL RISK")
            st.write("Target compromised. Start Protocols.")
        elif risk > 40:
            st.warning("ELEVATED RISK")
            st.write("Monitor financials.")
        else:
            st.success("STABLE")
        st.markdown("</div>", unsafe_allow_html=True)