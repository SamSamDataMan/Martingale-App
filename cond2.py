import streamlit as st
import matplotlib.pyplot as plt


def cond2_header():
    st.header("Condition 2: Fixed Number of Spins")
    st.text(
        "In this condition we allow each trial to continue for a fixed number of spins or until the\n"
        "entire bankroll is lost.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Fixed Number of Spins")
    return left, right


def render_cond2(left, right, trials, results, bankroll):
    winners = [i for i in results if i[-1] > 0]
    losers = [i for i in results if i[-1] < 0]
    bankrupt = [i for i in results if i[-1] == -1 * bankroll]
    winner_results = [i[-1] for i in winners]
    loser_results = [i[-1] for i in losers]
    total_won = sum(winner_results)
    total_lost = sum(loser_results)
    x = ["Winners", "Losers", "Bankrupt"]
    y = [len(winners), len(losers) - len(bankrupt), len(bankrupt)]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=["green", "yellow", "red"])
    right.subheader("Proportion of Winners and Losers")
    plt.title("Figure 2: Proportion of Winners and Losers")
    right.pyplot(fig)
    st.header("Results:")
    if len(winners) != 0:
        st.text(
            "The "
            + str(len(winners))
            + " winning trials won a total of $"
            + str(total_won)
            + " or $"
            + str(round(total_won / len(winners), 2))
            + " per winning trial.\n"
            "The "
            + str(len(losers))
            + " losing trials lost a total of $"
            + str(total_lost)
            + " or $"
            + str(round(total_lost / len(losers), 2))
            + " per losing trial."
        )
    else:
        st.text("There were no winning trials in this experiment.")
    st.text(
        "The total return of all trials in this experiment was $"
        + str(total_won + total_lost)
        + ".\n"
        "The expected value of each trial is $"
        + str(round((total_won + total_lost) / trials, 2))
        + " or "
        + str(round((((total_won + total_lost) / trials) / bankroll) * 100, 2))
        + "% of the starting"
        " bankroll."
    )

    st.header("Takeaways From Condition 2")
    st.subheader("1. A more ambituous stopping criteria leads to worse results.")
    st.text(
        "By examining the results based on longer- or shorter-duration trials, we can see that\n"
        "the longer a trial is allowed to continue (in terms of number of spins), the worse the\n"
        "expected results for that trial will be. \n"
    )

    st.subheader("2. Some combination of inputs may show positive expected values.")
    st.text("")
