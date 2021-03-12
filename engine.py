import random
from matplotlib import pyplot as plt


def handle_losing_spin(balance, bet):
    balance -= bet
    bet = bet * 2
    return balance, bet


def handle_winning_spin(balance, bet):
    balance += bet
    return balance


def run_trial(bankroll, bet, p_win, numSpins=10000000, multGoal=10000000):
    # reset results list & starting balance.
    trial_result = []
    balance = bankroll
    starting_bet = bet
    counter = 0
    # begin new trial.
    while balance > 0 and counter < numSpins and balance < multGoal:
        # if current bankroll is sufficient for the next wager, SPIN:
        if balance >= bet:
            result = run_spin(p_win, bet)
            counter += 1
            print("Spin Count", counter, "balance =", balance)
            # TODO: Refactor to ternary (one line if else)
            if result < 0:
                bet *= 2
                print("lose")
            else:
                bet = starting_bet
                print("win")
            balance += result
            print('new balance=', balance)
            trial_result.append(balance - bankroll)
        elif balance < starting_bet:
            bet = balance
        else:
            bet = starting_bet
    return trial_result


def run_spin(p_win, bet):
    is_winner = random.random() < p_win
    return bet if is_winner else -1 * bet


def spin_til_bust(trials, bankroll, startingBet, p_win, display_container):
    fig = plt.figure()
    # list containing lists of each trial's results.
    results_lists = []
    # iterate through trials.
    for trial in range(trials):
        trial_result = run_trial(bankroll, startingBet, p_win)
        results_lists.append(trial_result)
    x_max = 0
    for trial_result in results_lists:
        plt.plot(trial_result, linewidth=1, alpha=0.5)
        listMax = len(trial_result)
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


def x_num_spins(trials, bankroll, startingBet, p_win, numSpins, display_container):
    fig = plt.figure()
    results_lists = []
    spin_count = numSpins
    # number of subjects to repeat trial for
    for trial in range(trials):
        trial_result = run_trial(bankroll, startingBet, p_win, numSpins)
        results_lists.append(trial_result)
    x_max = 0
    for trial_result in results_lists:
        plt.plot(trial_result, linewidth=0.5, alpha=0.5)
        listMax = len(trial_result)
        if listMax > x_max:
            x_max = listMax
    plt.title("Figure 1: Profit Over # of Spins")
    plt.grid(b=True, which="major")
    plt.ylabel("Profit ($)")
    plt.xlabel("Spin Count")
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
    display_container.pyplot(fig)
    return results_lists


def x_or_nothing(trials, bankroll, startingBet, p_win, multGoal: int, display_container):
    fig = plt.figure()
    tcount = 1
    # list containing lists of each trial's results.
    results_lists = []
    # iterate through trials.
    for trial in range(trials):
        trial_result = run_trial(bankroll, startingBet, p_win, multGoal)
        results_lists.append(trial_result)
        print("New Trial, #", tcount)
        tcount += 1
    x_max = 0
    for trial_result in results_lists:
        plt.plot(trial_result, linewidth=0.5, alpha=0.5)
        listMax = len(trial_result)
        if listMax > x_max:
            x_max = listMax
    plt.title("Figure 1: Profit Over Time")
    plt.ylabel("Profit ($)")
    plt.ylim(-1.2 * bankroll, bankroll*multGoal)
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
    return results_lists
