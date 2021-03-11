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
            f"The {str(len(winners))} winning trials won a total of $ "
            f"{str(total_won)} or ${str(round(total_won / len(winners), 2))} "
            f"per winning trial.\nThe {str(len(losers))} The {str(len(losers))}"
            f" losing trials lost a total of ${str(total_lost)} or $"
            f"{str(round(total_lost / len(losers), 2))} per losing trial."
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

    st.subheader("2. Minimizing the starting bankroll produces widely varied results.")
    st.text(
        "By minimizing the starting bankroll, bankruptcy becomes more likely over a given number\n"
        "of spins. However, the impact of those bankrupt trials is also minimized on the overall\n"
        "expected value. While minimizing number of spins, the expected values associated with this\n"
        "strategy may range from slightly positive to massively negative, depending on the\n"
        "observed number of bankrupt trials. However, by increasing the number of spins and holding\n"
        "the small bankroll constant, we see a familiar pattern in the proportion of losing and\n"
        "bankrupt trials growing, and the expected value of the strategy approaching -100%."
    )

    st.subheader(
        "3. A large bankroll-to-starting wager ratio improves the proportion of winners but does not improve expected value."
    )
    st.text(
        "Over a given number of spins, it is much less likely to go bankrupt with a large bankroll\n"
        "relative to the starting wager. However, the downside risk of those bankruptcies has a\n"
        "larger impact on the expected value when they do occur. Likewise, the gradual nature of \n"
        "winnings associated with this strategy do not accumulate very quickly in comparison to the\n"
        "large starting bankroll. Thus, over a small number of spins, an experiment with this\n"
        "specification will produce a small positive or negative expected value. Over a larger\n"
        "number of spins, the same pattern emerges that expected value decreases in proportion to\n"
        "the trial duration."
    )
