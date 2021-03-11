import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt


def cond1_header():
    st.header("Condition 1: Spin Until Bankrupt")
    st.text(
        "In this condition we allow each trial to continue until the entire bankroll is lost.\n"
    )
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins Until Bankrupt")
    return left, right


def render_cond1(left, right, trials, results):
    left.subheader("Results")
    left.text(
        "Figure 1 shows the profit history of trials\n"
        "in this experiment. Note that most trials\n"
        "end in bankruptcy fairly quickly, but a\n"
        "relative few are successful for a large\n"
        "number of spins before going bankrupt."
    )

    # Descriptives for First Plot
    # TODO: Refactor out to helper function
    spinsToBust = []
    maxProfits = []
    upSpins = 0
    downSpins = 0
    for i in results:
        spinsToBust.append(len(i))
        maxProfits.append((max(i), len(i)))
        for j in i:
            if j < 0:
                downSpins += 1
            else:
                upSpins += 1
    maxProfitList = [i[0] for i in maxProfits]

    df = pd.DataFrame(spinsToBust)
    df.head()

    df.columns = ["Spin Count"]
    df.head()

    mean = round(df["Spin Count"].mean(), 2)
    median = round(df["Spin Count"].median(), 2)
    maxx = round(df["Spin Count"].max(), 2)
    minn = round(df["Spin Count"].min(), 2)

    left.text(
        "The shortest trial in the experiment\n"
        "concluded in a mere " + str(minn) + " spins, while the\n"
        "longest trial lasted for " + str(maxx) + " spins.\n"
        "The difference between measures of central\n"
        "tendency also speak to the skew of this\n"
        "distribution. Given a mean number of spins\n"
        "(" + str(int(mean)) + ") which is significantly higher\n"
        "than the median (" + str(int(median)) + "), we can see the impact\n"
        "of outlier long-duration trials skewing\n"
        "our spin-count distribution to the right."
    )

    df2 = pd.DataFrame(maxProfitList)
    df2.columns = ["Max Profit"]

    mean2 = df2["Max Profit"].mean()
    median2 = df2["Max Profit"].median()
    maxx2 = df2["Max Profit"].max()
    minn2 = df2["Max Profit"].min()

    right.subheader("Peak Profit During Trial")

    # TODO: Refactor plot to own function
    fig = plt.figure()
    plt.title("Figure 2: Max Profit of Each Trial")
    ax = sns.distplot(
        df2["Max Profit"],
        rug=True,
        rug_kws={"height": ".025"},
        kde_kws={"color": "green", "linewidth": "1.5"},
        hist=True,
        norm_hist=False,
        bins=int(trials / 10),
        hist_kws={"color": "lightsalmon"},
        color="crimson",
    )
    plt.legend()
    plt.grid(b=True, which="major", linewidth=0.4)
    ax.set_xlim(-10, maxx2)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set(xlabel="Peak Profit of Trial ($)", ylabel="Frequency of Outcome")
    right.pyplot(fig)
    right.subheader("")
    right.text("")
    right.text(
        "Figure 2 shows the distribution of peak\n"
        "profits for each trial (with each red \n"
        "line on the rugplot representing a\n"
        "single trial). Note that a small subset\n"
        "of all trials experiences significant profit\n"
        "before inevitably going bankrupt, skewing\n"
        "the distribution significantly to the right."
    )

    right.text(
        "The most successful trial in this experiment\n"
        "experienced a peak profit of $" + str(maxx2) + ", while\n"
        "the least successful trial(s) experienced a\n"
        "peak profit of $" + str(minn2) + ". Similar to figure 1\n"
        "the mean: $" + str(round(mean2, 2)) + " is significantly higher\n"
        "than the median: $" + str(round(median2, 2)) + " indicating rightward\n"
        "skew to this distribution as well."
    )

    st.header("Takeaways From Condition 1")
    st.subheader("1. Martingaling appears to be successful (until it isn't)")
    st.text(
        "Each trial experiences slow and steady profitability tightly grouped around an upward-\n"
        "sloping trajectory until the trial experiences a ruin or near-ruin scenario. After a \n"
        "near-ruin scenario, this slow, upward-sloping pattern continues until encoutering ruin\n"
        "or near-ruin again, and so forth until bankruptcy."
    )

    st.subheader(
        "2. Martingaling cannot turn an unprofitable game into a profitable one"
    )
    st.text(
        "The fact is that, regardless of any combination of input variables (bankroll or starting \n"
        "bet), each trial inevitably ends at some point in bankruptcy. This condition suggests,\n"
        "given a finite bankroll, a martingaler will eventually go bankrupt."
    )

    st.subheader(
        '3. Adjusting "Win Probability" to true 50/50 odds massively increases variance of results'
    )
    st.text(
        'Intuitively, removing a "house edge" from the game results in increases the expected\n'
        'longevity of each trial. In a "fair" game with 50/50 odds, we see a wider distribution of\n'
        "outcomes, but the fact remains that each trial will eventually go bankrupt by following\n"
        "this strategy. As a corollary to the first takeaway, martingaling will only be profitable\n"
        "in a game that is already profitable without the martingale strategy."
    )

    st.subheader("4. The variance in outcomes resulting from this strategy is massive")
    st.text(
        "If this strategy is not profitable, it is natural to wonder why it enjoyed periodic\n"
        "popularity. The large variance of outcomes associated with this strategy is one likely\n"
        "explanation. For example, if someone had tried using the strategy and experienced the \n"
        "short-term results associated with one of our outlier trials, but had not yet experienced \n"
        "an inevitable downswing, that person may have been anecdotally convinced of its efficacy,\n"
        'and may have convinced others to attempt this seemingly "fool-proof" strategy themselves.'
    )
