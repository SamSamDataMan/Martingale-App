import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def render_home():
    st.title("Martingale Strategy Analysis")
    st.text(
        "Developed by Samuel King\n"
        " - https://github.com/SamSamDataMan\n"
    )
    st.header("Introduction, User-Guide, & Methodology")
    st.text(
        "This application allows users to model the results of martingale gambling strategies.\n"
        "By adjusting inputs into the model and choosing from various experimental conditions,\n"
        "the user can trivially model and examine the expected results of a massive combination\n"
        "of custom-specified experimental designs."
    )
    st.text(
        "Use the sidebar to the left to navigate through the app, or see below for a brief user\n"
        "guide and explanation of our methodology."
    )
    with st.expander("What Is Martingaling?"):
        st.text(
            "Martingaling is a betting strategy which has bettors double "
            "their wager after each \n"
            "successive loss, returning to a set starting wager after each "
            "win. During each martingale\n"
            "cycle, the bettor is attempting to win an amount equal to their"
            " starting wager. Consider\n"
            "the following example showing a martingale strategy based "
            "on a $10 starting bet:\n"
        )
        results = {
            "Spin": ["Spin 1", "Spin 2", "Spin 3", "Spin 4", "Spin 5", "Spin 6"],
            "Martingale Cycle": [
                "Cycle 1/ Spin 1",
                "Cycle 2/ Spin 1",
                "Cycle 2/ Spin 2",
                "Cycle 2/ Spin 3",
                "Cycle 3/ Spin 1",
                "Cycle 3/ Spin 2",
            ],
            "Result": ["Win", "Lose", "Lose", "Win", "Lose", "Win"],
            "Return": ["+10", "-10", "-20", "+40", "-10", "+20"],
            "Total Profit": ["+10", "0", "-20", "+20", "+10", "+30"],
            "Next Action": [
                "Start New Cycle",
                "Double Bet",
                "Double Bet Again",
                "Start New Cycle",
                "Double Bet",
                "Start New Cycle",
            ],
        }
        df = pd.DataFrame(results)
        df.set_index("Spin", inplace=True)
        st.write(df.head(6))
        st.text(
            "The profit history of the of the above results can be graphed"
            " accordingly:"
        )

        spin = [0, 1, 2, 3, 4, 5, 6]
        profit = [0, 10, 0, -20, 20, 10, 30]
        fig = plt.figure(figsize=(7, 3))
        plt.xlabel("Spin")
        plt.ylabel("Profit ($)")
        plt.vlines(1, -20, 30, linestyles="--", colors="green", label="Start New Cycle")
        plt.vlines(4, -20, 30, linestyles="--", colors="green")
        plt.vlines(6, -20, 30, linestyles="--", colors="green")
        plt.legend(loc=2)
        plt.plot(profit)
        st.write(fig)
        st.text(
            "This general pattern of doubling wagers after each sucessive loss and return to a fixed\n"
            'starting wager after each win is called a "martingale" strategy.'
        )
    with st.expander("User Guide"):
        st.header("User Guide")
        st.subheader("Running Your Martingale Experiment:")
        st.text(
            "Within the left sidebar, use the dropdown menu to select among the experimental\n"
            "conditions described below. Within each condition, you will find various sliders\n"
            "and dropdowns representing inputs into the experiment. In each experimental\n"
            "condition, users will be asked to select:"
        )
        st.subheader("Win Probability")
        st.text(
            'This represents the probability of winning a given hand/ spin. "House Odds"\n'
            "represents a 47.3% chance of winning a given hand/ spin, roughly the same\n"
            'as a red/black bet at a casino roulette wheel. "True Flip" odds represent\n'
            "a 50% chance of success, as one would expect to encounter gambling in a fair\n"
            "game among friends.\n"
        )
        st.subheader("Number of Trials")
        st.text(
            "This slider allows users to choose the number of participants for which to\n"
            "repeat the experiment. The example above represents a single trial. Each\n"
            "trial is represented on the line chart (figure 1) with its own line. Running\n"
            "the experiment with more trials will produce a more robust set of statistical\n"
            "inferences, but is also likely to lead to more extreme outlier obseravtions.\n"
        )
        st.subheader("Starting Bankroll")
        st.text(
            "This slider gives users control over the amount of money with which each trial\n"
            "begins. When this amount is lost, the trial will be considered bankrupt (aka ruin\n"
            "scneario) and the trial will be over./n"
        )
        st.subheader("Starting Wager")
        st.text(
            "This slider allows users to control the starting wager for each martingale cycle.\n"
            "This input is capped at 10% of the starting bankroll to allow for an adequate\n"
            "implementation of the martingale strategy.\n"
        )
        st.subheader("Number of Spins (Condition 2 Only)")
        st.text(
            "In condition 2, this slider allows users to explore the effect of a stopping\n"
            "criteria based on number of spins. Trials that do not go bankrupt will end\n"
            "once this limit has been reached.\n"
        )
        st.subheader("Profit Goal (Condition 3 Only)")
        st.text(
            "In condition 3, this slider allows users to explore the effect of a stopping\n"
            "criteria based on a profit goal, as represented by a multiple of the starting\n"
            "bankroll. Trials that do not go bankrupt will end once this goal has been reached."
        )
    with st.expander("Methodology"):
        st.header("Methodology")
        st.text(
            "The purpose of this application is to allow users to trivially explore the martingale\n"
            "strategy under various conditions and inputs. Using Monte Carlo simulation, we model\n"
            "the distribution of results of the martingale strategy within varied experimental\n"
            "conditions and subject to the user-defined model inputs described above. By inputting\n"
            "various assumptions, users are able to quickly run and re-run related experiments and \n"
            "examine the impact of those assumptions on the results the specified strategy yields.\n"
        )
        st.subheader("Condition 1 - Spin Until Bankrupt")
        st.text(
            "This is the most straightforward condition, in which each trial (representing a bettor) \n"
            "is allowed to martingale until bankruptcy. This condition is largely theoretical, in that\n"
            "few bettors undertake a strategy intent on eventually going bankrupt. That aside, this\n"
            "condition allows us to best understand the full distribution of outcomes associated with\n"
            "a given martingale approach, particularly the duration of trials until bankruptcy and\n"
            "the peak profits of each trial."
        )

        st.subheader("Condition 2 - Set Number of Spins")
        st.text(
            "In this condition, each trial is stopped once the bettor reaches a set number of spins\n"
            "as defined by the user (via an an additional slider). This condition implements a\n"
            "stopping criteria which is intended to act as a real-world constraint (e.g. 250 spins\n"
            "may be used to represent a full day of martingaling at a casino roulette wheel -\n"
            "assuming ~40 spins/ hour. This condition allows us to approximate the expected value of\n"
            "the specified strategy and to observe the associated proportion of winning, losing, and\n"
            "bankrupt trials."
        )

        st.subheader("Condition 3 - Spin Until Profit Goal")
        st.text(
            "Similar to condition two, this condition attempts to implement a real-world stopping\n"
            "criteria, in this case a martingaler who is attempting to achieve some profit goal before\n"
            "stopping (e.g. the bettor wants to double/triple/10x their bankroll and then stop). This\n"
            "condition allows us to approximate the expected value of the specified strategy and to \n"
            "observe the proportion of winners and losers as well as the trial duration distribution.\n"
        )
