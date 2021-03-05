import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt


def render_cond2(left, right, trials, results, bankroll):
    winners = [i for i in results if i[-1] > 0]
    losers = [i for i in results if i[-1] < 0]
    winner_results = [i[-1] for i in winners]
    loser_results = [i[-1] for i in losers]
    total_won = sum(winner_results)
    total_lost = sum(loser_results)
    x = ["Winners", "Losers"]
    y = [len(winners), len(losers)]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=["green", "red"])
    right.subheader("Proportion of Winners and Losers")
    plt.title("Figure 2: Proportion of Winners and Losers")
    right.pyplot(fig)
    st.header("Results:")
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

    # st.header('Takeaways from this condition:')
    # st.subheader('1. Placeholder')
    # st.text('Placeholder')