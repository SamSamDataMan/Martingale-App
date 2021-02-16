import streamlit as st
import pandas as pd
import random
import seaborn as sns
import matplotlib.ticker as mtick
from matplotlib import pyplot as plt

house_odds = 0.4736842
true_flip_odds = 0.5
odds = house_odds


def handle_losing_spin(balance, bet):
    balance -= bet
    bet = bet * 2
    return balance, bet


def handle_winning_spin(balance, bet):
    balance += bet
    return balance


def spin_til_bust(trials, bankroll, startingBet):
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
                    if random.random() > p_win:
                        balance, bet = handle_losing_spin(balance, bet)
                        trialResult.append(balance-bankroll)
                    # winning spin
                    else:
                        balance = handle_winning_spin(balance, bet)
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
    plt.ylabel('Profit ($)')
    plt.ylim(-2*bankroll)
    plt.hlines((-1*bankroll), 0, x_max,
               colors='Red', linestyles='solid',
               linewidth=2, label='Bankrupt')
    plt.legend()
    plt.xlabel('Spin Count')
    plt.grid(b=True, which='major')
    left.pyplot(fig)
    return resultsLists


def x_num_spins(trials, bankroll, startingBet, numSpins):
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
                    # losing spin
                    if random.random() > p_win:
                        balance, bet = handle_losing_spin(balance, bet)
                        trialResult.append(balance-bankroll)
                        spins += 1
                        counter += 1
                    # winning spin
                    else:
                        balance = handle_winning_spin(balance, bet)
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
    plt.ylabel('Profit ($)')
    plt.xlabel('Spin Count')
    plt.legend()
    left.pyplot(fig)
    return resultsLists


def x_or_nothing(trials, bankroll, startingBet, multGoal: int):
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
                    if random.random() > p_win:
                        balance, bet = handle_losing_spin(balance, bet)
                        trialResult.append(balance-bankroll)
                    # winning spin
                    else:
                        balance = handle_winning_spin(balance, bet)
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
    plt.ylabel('Profit ($)')
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
     'Page Navigation:',
     ('Home', 'Condition 1: Spin Until Bankrupt', 'Condition 2: Fixed Number of Spins',
      'Condition 3: X-or-nothing', 'Conclusions'))

if option == 'Condition 1: Spin Until Bankrupt' or option == 'Condition 2: Fixed Number of Spins' or option == 'Condition 3: X-or-nothing':
    odds = st.sidebar.selectbox(
        'Choose a Win Probability:',
        ('House Odds', 'True Flip')
    )

if odds == "House Odds":
    p_win = house_odds
elif odds == "True Flip":
    p_win = true_flip_odds

if option == 'Home':
    st.header('Introduction, User-Guide, & Methodology')
    st.text('This application allows users to model the results of martingale gambling strategies.\n'
            'By adjusting inputs into the model and choosing from various experimental conditions,\n'
            'the user can trivially model and examine the expected results of a massive combination\n'
            'of custom-specified designs.')
    st.subheader('Introduction')
    st.text('Martingaling is a betting strategy which has bettors double '
            'their wager after each \n'
            'successive loss, returning to a set starting wager after each '
            'win. During each martingale\n'
            'cycle, the bettor is attempting to win an amount equal to their'
            ' starting wager. Consider\n'
            'the following example showing a martingale strategy based '
            'on a $10 starting bet:\n')
    results = {'Spin': ['Spin 1', 'Spin 2', 'Spin 3', 'Spin 4', 'Spin 5',
                        'Spin 6'],
               'Martingale Cycle': ['Cycle 1/ Spin 1', 'Cycle 2/ Spin 1',
                                    'Cycle 2/ Spin 2', 'Cycle 2/ Spin 3',
                                    'Cycle 3/ Spin 1', 'Cycle 3/ Spin 2'],
               'Result': ['Win', 'Lose', 'Lose', 'Win', 'Lose', 'Win'],
               'Return': ['+10', '-10', '-20', '+40', '-10', '+20'],
               'Total Profit': ['+10', '0', '-20', '+20', '+10', '+30'],
               'Next Action': ['Start New Cycle', 'Double Bet',
                               'Double Bet Again', 'Start New Cycle',
                               'Double Bet', 'Start New Cycle']
               }
    df = pd.DataFrame(results)
    df.set_index('Spin', inplace=True)
    st.write(df.head(6))
    st.text('The profit history of the of the above results can be graphed'
            ' accordingly:')

    spin = [0, 1, 2, 3, 4, 5, 6]
    profit = [0, 10, 0, -20, 20, 10, 30]
    fig = plt.figure(figsize=(7, 3))
    plt.xlabel('Spin')
    plt.ylabel('Profit ($)')
    plt.vlines(1, -20, 30, linestyles='--', colors='green',
               label="Start New Cycle")
    plt.vlines(4, -20, 30, linestyles='--', colors='green')
    plt.vlines(6, -20, 30, linestyles='--', colors='green')
    plt.legend(loc=2)
    plt.plot(profit)
    st.write(fig)

    st.header('User Guide')
    st.subheader('Running Your Martingale Experiment:')
    st.text('Within the left sidebar, use the dropdown menu to select among the experimental\n'
            'conditions described below. Within each condition, you will find various sliders\n'
            'and dropdowns representing inputs into the experiment. In each experimental\n'
            'condition, users will be asked to select:')
    st.subheader('Win Probability')
    st.text('This represents the probability of winning a given hand/ spin. "House Odds"\n'
            'represents a 47.3% chance of winning a given hand/ spin, roughly the same\n'
            'as a red/black bet at a casino roulette wheel. "True Flip" odds represent\n'
            'a 50% chance of success, as one would expect to encounter gambling in a fair\n'
            'game among friends.\n')
    st.subheader('Number of Trials')
    st.text('This slider allows users to choose the number of participants for which to\n'
            'repeat the experiment. The example above represents a single trial. Each\n'
            'trial is represented on the line chart (figure 1) with its own line. Running\n'
            'the experiment with more trials will produce a more robust set of statistical\n'
            'inferences, but is also likely to lead to more extreme outlier obseravtions.\n')
    st.subheader('Starting Bankroll')
    st.text('This slider gives users control over the amount of money with which each trial\n'
            'begins. When this amount is lost, the trial will be considered bankrupt (aka ruin\n'
            'scneario) and the trial will be over./n')
    st.subheader('Starting Wager')
    st.text('This slider allows users to control the starting wager for each martingale cycle.\n'
            'This input is capped at 10% of the starting bankroll to allow for an adequate\n'
            'implementation of the martingale strategy.\n'
            )
    st.subheader('Number of Spins (Condition 2 Only)')
    st.text('In condition 2, this slider allows users to explore the effect of a stopping\n'
            'criteria based on number of spins. Trials that do not go bankrupt will end\n'
            'once this limit has been reached.\n'
            )
    st.subheader('Profit Goal (Condition 3 Only)')
    st.text('In condition 3, this slider allows users to explore the effect of a stopping\n'
            'criteria based on a profit goal, as represented by a multiple of the starting\n'
            'bankroll. Trials that do not go bankrupt will end once this goal has been reached.')

    st.header('Methodology')
    st.text('The purpose of this application is to allow users to trivially explore the martingale\n'
            'strategy under various conditions and inputs. Using repeated stochastic simulation, we\n'
            'model the distribution of results of the martingale strategy within varied experimental\n'
            'conditions and subject to the user-defined model inputs described above. By inputting\n'
            'various assumptions, users are able to quickly run and re-run related experiments and \n'
            'examine the impact of those assumptions on the distribution of results the strategy will\n'
            'produce.\n')
    st.subheader('Condition 1 - Spin Until Bankrupt')
    st.text('This is the most straightforward condition, in which each trial (representing a bettor) \n'
            'is allowed to martingale until bankruptcy. This condition is largely theoretical, in that\n'
            'few bettors undertake a strategy intent on eventually going bankrupt. That aside, this\n'
            'condition allows us to best understand the full distribution of outcomes associated with\n'
            'a given martingale approach.\n')

    st.subheader('Condition 2 - Set Number of Spins')
    st.text('In this condition, each trial is stopped once the bettor reaches a set number of spins\n'
            'as defined by the user (via an an additional slider). This condition implements a\n'
            'stopping criteria which is intended to act as a real-world constraint (e.g. 250 spins\n'
            'may be used to represent a full day of martingaling at a casino roulette wheel -\n'
            'assuming something on the order of 40 spins per hour.')

    st.subheader('Condition 3 - Spin Until Profit Goal')
    st.text('Similar to condition two, this condition attempts to implement a real-world stopping\n'
            'criteria, in this case a martingaler who is attempting to achieve some profit goal\n'
            'before stopping (e.g. the bettor wants to double/triple/10x their bankroll and then\n'
            'stop).\n')

elif option == 'Condition 1: Spin Until Bankrupt':
    st.header("Condition 1: Spin Until Bankrupt")
    st.text('In this condition we allow each trial to continue until the entire bankroll is lost.\n')
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
    results = spin_til_bust(trials, bankroll, startBet)
    left.text('Figure 1 shows the profit history of trial\n'
              'in this experiment. Note that most trials\n'
              'end in bankruptcy fairly quickly, but a\n'
              'relative few are successful for a large\n'
              'number of spins before going bankrupt.')

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

    left.text('The shortest trial in the experiment\n'
              'concluded in a mere ' + str(minn) + ' spins, while the\n'
              'longest trial lasted for ' + str(maxx) + ' spins.\n'
              'The difference between measure of central\n'
              'tendency also speak to the skew of this\n'
              'distribution. Given a mean number of spins\n'
              '(' + str(int(mean)) + ') which is significantly higher\n'
              'than the median (' + str(int(median)) + '), we can see the impact\n'
              'of outlier long-duration trials skewing\n'
              'our spin-count distribution.')

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
    right.text('Figure 2 shows the distribution of peak\n'
               'profits for each trial (with each red \n'
               'line on the rugplot representing a\n'
               'single trial). Note that a small subset\n'
               'of all trials experiences significant profit\n'
               'before inevitably going bankrupt, skewing the\n'
               'distribution significantly to the right.')
    
    right.text('The most successful trial in this experiment\n'
               'experienced a peak profit of $' + str(maxx2) + ', while\n'
               'the least successful trial(s) experienced a\n'
               'peak profit of $' + str(minn2) + '. Similar to figure 1\n'
               'the mean: $' + str(round(mean2, 2)) + ' is significantly higher\n'
               'than the median: $' + str(round(median2, 2)) + ' indicating rightward\n'
               'skew to this distribution as well.')

    st.header('Takeaways From This Condition')
    st.subheader('1. Martingaling cannot turn an unprofitable game into a profitable one')
    st.text('In this condiiton, each trial is allowed to continue until the trial is bankrupt. The fact\n'
            'that, regardless of any combination of input variables (bankroll or starting bet), each\n'
            'trial inevitably ends at some point in bankruptcy.')
    st.subheader('2. The variance in outcomes resulting from this strategy is massive')
    st.text('If this strategy is not profitable, it is natural to wonder why it enjoyed periodic\n'
            'popularity. The large variance of outcomes associated with this strategy is one likely\n'
            'explanation. For example, if someone had tried using the strategy and experienced the \n'
            'short-term results associated with one of our outlier trials, but had not yet experienced \n'
            'an inevitable downswing, that person may have been anecdotally convinced of its efficacy,\n'
            'and may have convinced others to attempt this seemingly "fool-proof" strategy themselves.')
    st.subheader('3. Adjusting "Win Probability" to true 50/50 odds massively increases variance of results')
    st.text('Intuitively, removing a "house edge" from the game results in increases the expected\n'
            'longevity of each trial. In a "fair" game with 50/50 odds, we see a wider distribution of\n'
            'outcomes, but the fact remains that each trial will eventually go bankrupt by following\n'
            'this strategy. As a collolary to the first takeaway, martingaling will only be profitable\n'
            'in a game that is already profitable without the martingale strategy.')

elif option == 'Condition 2: Fixed Number of Spins':
    st.header("Condition 2: Fixed Number of Spins")
    st.text('In this condition we allow each trial to continue until a\n'
            'fixed number of spins or the entire bankroll is lost.\n')
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
    results = x_num_spins(trials, bankroll, startBet, numSpins)
    winners = [i for i in results if i[-1] > 0]
    losers = [i for i in results if i[-1] < 0]
    x = ['Winners', 'Losers']
    y = [len(winners), len(losers)]
    fig = plt.figure(figsize=(8, 6))
    ax = plt.bar(x, y, color=['green', 'red'])
    right.subheader('Proportion of Winners and Losers')
    plt.title('Figure 2: Proportion of Winners and Losers')
    right.pyplot(fig)

elif option == 'Condition 3: X-or-nothing':
    st.header("Condition 3: Multiplier Goal")
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
    results = x_or_nothing(trials, bankroll, startBet, multGoal)
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
elif option == "Conclusions":
    st.header('Conclusions')
else:
    st.write('Hmmm... this shouldn\'t be...')