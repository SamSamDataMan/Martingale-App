import streamlit as st
from engine import spin_til_bust, x_num_spins, x_or_nothing
from home import render_home
from cond1 import render_cond1
from cond2 import render_cond2
from cond3 import render_cond3
from conclusions import render_conc

house_odds = 0.4736842
true_flip_odds = 0.5
odds = house_odds


# Sidebar - User Inputs
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

if (
    option == "Condition 1: Spin Until Bankrupt"
    or option == "Condition 2: Fixed Number of Spins"
    or option == "Condition 3: X-or-nothing"
):
    odds = st.sidebar.selectbox(
        "Choose a Win Probability:", ("House Odds (47.3%)", "True Flip (50/50)")
    )

if odds == "House Odds (47.3%)":
    p_win = house_odds
elif odds == "True Flip (50/50)":
    p_win = true_flip_odds

if option == "Home":
    render_home()

elif option == "Condition 1: Spin Until Bankrupt":
    st.header("Condition 1: Spin Until Bankrupt")
    st.text(
        "In this condition we allow each trial to continue until the entire bankroll is lost.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins Until Bankrupt")
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
    # Create first chart
    results = spin_til_bust(trials, bankroll, startBet, p_win, display_container=left)
    render_cond1(left, right, trials, results)

elif option == "Condition 2: Fixed Number of Spins":
    st.header("Condition 2: Fixed Number of Spins")
    st.text(
        "In this condition we allow each trial to continue for a fixed number of spins or until the\n"
        "entire bankroll is lost.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Fixed Number of Spins")
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
        "4. Select a number of" " spins for each trial:", 10, 10000, 100, step=10
    )
    results = x_num_spins(
        trials, bankroll, startBet, p_win, numSpins, display_container=left
    )
    render_cond2(left, right, trials, results, bankroll)

elif option == "Condition 3: X-or-nothing":
    st.header("Condition 3: Multiplier Goal")
    st.text(
        "In this condition we allow each trial to continue\n"
        "until the entire bankroll is lost or a multiplier goal is met.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins To Goal or Bankrupt")
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
    results = x_or_nothing(
        trials, bankroll, startBet, p_win, multGoal, display_container=left
    )
    render_cond3(left, right, trials, results, bankroll)

    # RESUME HERE
elif option == "Conclusions":
    render_conc()
