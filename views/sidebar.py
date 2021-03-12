import streamlit as st


def render_option():
    st.sidebar.title("Martingale Analysis")
    option = st.sidebar.selectbox(
        "Page Navigation:",
        (
            "Home",
            "Condition 1: Spin Until Bankrupt",
            "Condition 2: Fixed Number of Spins",
            "Condition 3: X-or-nothing",
            "Conclusions",
        ),
    )
    return option


house_odds = 0.4736842
true_flip_odds = 0.5
odds = house_odds


def render_odds():
    odds = st.sidebar.selectbox(
        "Choose a Win Probability:", ("House Odds (47.3%)", "True Flip (50/50)")
    )
    if odds == "House Odds (47.3%)":
        p_win = house_odds
    elif odds == "True Flip (50/50)":
        p_win = true_flip_odds
    return p_win


def render_c1_sidebar():
    trials = st.sidebar.slider(
        "1. Select a # of trials to repeat the experiment:", 50, 500, 100, step=10
    )
    bankroll = st.sidebar.slider(
        "2. Select a starting bankroll" " for each trial:", 100, 10000, 1000, step=100
    )
    startBet = st.sidebar.slider(
        "3. Select a starting wager" " for each martingale cycle:",
        5,
        int(bankroll / 10),
        10,
        step=5,
    )
    return trials, bankroll, startBet


def render_c2_sidebar():
    trials = st.sidebar.slider(
        "1. Select a # of trials to repeat the experiment:", 50, 500, 100, step=10
    )
    bankroll = st.sidebar.slider(
        "2. Select a starting bankroll" " for each trial:", 100, 10000, 1000, step=100
    )
    startBet = st.sidebar.slider(
        "3. Select a starting wager" " for each martingale cycle:",
        5,
        int(bankroll / 10),
        10,
        step=5,
    )
    numSpins = st.sidebar.slider(
        "4. Select a number of" " spins for each trial:", 100, 10000, 100, step=10
    )
    return trials, bankroll, startBet, numSpins


def render_c3_sidebar():
    trials = st.sidebar.slider(
        "1. Select a # of trials to repeat the experiment:", 50, 500, 100, step=10
    )
    bankroll = st.sidebar.slider(
        "2. Select a starting bankroll" " for each trial:", 100, 10000, 1000, step=100
    )
    startBet = st.sidebar.slider(
        "3. Select a starting wager" " for each martingale cycle:",
        5,
        int(bankroll / 10),
        10,
        step=5,
    )
    multGoal = st.sidebar.slider(
        "4. Select a bankroll multiplier" " as a goal for each trial:", 2, 10, 2, step=1
    )
    return trials, bankroll, startBet, multGoal
