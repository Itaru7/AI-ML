Your task this week is to implement an AI agent who plays a perfect (or near perfect) game of an arbitrary sized Tic Tac Toe.

You can play and win a game (of any size) against a non-optimal AI agent who picks moves randomly:

	python tictactoe.py 6 rand

Note that if you have both Python 2 and Python 3 installed, you may need to type:

	python3 tictactoe.py 6 rand

As you can see below, this is not a challenging game to play.

![Screenshot]()

Your task is to implement an AI agent who will play a better game.

1. Implement the minimax algorithm by filling in your code in the following 4 functions in adversarial_search.py:
*minimax, value, max_value and min_value.*
You can test your minimax code on a 3x3 Tic Tac Toe as follows:

		python tictactoe.py 3 minimax
    Make sure your minimax agent is unbeatable. If you are somehow able to win, that is an indication that your implementation is not correct and you will get no points for this question.

    Even though your agent plays a perfect game and cannot be defeated, it searches the entire tree from the current game state to find the best move. The program prints the number of nodes evaluated with each move. Here are the number of nodes evaluated when I play the following game:

    ![Screenshot]()

        Number of nodes evaluated so far: 59,704
        Number of nodes evaluated so far: 60,630
        Number of nodes evaluated so far: 60,690
        Number of nodes evaluated so far: 60,694
        Total number of nodes evaluated: 60,694
    Note that the number of nodes will be different for each game ­ but of the same order of magnitude (around 60,000).

    You can try your minimax agent with a 4x4 Tic Tac Toe but you'll see that it takes too long to decide on a single move. We'll have to do better.

2. Implement the minimax algorithm with Alpha Beta pruning by filling in your code in the following 4 functions in adversarial_search.py: alphabeta, ab_value, abmax_value and abmin_value. You can test your Alpha Beta code on a 3x3 Tic Tac Toe as follows:
		python tictactoe.py 3 alphabeta
**Make sure that your agent is still unbeatable. If you are somehow able to win, that is an indication that your implementation is not correct. **
You will see that the game is much faster now and the number of nodes expanded has been significantly reduced. Here are the number of nodes evaluated when I play the game shown in the previous question:
		Number of nodes evaluated so far: 4,089
		Number of nodes evaluated so far: 4,367
		Number of nodes evaluated so far: 4,419
		Number of nodes evaluated so far: 4,423
		Total number of nodes evaluated: 4,423
However we are still unable to play a 4x4 Tic Tac Toe.

3. Implement a depth limited alpha beta algorithm by filling in your code in the following 4 functions in adversarial_search.py: abdl, abdl_value, abdlmax_value and abdlmin_value. You can use the evaluation
function that has been implemented for you in tictactoe.py (the eval method in GameState class) to evaluate non terminal nodes. However for the terminal nodes (win, tie and lose) you will have to decide on values that are consistent with the values retuned by eval. Make sure you understand what eval is doing first.

    You can test your implementation code on a 4x4 Tic Tac Toe and with a depth of 6 as follows:

        python tictactoe.py 4 abdl 6

    Here are the number of nodes evaluated when I play the following game:

    ![Screenshot]()

        Number of nodes evaluated so far: 494,057
        Number of nodes evaluated so far: 819,244
        Number of nodes evaluated so far: 862,025
        Number of nodes evaluated so far: 903,412
        Number of nodes evaluated so far: 906,785
        Number of nodes evaluated so far: 906,944
        Number of nodes evaluated so far: 906,957
        Number of nodes evaluated so far: 906,958
        Total number of nodes evaluated: 906,958

    You will find that your agent is still unbeatable. You can even test your implementation on a 7x7 Tic Tac Toe with a depth of 3 as follows:

        python tictactoe.py 7 abdl 3
    What depth do you have to go down to to beat your abdl agent?

    To make sure that you are handling the depth correctly, test your algorithm with a depth of 0. How many nodes are evaluated after you play your first move? For a 4x4 game, 15 nodes should be evaluated.