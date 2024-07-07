import streamlit as st
import pandas as pd
import preprocessor  
import plotly.express as px
import helper
import plotly.graph_objects as go


data = pd.read_csv("deliveries.csv")
data1 = pd.read_csv("matches.csv")
player_data = pd.read_csv("player_stat.csv")


st.sidebar.header("IPL Analysis")
st.sidebar.image("main.png", use_column_width=True)

selected_action = st.sidebar.radio(
    'Select an action',
    ('Trophies Tally', 'Game Performances','Overall Analysis', 'Franchise Analysis', 'Player Wise analysis')
)

if selected_action == 'Trophies Tally':
    st.header('Trophies Tally')

    df = preprocessor.load_trophies_data('trophies_count.xlsx')
    st.table(df)











if selected_action == 'Game Performances':
    st.header('Game Performances')
    st.subheader("Top Run-Scorers")

# Sort the players by total runs in descending order
    top_run_scorers = player_data.sort_values('runs', ascending=False).head(10)

# Define the color palette for the players
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
    x=top_run_scorers['player'],
    y=top_run_scorers['runs'],
    text=top_run_scorers['runs'].astype(int),
    textposition='auto',
    marker_color=[colors[i] for i, _ in enumerate(top_run_scorers['player'])]
)])

# Customize the chart layout
    fig.update_layout(
    title='Top Run-Scorers in IPL',
    xaxis_title='Player',
    yaxis_title='Runs',
    bargap=0.1
)

# Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Wicket-Takers")

# Sort the players by total wickets in descending order
    top_wicket_takers = player_data.sort_values('wickets', ascending=False).head(10)

# Define the color palette for the players
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
    x=top_wicket_takers['player'],
    y=top_wicket_takers['wickets'],
    text=top_wicket_takers['wickets'].astype(int),
    textposition='auto',
    marker_color=[colors[i] for i, _ in enumerate(top_wicket_takers['player'])]
)])

# Customize the chart layout
    fig.update_layout(
    title='Top Wicket-Takers in IPL',
    xaxis_title='Player',
    yaxis_title='Wickets',
    bargap=0.1
)

# Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)



    st.subheader("All-Rounders")

    # Create the scatter plot
    fig = go.Figure(data=go.Scatter(
        x=player_data['batting_avg'],
        y=player_data['bowling_avg'],
        mode='markers',
        text=player_data['player'],
        marker=dict(
            size=10,
            color=player_data['batting_avg'] * player_data['bowling_avg'],  # Use a combined metric to size the markers
            colorscale='Viridis',
            showscale=True
        )
    ))

    # Customize the chart layout
    fig.update_layout(
        title='All-Rounders in IPL',
        xaxis_title='Batting Average',
        yaxis_title='Bowling Average',
        width=800,
        height=600
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)
































    player_data['boundary_percent'] = (player_data['boundaries'] / player_data['runs']) * 100

    # Sort the players by boundary percentage in descending order
    sorted_boundary_percent = player_data.sort_values('boundary_percent', ascending=False)

    # Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
        x=sorted_boundary_percent['player'],
        y=sorted_boundary_percent['boundary_percent'],
        text=sorted_boundary_percent['boundary_percent'].apply(lambda x: f"{x:.2f}%"),
        textposition='auto'
    )])

    # Customize the chart layout
    fig.update_layout(
        title='Boundary Percentage for Each Player',
        xaxis_title='Player',
        yaxis_title='Boundary Percentage (%)',
        bargap=0.1
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


    st.subheader("Most Catches")

# Assuming the catches data is in a column named 'catches'
    top_catches = player_data.sort_values('catches', ascending=False).head(10)

# Define the color palette for the players
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
    x=top_catches['player'],
    y=top_catches['catches'],
    text=top_catches['catches'].astype(int),
    textposition='auto',
    marker_color=[colors[i] for i, _ in enumerate(top_catches['player'])]
)])

# Customize the chart layout
    fig.update_layout(
    title='Most Catches in IPL',
    xaxis_title='Player',
    yaxis_title='Catches',
    bargap=0.1
)

# Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)














    st.subheader("Most Stumpings")

# Assuming the stumpings data is in a column named 'stumpings'
    top_stumpings = player_data.sort_values('stumpings', ascending=False).head(10)

# Define the color palette for the players
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
    x=top_stumpings['player'],
    y=top_stumpings['stumpings'],
    text=top_stumpings['stumpings'].astype(int),
    textposition='auto',
    marker_color=[colors[i] for i, _ in enumerate(top_stumpings['player'])]
)])

# Customize the chart layout
    fig.update_layout(
    title='Most Stumpings in IPL',
    xaxis_title='Player',
    yaxis_title='Stumpings',
    bargap=0.1
)

# Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)



































# Display the Overall Analysis if selected
if selected_action == 'Overall Analysis':
    seasons = data1['season'].unique()
    teams = data1['team1'].nunique()
    data1['season'] = data1['season'].replace({'2007/08':2008})
    data1['season'] = data1['season'].replace({'2009/10':2010})
    data1['season'] = data1['season'].replace({'2020/21':2020})
    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)  # Use columns instead of beta_columns

    with col1:
        st.header("Total Seasons")
        st.title(17)

    with col2:
        st.header("Teams Participated")
        st.title(teams)

    with col3:
        st.header("Total Matches played")
        st.title(1095)
    
    col1, col2, col3 = st.columns(3)
    batsmans = data['batter'].nunique()
    bowlers = data['bowler'].nunique()
    total_players =  batsmans + bowlers
    with col1:
        st.header("Total Bowlers ")
        st.title(bowlers)
        
    with col2:
        st.header("Total Batsmans")
        st.title(batsmans)
    with col3:
        st.header("Total Players")
        st.title(total_players)


    matches_per_season = data1.groupby('season').size().reset_index(name='matches')

# Create the line chart
    st.title("Matches Played Per Season")
    fig = px.bar(matches_per_season, x='season', y='matches', title='Matches per Season')
    fig.update_layout(
    xaxis_title="Number of Matches",
    yaxis_title="Season",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)

# Display the chart
    st.plotly_chart(fig)



    matches_per_city = data1.groupby('city').size().reset_index(name='matches')
    top_cities = matches_per_city.nlargest(10, 'matches')

# Create the pie chart
    fig = px.pie(top_cities, values='matches', names='city', title='Top 10 Cities by Matches')

# Customize the layout
    fig.update_layout(
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="RebeccaPurple"
    )
)
    st.plotly_chart(fig)
     



    player_of_match_counts = data1['player_of_match'].value_counts().reset_index()
    player_of_match_counts.columns = ['player', 'count']

# Sort the players by the number of "Player of the Match" awards
    top_players = player_of_match_counts.sort_values('count', ascending=False).head(25)

#    Add a column for the team the player was playing for
    # top_players['team'] = top_players['player'].map(lambda x: data1.loc[data1['player_of_match'] == x, 'winner'].iloc[0])

# Display the top 25 players in a table
    st.subheader("Top 25 Players by 'Player of the Match' Awards")
    st.table(top_players)








































# Additional sections can be added similarly...
if selected_action == 'Franchise Analysis':
    st.sidebar.header('Franchise Analysis')
    st.title('Matches Win Over Years')
    team_lists = data1['team1'].unique().tolist()
    team_lists.sort()
    selected_team = st.sidebar.selectbox('Select a Franchiese ', team_lists)
    team_data = helper.year_wise_matches_wins(data1,selected_team) 
    
    fig = px.line(team_data, x="season", y='winner')

    st.plotly_chart(fig)
    
    sixes_count = helper.count_sixes(data, selected_team)
    
    st.title(f"Total Sixes Hit by {selected_team}: {sixes_count}")
     
    fours_count = helper.count_fours(data, selected_team)
    st.title(f"Total Fours Hit by {selected_team}: {fours_count}")

    wickets_counts = helper.count_wickets(data,selected_team)
    st.title(f"Total Wickets Taken By {selected_team}: {wickets_counts}")

    winning_teams = data1[(data1['winner'] == data1['team1']) & (data1['team1'] == selected_team)]
    player_counts = winning_teams.groupby('player_of_match').size().reset_index(name='count')
    top_players = player_counts.nlargest(5, 'count')

    st.title(f"Top 3 Players of {selected_team}")
    st.table(top_players)









player_names = player_data['player'].unique()

if selected_action == 'Player Wise analysis':
    st.header('Player Wise Analysis')

    # Add a search bar with suggestions
    selected_player = st.selectbox("Search for a player", player_names)

    # Filter the data based on the selected player
    player_data_filtered = player_data[player_data['player'] == selected_player]

    # Display the player's data in a card format
    if not player_data_filtered.empty:
        st.subheader(f"Data for {selected_player}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Runs", int(player_data_filtered['runs'].values[0]))
            st.metric("Boundaries", int(player_data_filtered['boundaries'].values[0]))
            st.metric("Batting Average", player_data_filtered['batting_avg'].values[0])
            st.metric("Strike Rate", player_data_filtered['batting_strike_rate'].values[0])
        
        with col2:
            st.metric("Wickets", int(player_data_filtered['wickets'].values[0]))
            st.metric("Bowling Average", player_data_filtered['bowling_avg'].values[0])
            st.metric("Economy", player_data_filtered['bowling_economy'].values[0])
            st.metric("Catches", int(player_data_filtered['catches'].values[0]))

        # Batting Analysis - Batting Average vs Strike Rate
        st.subheader(f"{selected_player} - Batting Analysis")

        # Create the scatter plot
     



















    selected_players = st.multiselect("Select players to compare", player_names, max_selections=3)

    if selected_players:
        st.subheader("Player Comparison")

        # Filter the data for the selected players
        player_data_filtered = player_data[player_data['player'].isin(selected_players)]

        # Define the color palette for the players
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

        # Create charts for the player stats
        col1, col2 = st.columns(2)

        with col1:
            # Runs
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['runs'],
                text=player_data_filtered['runs'].astype(int),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Runs Scored',
                xaxis_title='Player',
                yaxis_title='Runs'
            )
            st.plotly_chart(fig)

            # Wickets
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['wickets'],
                text=player_data_filtered['wickets'].astype(int),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Wickets Taken',
                xaxis_title='Player',
                yaxis_title='Wickets'
            )
            st.plotly_chart(fig)

        with col2:
            # Batting Average
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['batting_avg'],
                text=player_data_filtered['batting_avg'].apply(lambda x: f"{x:.2f}"),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Batting Average',
                xaxis_title='Player',
                yaxis_title='Average'
            )
            st.plotly_chart(fig)

            # Bowling Average
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['bowling_avg'],
                text=player_data_filtered['bowling_avg'].apply(lambda x: f"{x:.2f}"),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Bowling Average',
                xaxis_title='Player',
                yaxis_title='Average'
            )
            st.plotly_chart(fig)

        col3, col4 = st.columns(2)

        with col3:
            # Batting Strike Rate
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['batting_strike_rate'],
                text=player_data_filtered['batting_strike_rate'].apply(lambda x: f"{x:.2f}"),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Batting Strike Rate',
                xaxis_title='Player',
                yaxis_title='Strike Rate'
            )
            st.plotly_chart(fig)

            # Bowling Economy
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['bowling_economy'],
                text=player_data_filtered['bowling_economy'].apply(lambda x: f"{x:.2f}"),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Bowling Economy',
                xaxis_title='Player',
                yaxis_title='Economy'
            )
            st.plotly_chart(fig)

        with col4:
            # Catches
            fig = go.Figure(data=[go.Bar(
                x=player_data_filtered['player'],
                y=player_data_filtered['catches'],
                text=player_data_filtered['catches'].astype(int),
                textposition='inside',
                marker_color=[colors[i] for i, _ in enumerate(player_data_filtered['player'])]
            )])
            fig.update_layout(
                title='Catches Taken',
                xaxis_title='Player',
                yaxis_title='Catches'
            )
            st.plotly_chart(fig)

        # Display the color legend
       
    else:
        st.write("Please select at least one player to compare.")