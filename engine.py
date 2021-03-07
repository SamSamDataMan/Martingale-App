import random
from matplotlib import pyplot as plt


def handle_losing_spin(balance, bet):
    balance -= bet
    bet = bet * 2
    return balance, bet


def handle_winning_spin(balance, bet):
    balance += bet
    return balance


def spin_til_bust(trials, bankroll, startingBet, p_win, display_container):
    fig = plt.figure()
    # list containing lists of each trial's results.
    results_lists = []
    # iterate through trials.
    for trial in range(trials):
        trial_result = run_trial(bankroll, startingBet, p_win)
        results_lists.append(trial_result)
        plt.plot(trial_result, linewidth=1, alpha=0.5)
    x_max = 0
    for i in results_lists:
        listMax = len(i)
        if listMax > x_max:
            x_max = listMax
    plt.title("Figure 1: Profit Over Time")
    plt.ylabel("Profit ($)")
    plt.ylim(-2 * bankroll)
    plt.hlines(
        (-1 * bankroll),
        0,
        x_max,
        colors="Red",
        linestyles="solid",
        linewidth=2,
        label="Bankrupt",
    )
    plt.legend()
    plt.xlabel("Spin Count")
    plt.grid(b=True, which="major")
    display_container.pyplot(fig)
    return results_lists


def run_trial(
    bankroll,
    bet,
    p_win,
):
    # reset results list & starting balance.
    trial_result = []
    balance = bankroll
    # begin new trial.
    while True:
        # if subject is bankrupt, game is over.
        if balance < bet:
            # end trial by breaking while loop.
            break
        # otherwise, begin new martingale cycle.
        while True:
            # if current bankroll is sufficient for the next wager, SPIN:
            if balance >= bet:
                result = run_spin(p_win, bet)
                if result < 0:
                    bet *= 2
                balance += result
                trial_result.append(balance - bankroll)
            else:
                break
    return trial_result


# pass correct args to run_trial
# pass correct args to run_spin
def run_spin(p_win, bet):
    is_winner = random.random() < p_win
    return bet if is_winner else -1 * bet


def x_num_spins(trials, bankroll, startingBet, p_win, numSpins, display_container):
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
                print("New Martingale Cycle #", cycles)
            # control sims by number of spins
            while counter <= numSpins:
                if counter == numSpins:
                    break
                if balance >= bet:
                    # losing spin
                    if random.random() > p_win:
                        balance, bet = handle_losing_spin(balance, bet)
                        trialResult.append(balance - bankroll)
                        spins += 1
                        counter += 1
                    # winning spin
                    else:
                        balance = handle_winning_spin(balance, bet)
                        trialResult.append(balance - bankroll)
                        spins += 1
                        cycles += 1
                        counter += 1
                        break
                else:
                    print(
                        "You're Broke, Current Profit =",
                        balance - bankroll,
                        "current bet =",
                        bet,
                    )
                    break
        plt.plot(trialResult, linewidth=0.5, alpha=0.5)
    plt.title("Figure 1: Profit Over # of Spins")
    plt.grid(b=True, which="major")
    plt.ylabel("Profit ($)")
    plt.xlabel("Spin Count")
    plt.hlines(
        (-1 * bankroll),
        0,
        numSpins,
        colors="Red",
        linestyles="solid",
        linewidth=2,
        label="Bankrupt",
    )
    plt.legend()
    display_container.pyplot(fig)
    return resultsLists


def x_or_nothing(
    trials, bankroll, startingBet, p_win, multGoal: int, display_container
):
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
            if balance < bet or balance >= bankroll * multGoal:
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
                        trialResult.append(balance - bankroll)
                    # winning spin
                    else:
                        balance = handle_winning_spin(balance, bet)
                        trialResult.append(balance - bankroll)
                        break
                else:
                    break
        plt.plot(trialResult, linewidth=1, alpha=0.5)
    x_max = 0
    for i in resultsLists:
        listMax = len(i)
        if listMax > x_max:
            x_max = listMax
    plt.title("Figure 1: Profit Over Time")
    plt.ylabel("Profit ($)")
    plt.ylim(-1.2 * bankroll)
    plt.hlines(
        (-1 * bankroll),
        0,
        x_max,
        colors="Red",
        linestyles="solid",
        linewidth=2,
        label="Bankrupt",
    )
    plt.hlines(
        ((multGoal * bankroll) - bankroll),
        0,
        x_max,
        colors="Green",
        linestyles="solid",
        linewidth=2,
        label="Achieved Goal",
    )
    plt.legend()
    plt.xlabel("Spin Count")
    plt.grid(b=True, which="major")
    display_container.pyplot(fig)
    return resultsLists
