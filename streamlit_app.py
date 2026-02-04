import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="2026 NET Team Sheet Plus", layout="wide")

# Custom CSS for that "Eye-Friendly" look
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        margin-bottom: 10px;
    }
    .win-pill {
        background-color: #d4edda;
        color: #155724;
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: bold;
    }
    .loss-pill {
        background-color: #f8d7da;
        color: #721c24;
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA ---
team_name = "Kansas Jayhawks"
net_rank = 4
record = "22-4 (11-3 Big 12)"

# Mock Game Data for Quadrant 1
q1_data = {
    "Date": ["Jan 15", "Jan 22", "Feb 05", "Feb 12"],
    "Opponent": ["@ Houston", "vs Baylor", "vs Iowa St", "@ Arizona"],
    "Loc": ["AWAY", "HOME", "NEUTRAL", "AWAY"],
    "Opp NET": [1, 12, 10, 8],
    "Result": ["L", "W", "W", "W"],
    "Score": ["68-75", "82-74", "70-65", "77-72"]
}
df_q1 = pd.DataFrame(q1_data)

# --- UI LAYOUT ---

# 1. Header Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://via.placeholder.com/150", width=120) # Replace with actual logo URL
with col2:
    st.title(f"{team_name}")
    st.subheader(f"NET Rank: #{net_rank} | {record}")

st.divider()

# 2. Top-Level Metrics (Resume vs Quality)
col_res, col_qual = st.columns(2)

with col_res:
    st.markdown("### 📋 Resume Metrics")
    c1, c2, c3 = st.columns(3)
    c1.metric("SOR", "3")
    c2.metric("KPI", "5")
    c3.metric("WAB", "+4.2")

with col_qual:
    st.markdown("### 📊 Predictive Metrics")
    c1, c2, c3 = st.columns(3)
    c1.metric("KenPom", "6")
    c2.metric("BPI", "8")
    c3.metric("T-Rank", "7")

st.divider()

# 3. Quadrant Breakdown
st.markdown("## Quadrant 1 (High Quality)")

# Using Streamlit's new column_config for better visuals
st.dataframe(
    df_q1,
    column_config={
        "Result": st.column_config.TextColumn(
            "Result",
            help="Game Outcome",
            width="small",
        ),
        "Opp NET": st.column_config.NumberColumn(
            "Opp NET",
            format="#%d",
        ),
    },
    hide_index=True,
    use_container_width=True
)

# 4. Quadrant Summary Cards
st.markdown("### Resume Summary")
q_cols = st.columns(4)
q_cols[0].info("**Q1:** 8-3")
q_cols[1].success("**Q2:** 6-1")
q_cols[2].success("**Q3:** 4-0")
q_cols[3].success("**Q4:** 4-0")
