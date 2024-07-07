import streamlit as st
import pandas as pd
data = pd.read_csv("deliveries.csv")
data1 = pd.read_csv("matches.csv")


def trophies_tally(data):
    # Code to display trophies tally
    st.header("Trophies Tally")
    # Implement the logic to display the trophies tally
    pass

def overall_analysis(data):
    # Code to display overall analysis
    st.header("Overall Analysis")
    # Implement the logic to display the overall analysis
    pass

def franchise_analysis(data):
    # Code to display franchise analysis
    st.header("Franchise Analysis")

    # Get unique franchises/teams
    franchises = data['team1'].unique()
    franchises = sorted(franchises)

    # Sidebar - Select franchise
    selected_franchise = st.sidebar.selectbox('Select Franchise', franchises)

    # Filter the data based on the selected franchise
    franchise_df = data[(data['team1'] == selected_franchise) | (data['team2'] == selected_franchise)]

    # Display the matches played by the selected franchise
    st.subheader(f"Matches played by {selected_franchise}")
    st.dataframe(franchise_df)

    # Implement additional analysis for the selected franchise
    # e.g., win-loss ratio, top players, etc.

def player_wise_analysis(data):
    # Code to display player-wise analysis
    st.header("Player Wise analysis")
    # Implement the logic to display the player-wise analysis
    pass


def year_wise_matches_wins(data1,team):
    new_data = data1[(data1['winner'] == team)]
    final_data = new_data.groupby('season').count()['winner'].reset_index()
    return final_data
    
def count_sixes(data, team):
    new_data = data[(data['batting_team'] == team) & (data['batsman_runs'] == 6)]
    return new_data.shape[0]

def count_fours(data,team):
    new_data_for_4 = data[(data['batting_team'] == team) & (data['batsman_runs'] == 4)]
    return new_data_for_4.shape[0]

def count_wickets(data,team):
    new_data_for_wickets = data[(data['batting_team'] == team) & (data['is_wicket'] == 1)]
    return new_data_for_wickets.shape[0]