"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    count = 0
    total = 0
    if_one = False
    while (count < num_rolls):
        temp = dice()
        if temp == 1:
            if_one = True
        total += temp
        count += 1
    if if_one:
        return 1
    return total

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if num_rolls == 0:
        tens = opponent_score//10
        ones = opponent_score%10
        return abs(tens - ones) + 1
    return roll_dice(num_rolls,dice)

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    total = score + opponent_score
    if (total%7 == 0):
        return four_sided
    return six_sided

def bid_for_start(bid0, bid1, goal=GOAL_SCORE):
    """Given the bids BID0 and BID1 of each player, returns three values:

    - the starting score of player 0
    - the starting score of player 1
    - the number of the player who rolls first (0 or 1)
    """
    assert bid0 >= 0 and bid1 >= 0, "Bids should be non-negative!"
    assert type(bid0) == int and type(bid1) == int, "Bids should be integers!"

    # The buggy code is below:
    # if bid0 == bid1:
    #     return 0, goal, goal
    # elif bid0 == (bid1 - 5):
    #     return 0, 0, 0
    # elif bid1 == (bid0 + 5):
    #     return 10, 0, 1
    # elif bid1 > bid0:
    #     return bid1, bid0, 0
    # else:
    #     return bid0, bid1, 1

    if bid0 == bid1:
        return goal, goal, 0
    elif bid0 == (bid1 - 5):
        return 0, 10, 1
    elif bid0 == (bid1 + 5):
        return 10, 0, 0
    elif bid1 > bid0:
        return bid1, bid0, 1
    else:
        return bid1, bid0, 0

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    while (score0 < goal and score1 < goal):
    # if True:
        dice, num_rolls = 0, 0
        if who == 0:
            dice = select_dice(score0, score1)
            num_rolls = strategy0(score0, score1)
            score0 += take_turn(num_rolls, score1, dice)
        else:
            dice = select_dice(score1, score0)
            num_rolls = strategy1(score1, score0)
            score1 += take_turn(num_rolls, score0, dice)

        if (score0 == 2*score1 or score1 == 2*score0):
            temp = score0
            score0 = score1
            score1 = temp
        who = other(who)
    return score0, score1  # You may want to change this line.

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=10000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    def average(*args):
        count = 0
        total = 0
        while (count < num_samples):
            total += fn(*args)
            count += 1
        ave = total/num_samples
        return ave
    return average

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Assume that dice always
    return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    highest = 1
    highest_ave = 0
    count = 1
    while (count < 11):
        ave = make_averaged(roll_dice)(count, dice)
        if ave > highest_ave:
            highest = count
            highest_ave = ave
        count += 1
    return highest


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # testing percentage chance certain scores will show up
        def last():    
            def perc_value(value, num_rolls, dice=six_sided):
                count = 0
                num_values = 0
                while (count < 3000000):
                    if(roll_dice(num_rolls, dice)==value):
                        num_values +=1
                    count +=1
                perc = num_values / count
                if (perc!=0):
                    if dice == six_sided:
                        string = "six_sided"
                    elif dice == four_sided:
                        string = "four_sided"
                    print("%", value, "returned for", string, "dice rolled", num_rolls, "times:", perc)
                return perc
            
            def run_perc_value(dice=six_sided):
                val = 1
                n_roll = 1
                if False:
                    while(val<=60):
                        while(n_roll<=10):
                            if(n_roll*2<val or val==1):
                                perc_value(val,n_roll,dice)
                            n_roll+=1
                        print("**************************************************")
                        n_roll=1
                        val+=1
                if True:
                    while(n_roll<=10):
                        while(val<=n_roll*6):
                            if(n_roll*2<=val or val==1):
                                perc_value(val,n_roll,dice)
                            val+=1
                        print("**************************************************")
                        val=1
                        n_roll+=1
                print("**************************************************")
                print("**************************************************")
                print("**************************************************")
            run_perc_value()
            print("**************************************************")
            run_perc_value(four_sided)
            print("**************************************************")
        last()
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(5) win rate:', average_win_rate(always_roll(5)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if False: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
    if False:
        print('hh testing win rate:', average_win_rate(testing))
    "*** You may add additional experiments as you wish ***"

# Strategies

def testing(score, opponent_score, margin=8, num_rolls=5):
    return 0
def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    sum_digits = abs(opponent_score//10 - opponent_score%10) + 1
    if sum_digits >= margin:
        return 0
    return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least MARGIN points and rolls
    NUM_ROLLS otherwise.
    """

    sum_digits = abs(opponent_score//10 - opponent_score%10) + 1
    sum = score + sum_digits
    if (sum == 2*opponent_score):
        return num_rolls
    elif (sum == 0.5*opponent_score):
        return 0
    return bacon_strategy(score, opponent_score, margin, num_rolls)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """

    sum_digits = abs(opponent_score//10 - opponent_score%10) + 1
    bacon = bacon_strategy(score, opponent_score, 8, 6)
    swap = swap_strategy(score, opponent_score, 8, 6)

    if ((score + sum_digits) >= 100 and swap < 1):
        return bacon

    elif (score > 95 and opponent_score < 50):
        return 10

    elif swap == 0:
        if (abs(opponent_score - score) < 15):
            return 6
        else:
            return swap

    elif ((score + 1) == 0.5*opponent_score):
        if (abs(opponent_score - score) < 15):
            return 6
        else:
            return 10

    # elif ((score + sum_digits + opponent_score)%7 == 0):
    #     return bacon
    # elif ((score + opponent_score + 1)%7 == 0):
    #     return 10

    elif (select_dice(score, opponent_score) == six_sided):
        if score < 50:
            return 7
        elif (score > 80 and swap < 1):
            return 2
        else:
            return 5

    elif (select_dice(score, opponent_score) == four_sided):
        if score < 50:
            return 5
        elif (score > 80 and swap < 1):
            return 1
        else:
            return 3


    # elif (select_dice(score, opponent_score) == four_sided):
    #     if (score >= 80):
    #         return bacon
    #     else:
    #         return 4


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
