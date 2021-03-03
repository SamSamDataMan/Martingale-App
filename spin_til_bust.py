import random
from matplotlib import pyplot as plt


def spin_til_bust(trials, bankroll, startingBet, p_win, display_container):
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
    display_container.pyplot(fig)
    return resultsLists