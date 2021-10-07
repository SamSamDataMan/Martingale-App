import streamlit as st
import matplotlib.pyplot as plt


def cond3_header():
    st.header("Condition 3: Multiplier Goal")
    st.text(
        "In this condition we allow each trial to continue\n"
        "until the entire bankroll is lost or a multiplier goal is met.\n"
    )
    left, right = st.columns(2)
    left.subheader("Spins to Goal or Bankrupt")
    return left, right


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
    right.subheader("Count of Winners and Losers")
    plt.title("Figure 2: Count of Winners and Losers")
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

    st.header("Takeaways From Condition 3")

    st.subheader("1. A more ambitious stopping criteria leads to worse results.")
    st.text("By examining the results based on higher of lowe multiplier goals, we can see that,\n"
            "intuitively, the more ambitious the goal, the smaller the proportion of trials reach\n"
            "that goal. Similarly, the expected value of a given trial decreases proportionally as\n"
            "the multiplier goal increases.\n"
            )

    st.subheader("2. Increasing the bankroll-to-starting wager ratio decreases odds of success.")
    st.text("Conversely, as compared to condition 2, a larger bankroll-to-starting wager ratio\n"
            "does not improve the odds of being successful in this condition. This is attributed to\n"
            "the fact that the stopping goal becomes more ambitious in proportion to the size of the\n"
            "starting bankroll (e.g. the stopping goal is a multiple of the bankroll).\n"
            )
