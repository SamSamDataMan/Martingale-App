import streamlit as st
from engine import spin_til_bust, x_num_spins, x_or_nothing
from home import render_home
from sidebar import (
    render_option,
    render_odds,
    render_c1_sidebar,
    render_c2_sidebar,
    render_c3_sidebar,
)
from cond1 import render_cond1
from cond2 import render_cond2
from cond3 import render_cond3
from conclusions import render_conc

house_odds = 0.4736842
true_flip_odds = 0.5
odds = house_odds

option = render_option()

if (
    option == "Condition 1: Spin Until Bankrupt"
    or option == "Condition 2: Fixed Number of Spins"
    or option == "Condition 3: X-or-nothing"
):
    odds = render_odds()

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
    trials, bankroll, startBet = render_c1_sidebar()
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
    trials, bankroll, startBet, numSpins = render_c2_sidebar()
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
    trials, bankroll, startBet, multGoal = render_c3_sidebar()
    results = x_or_nothing(
        trials, bankroll, startBet, p_win, multGoal, display_container=left
    )
    render_cond3(left, right, trials, results, bankroll)

elif option == "Conclusions":
    render_conc()
