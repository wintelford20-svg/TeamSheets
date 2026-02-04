import streamlit as st
import pandas as pd

# --- LOAD DATA ---
@st.cache_data # This keeps the app fast by not reloading files on every click
def load_data():
    teams = pd.read_csv("teams_summary.csv")
    games = pd.read_csv("game_logs.csv")
    return teams, games

try:
    df_teams, df_games = load_data()
except FileNotFoundError:
    st.error("Please ensure teams_summary.csv and game_logs.csv are in the same folder.")
    st.stop()

# --- SIDEBAR SELECTOR ---
st.sidebar.header("Navigation")
selected_team = st.sidebar.selectbox("Select a Team", df_teams["Team"].unique())

# Filter data for the selected team
team_stats = df_teams[df_teams["Team"] == selected_team].iloc[0]
team_games = df_games[df_games["Team"] == selected_team]

# --- UI LAYOUT ---
st.title(f"🏀 {selected_team} Team Sheet")
st.subheader(f"NET Rank: #{team_stats['NET']} | Overall: {team_stats['Record']}")

# 1. Metric Cards
col_res, col_qual = st.columns(2)
with col_res:
    st.markdown("#### 📋 Resume")
    c1, c2, c3 = st.columns(3)
    c1.metric("SOR", team_stats['SOR'])
    c2.metric("KPI", team_stats['KPI'])
    c3.metric("WAB", team_stats['WAB'])

with col_qual:
    st.markdown("#### 📊 Quality")
    c1, c2, c3 = st.columns(3)
    c1.metric("KenPom", team_stats['KenPom'])
    c2.metric("BPI", team_stats['BPI'])
    c3.metric("T-Rank", team_stats['T-Rank'])

st.divider()

# 2. Quadrant Selector
q_choice = st.radio("View Games by Quadrant", ["Q1", "Q2", "Q3", "Q4"], horizontal=True)
filtered_games = team_games[team_games["Quadrant"] == q_choice]

# 3. Dynamic Game Table
st.markdown(f"### {q_choice} Games")
if not filtered_games.empty:
    st.dataframe(
        filtered_games[["Date", "Opponent", "Loc", "Opp_NET", "Result", "Score"]],
        hide_index=True,
        use_container_width=True
    )
else:
    st.write(f"No {q_choice} games played yet.")

# 4. Footer Summary
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Q1:** {team_stats['Q1_Rec']}")
st.sidebar.markdown(f"**Q2:** {team_stats['Q2_Rec']}")
st.sidebar.markdown(f"**Q3:** {team_stats['Q3_Rec']}")
st.sidebar.markdown(f"**Q4:** {team_stats['Q4_Rec']}")
