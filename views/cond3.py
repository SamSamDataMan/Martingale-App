import streamlit as st
import matplotlib.pyplot as plt


def cond3_header():
    st.header("Condition 3: Multiplier Goal")
    st.text(
        "In this condition we allow each trial to continue\n"
        "until the entire bankroll is lost or a multiplier goal is met.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins To Goal or Bankrupt")
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

    st.header("Takeaways From Condition 3")
    
    st.subheader("1. A more ambituous stopping criteria leads to worse results.")
    st.text("By examining the results based on higher of lowe multiplier goals, we can see that,\n"
            "intuitively, the more ambitous the goal, the smaller the proportion of trials reach\n"
            "that goal. Similarly, the expected value of a given trial decreases proportionally as\n"
            "the multiplier goal increases.\n"
            )
    
    #st.subheader("2. Minimizing the starting bankroll produces widely varied results.")
    #st.text("By minimizing the starting bankroll, bankruptcy becomes more likely over a given number\n"
        # "of spins. However, the impact of those bankrupt trials is also minimized on the overall\n"
        # "expected value. While minimizing number of spins, the expected values associated with this\n"
        # "strategy may range from slightly positive to massively negative, depending on the\n"
        # "observed number of bankrupt trials. However, by increasing the number of spins and holding\n"
        # "the small bankroll constant, we see a familiar pattern in the proportion of losing and\n"
        # "bankrupt trials growing, and the expected value of the strategy approaching -100%.")
    
    #st.subheader(
        # "3. A large bankroll-to-starting wager ratio improves the proportion of winners but does not improve expected value.")
    #st.text(
        # "Over a given number of spins, it is much less likely to go bankrupt with a large bankroll\n"
        # "relative to the starting wager. However, the downside risk of those bankruptcies has a\n"
        # "larger impact on the expected value when they do occur. Likewise, the gradual nature of \n"
        # "winnings associated with this strategy do not accumulate very quickly in comparison to the\n"
        # "large starting bankroll. Thus, over a small number of spins, an experiment with this\n"
        # "specification will produce a small positive or negative expected value. Over a larger\n"
        # "number of spins, the same pattern emerges that expected value decreases in proportion to\n"
        # "the trial duration.")