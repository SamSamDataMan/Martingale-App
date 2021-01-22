import streamlit as st
import pandas as pd
import random
import seaborn as sns
import matplotlib.ticker as mtick
from matplotlib import pyplot as plt


def spinTilBust(trials, bankroll, startingBet):
    fig = plt.figure()
    # list containing lists of each trial's results.
    resultsLists = []
    # iterate through trials.
    for trial in range(trials):
        # reset results list & starting balance.
        trialResult = []
        balance = bankroll
        # begin new trial.
        while True:
            bet = startingBet
            # if subject is bankrupt, game is over.
            if balance < bet:
                # append results to master list.
                resultsLists.append(trialResult)
                # end trial by breaking while loop.
                break
            # otherwise, begin new martingale cycle.
            while True:
                # if current bankroll is sufficient for the next wager, SPIN:
                if balance >= bet:
                    # losing spin
                    if random.random() > 0.4736842:
                        balance -= bet
                        bet = bet * 2
                        trialResult.append(balance-bankroll)
                    # winning spin
                    else:
                        balance += bet
                        trialResult.append(balance-bankroll)
                        break
                else:
                    break
        plt.plot(trialResult, linewidth=1, alpha=.5)
    x_max = 0
    for i in resultsLists:
        listMax = len(i)
        if listMax > x_max:
            x_max = listMax
    plt.title('Figure 1: Profit Over Time')
    plt.ylabel('Profit')
    plt.ylim(-2*bankroll)
    plt.hlines((-1*bankroll), 0, x_max,
               colors='Red', linestyles='solid',
               linewidth=2, label='Bankrupt')
    plt.legend()
    plt.xlabel('Spin Count')
    plt.grid(b=True, which='major')
    left.pyplot(fig)
    return resultsLists


def xNumSpins(trials, bankroll, startingBet, numSpins):
    fig = plt.figure()
    resultsLists = []
    # number of subjects to repeat trial for
    for trial in range(trials):
        trialResult = []
        balance = bankroll
        cycles = 1
        spins = 1
        counter = 1
        # New Martingale Cycle
        while counter <= numSpins:
            if counter == numSpins:
                resultsLists.append(trialResult)
                break
            bet = startingBet
            if balance < bet:
                resultsLists.append(trialResult)
                break
            else:
                print('New Martingale Cycle #', cycles)
            # control sims by number of spins
            while counter <= numSpins:
                if counter == numSpins:
                    break
                if balance >= bet:
                    print('New Spin #', spins,
                          'Balance =', balance,
                          'Bet =', bet)
                    if random.random() > .4736842:
                        balance -= bet
                        bet = bet * 2
                        trialResult.append(balance-bankroll)
                        spins += 1
                        counter += 1
                    else:
                        balance += bet
                        trialResult.append(balance-bankroll)
                        spins += 1
                        cycles += 1
                        counter += 1
                        break
                else:
                    print("You're Broke, Current Profit =", balance-bankroll,
                          "current bet =", bet)
                    break
        plt.plot(trialResult, linewidth=.5, alpha=.5)
    plt.title('Figure 1: Profit Over # of Spins')
    plt.grid(b=True, which='major')
    plt.ylabel('Profit')
    plt.xlabel('Spin Count')
    plt.legend()
    left.pyplot(fig)
    return resultsLists


def xOrNothing(trials, bankroll, startingBet, multGoal: int):
    fig = plt.figure()
    # list containing lists of each trial's results.
    resultsLists = []
    # iterate through trials.
    for trial in range(trials):
        # reset results list & starting balance.
        trialResult = []
        balance = bankroll
        # begin new trial.
        while True:
            bet = startingBet
            # if subject is bankrupt, game is over.
            if balance < bet or balance >= bankroll*multGoal:
                # append results to master list.
                resultsLists.append(trialResult)
                # end trial by breaking while loop.
                break
            # otherwise, begin new martingale cycle.
            while True:
                # if current bankroll is sufficient for the next wager, SPIN:
                if balance >= bet:
                    # losing spin
                    if random.random() > 0.4736842:
                        balance -= bet
                        bet = bet * 2
                        trialResult.append(balance-bankroll)
                    # winning spin
                    else:
                        balance += bet
                        trialResult.append(balance-bankroll)
                        break
                else:
                    break
        plt.plot(trialResult, linewidth=1, alpha=.5)
    x_max = 0
    for i in resultsLists:
        listMax = len(i)
        if listMax > x_max:
            x_max = listMax
    plt.title('Figure 1: Profit Over Time')
    plt.ylabel('Profit')
    plt.ylim(-1.2*bankroll)
    plt.hlines((-1*bankroll), 0, x_max,
               colors='Red', linestyles='solid',
               linewidth=2, label='Bankrupt')
    plt.hlines(((multGoal*bankroll)-bankroll), 0, x_max,
               colors='Green', linestyles='solid',
               linewidth=2, label='Achieved Goal')
    plt.legend()
    plt.xlabel('Spin Count')
    plt.grid(b=True, which='major')
    left.pyplot(fig)
    return resultsLists


# Sidebar - User Inputs
st.sidebar.title('Martingale Analysis')
option = st.sidebar.selectbox(
     'Choose an experimental condition:',
     ('Spin Until Bankrupt', 'Fixed Number of Spins', 'X-or-nothing'))

if option == 'Spin Until Bankrupt':
    st.header("Condition: Spin Until Bankrupt")
    st.text('In this condition we allow each trial to continue\n'
            'until the entire bankroll is lost.\n')
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins Until Bankrupt")
    trials = st.sidebar.slider('1. Select a # of trials to'
                               'repeat the experiment:', 10, 1000, 100,
                               step=10)
    bankroll = st.sidebar.slider('2. Select a starting bankroll'
                                 ' for each trial:', 25, 10000, 1000,
                                 step=25)
    startBet = st.sidebar.slider('3. Select a starting wager'
                                 ' for each martingale cycle:',
                                 5, int(bankroll/10), 10, step=5)
    # Create first chart
    results = spinTilBust(trials, bankroll, startBet)

    # Descriptives for First Plot
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
    totalSpins = upSpins + downSpins
    maxProfitList = [i[0] for i in maxProfits]

    df = pd.DataFrame(spinsToBust)
    df.head()

    df.columns = ['Spin Count']
    df.head()

    mean = round(df['Spin Count'].mean(), 2)
    median = round(df['Spin Count'].median(), 2)
    std = round(df['Spin Count'].std(), 2)
    maxx = round(df['Spin Count'].max(), 2)
    minn = round(df['Spin Count'].min(), 2)

    neverUp = [i for i in maxProfits if i[0] == -10]
    doubledUp = [i for i in maxProfits if i[0] >= 1000]
    tripledUp = [i for i in maxProfits if i[0] >= 2000]
    tenX = [i for i in maxProfits if i[0] >= 10000]

    df2 = pd.DataFrame(maxProfitList)
    df2.columns = ['Max Profit']

    mean2 = df2['Max Profit'].mean()
    median2 = df2['Max Profit'].median()
    std2 = df2['Max Profit'].std()
    maxx2 = df2['Max Profit'].max()
    minn2 = df2['Max Profit'].min()

    right.subheader("Peak Profit During Trial")
    fig = plt.figure()
    plt.title('Figure 2: Max Profit of Each Trial')
    ax = sns.distplot(df2['Max Profit'],
                      rug=True, rug_kws={'height': '.085'},
                      kde_kws={'color': 'forestgreen', 'linewidth': '1.5'},
                      bins=30, hist=False,
                      color='crimson')
    # plt.vlines(mean2,0,0.0005,colors='indigo',linestyles='dotted',linewidth=2,label='Mean',)
    # plt.vlines(median2,0,0.0005,colors='orange',linestyles='--',linewidth=2,label='Median')
    plt.legend()
    plt.grid(b=True, which='major', linewidth=.4)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set(xlabel='Peak Profit of Trial ($)', ylabel='Frequency of Outcome')
    ax.set_facecolor('aliceblue')
    right.pyplot(fig)

    # First Table
    left_column, right_column = st.beta_columns(2)
    a = pd.DataFrame([int(mean), int(median), int(std), int(maxx), int(minn)])
    a.index = ['Mean', 'Median', 'St.Dev', 'Maximum', 'Minimum']
    a.columns = ['Number of Spins']
    left_column.write(a)

    a = pd.DataFrame([int(mean2), int(median2), int(std2),
                      int(maxx2), int(minn2)])
    a.index = ['Mean', 'Median', 'St.Dev', 'Maximum', 'Minimum']
    a.columns = ['Peak Profit']
    right_column.write(a)

elif option == 'Fixed Number of Spins':
    st.header("Condition: Fixed Number of Spins")
    st.text('In this condition we allow each trial to continue until a\n'
            'fixed number of spins or the entire bankrollis lost.\n')
    left, right = st.beta_columns(2)
    left.subheader("Fixed Number of Spins")
    trials = st.sidebar.slider('1. Select a # of trials to'
                               ' repeat the experiment:', 10, 1000, 100,
                               step=10)
    bankroll = st.sidebar.slider('2. Select a starting bankroll'
                                 ' for each trial:', 25, 10000, 1000,
                                 step=25)
    startBet = st.sidebar.slider('3. Select a starting wager'
                                 ' for each martingale cycle:',
                                 5, int(bankroll/10), 10, step=5)
    numSpins = st.sidebar.slider('4. Select a number of'
                                 ' spins for each trial:',
                                 10, 10000, 100, step=10)
    results = xNumSpins(trials, bankroll, startBet, numSpins)
    winners = [i for i in results if i[-1] > 0]
    losers = [i for i in results if i[-1] < 0]
    x = ['Winners', 'Losers']
    y = [len(winners), len(losers)]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=['green', 'red'])
    right.subheader('Proportion of Winners and Losers')
    plt.title('Figure 2: Proportion of Winners and Losers')
    right.pyplot(fig)

elif option == 'X-or-nothing':
    st.header("Condition: Multiplier Goal")
    st.text('In this condition we allow each trial to continue\n'
            'until the entire bankroll is lost or a multiplier goal is met.\n')
    left, right = st.beta_columns(2)
    left.subheader("Number of Spins To Goal or Bankrupt")
    trials = st.sidebar.slider('1. Select a # of trials to'
                               ' repeat the experiment:', 10, 1000, 100,
                               step=10)
    bankroll = st.sidebar.slider('2. Select a starting bankroll'
                                 ' for each trial:', 25, 10000, 1000,
                                 step=25)
    startBet = st.sidebar.slider('3. Select a starting wager'
                                 ' for each martingale cycle:',
                                 5, int(bankroll/10), 10, step=5)
    multGoal = st.sidebar.slider('4. Select a bankroll multiplier'
                                 ' as a goal for each trial:',
                                 2, 10, 2, step=1)
    results = xOrNothing(trials, bankroll, startBet, multGoal)
    winnerResults = []
    loserResults = []
    for i in results:
        if i[-1] > 0:
            winnerResults.append(i)
        else:
            loserResults.append(i)
    winnerCount = len(winnerResults)
    loserCount = len(loserResults)
    x = ['Winners', 'Losers']
    y = [winnerCount, loserCount]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=['green', 'red'])
    right.subheader('Proportion of Winners and Losers')
    plt.title('Figure 2: Proportion of Winners and Losers')
    right.pyplot(fig)
    # RESUME HERE
else:
    st.write('Hmmm... this shouldn\'t be...')

# BEGIN FAQ SECTION
st.subheader('Frequently Asked Questions:')
if st.checkbox('What Is Martingaling?'):
    st.text('Martingaling is a betting strategy which has bettors double '
            'their wager after each \n'
            'successive loss, returning to a fixed starting wager after each '
            'win. The bettor \n'
            'is attempting to win an amount equal to their starting wager '
            'during each cycle.\n'
            'Martingale strategies are profitable under theoretical '
            'conditions, but quickly revert to \n'
            'negative-expectation once real-world limitations '
            '(e.g. finite bankroll, house \n'
            'bet limits, etc...) are acccounted for.')

if st.checkbox('How do I interpret figure 1?'):
    st.text('Great question!')

if st.checkbox('How do I interpret figure 2?'):
    st.text('Great question!')

if st.checkbox('How do I interpret Table 1?'):
    st.text('Great question!')

if st.checkbox('How do I interpret Table 2?'):
    st.text('Great question!')
