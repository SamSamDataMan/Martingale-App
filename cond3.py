import streamlit as st
import matplotlib.pyplot as plt


def render_cond3(left, right, trials, results, bankroll):
    winnerResults = []
    loserResults = []
    for i in results:
        if i[-1] > 0:
            winnerResults.append(i)
        else:
            loserResults.append(i)
    winnerCount = len(winnerResults)
    loserCount = len(loserResults)
    winnerTotals = [i[-1] for i in winnerResults]
    loserTotals = [i[-1] for i in loserResults]
    total_won_c3 = sum(winnerTotals)
    total_lost_c3 = sum(loserTotals)
    x = ["Winners", "Losers"]
    y = [winnerCount, loserCount]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=["green", "red"])
    right.subheader("Proportion of Winners and Losers")
    plt.title("Figure 2: Proportion of Winners and Losers")
    right.pyplot(fig)

    st.header("Results:")
    if winnerCount != 0:
        st.text(
            "The "
            + str(len(winnerResults))
            + " winning trials won a total of $"
            + str(total_won_c3)
            + " or $"
            + str(round(total_won_c3 / len(winnerResults), 2))
            + " per winning trial.\n"
            "The "
            + str(len(loserResults))
            + " losing trials won a total of $"
            + str(total_lost_c3)
            + " or $"
            + str(round(total_lost_c3 / len(loserResults), 2))
            + " per losing trial.\n"
        )
    else:
        st.text("There were no winning trials in this experiment.")
    st.text(
        "The total return of all trials in this experiment was $"
        + str(total_won_c3 + total_lost_c3)
        + ".\n"
        "The expected value of each trial is $"
        + str(round((total_won_c3 + total_lost_c3) / trials, 2))
        + " or "
        + str(round((((total_won_c3 + total_lost_c3) / trials) / bankroll) * 100, 2))
        + "% of the"
        " starting bankroll."
    )
