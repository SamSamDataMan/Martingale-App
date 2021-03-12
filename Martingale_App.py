from engine import spin_til_bust, x_num_spins, x_or_nothing
from views.home import render_home
from views.sidebar import (
    render_option,
    render_odds,
    render_c1_sidebar,
    render_c2_sidebar,
    render_c3_sidebar,
)
from views.cond1 import cond1_header, render_cond1
from views.cond2 import cond2_header, render_cond2
from views.cond3 import cond3_header, render_cond3
from views.conclusions import render_conc


option = render_option()

if (
    option == "Condition 1: Spin Until Bankrupt"
    or option == "Condition 2: Fixed Number of Spins"
    or option == "Condition 3: X-or-nothing"
):
    p_win = render_odds()

if option == "Home":
    render_home()

elif option == "Condition 1: Spin Until Bankrupt":
    left, right = cond1_header()
    print('Here1')
    trials, bankroll, startBet = render_c1_sidebar()
    print('Here2')
    results = spin_til_bust(trials, bankroll, startBet, p_win, display_container=left)
    print('Here3')
    render_cond1(left, right, trials, results)
    print('Here4')

elif option == "Condition 2: Fixed Number of Spins":
    left, right = cond2_header()
    trials, bankroll, startBet, numSpins = render_c2_sidebar()
    results = x_num_spins(
        trials, bankroll, startBet, p_win, numSpins, display_container=left
    )
    render_cond2(left, right, trials, results, bankroll)

elif option == "Condition 3: X-or-nothing":
    left, right = cond3_header()
    trials, bankroll, startBet, multGoal = render_c3_sidebar()
    results = x_or_nothing(
        trials, bankroll, startBet, p_win, multGoal, display_container=left
    )
    render_cond3(left, right, trials, results, bankroll)

elif option == "Conclusions":
    render_conc()
