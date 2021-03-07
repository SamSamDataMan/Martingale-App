import streamlit as st


def render_conc():
    st.header("Conclusions")
    st.subheader("General")
    st.text(
        "From this experiment, we can conclude that martingaling is an extremely high variance\n"
        "strategy, with an asymmetric downside risk for participants. Further, the strategy does\n"
        "not significantly alter a game's expectation from any other strategy. Martingaling is\n"
        "not an effective risk-mitigation strategy, and those who try it for long enough will\n"
        "eventually go bankrupt."
    )
    st.text(
        "If one is intent on martingaling, they will see relatively much better results if it\n"
        'can be done in a "fair" game, or one in which the house does not have an inherent\n'
        "advantage. That said, even in a fair game, martingale trials will still eventually\n"
        "end in bankruptcy."
    )
    st.subheader("Condition 1")
    st.text(
        "Condition 1 proved that, given a finite bankroll, a martingale strategy in a negative-\n"
        "expectation game will inevitable end in bankruptcy.\n"
    )
    st.text(
        "This condition also showed that adjusting odds to remove a house edge (e.g. a neutral-\n"
        "expectation game) will produce a wider distribution of results and increase the expected\n"
        "longevity of each individual trial"
    )
    st.subheader("Condition 2")
    st.text(
        "Condition 2 showed that more a more aggressive approach (either a longer trial-duration\n"
        "or higher starting-bet:bankroll ratio) will result in worse performance for each trial,\n"
        "as indicated by a lower returned expected value per trial."
    )
    st.subheader("Condition 3")
    st.text(
        "Similar to condition 2, condition 3 showed that a more aggressive approach (either a more\n"
        "ambitious stopping critera or starting-bet:bankroll ratio) will result in worse\n"
        "performance for each trial, as indicated by a lower returned expected value per trial."
    )
