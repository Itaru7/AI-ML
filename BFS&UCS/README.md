Your task this week is to help Sammy the Spartan on a quest to collect all the medals found in a maze.

You can see how the depth, first algorithm graph solves the quest in the quest defined in sjsu.txt by running:

    python spartanquest.py sjsu.txt dfs
Note if you have both Python 2 and Python 3 installed, you may need to type:

    python3 spartanquest.py sjsu.txt dfs
As you can see below, this is not an efficient way for our mascot to collect the medals.
![Screenshot](https://github.com/Itaru7/AI-ML/blob/master/BFS%26UCS/Screen%20Shot.png)
Your task is to help Sammy the Spartan find a more efficient solution by implementing:

1. the **breadth-first search graph algorithm** by filling in your code in the function **bfs** in the Python module uninformed_search.py.

2. **the uniform cost search graph algorithm** by filling in your code in the function **ucs** in the Python module uninformed_search.py. Note that Sammy is always facing West and it is more difficult for him to move backward (East) than forward (West). There is also a slight hill so moving North is slightly more difficult than moving South. The costs associated with each move are listed in spartanquest.py:

		cost = {WEST: 1, SOUTH: 1, EAST: 6, NORTH: 2}

Even though you need all the files to test your program, you only need to upload your solution in uninformed_search.py.

The program prints some statistics that measure the efficiency of your solutions. Here are the expected results for the quest described in sjsu.txt:

python spartanquest.py sjsu.txt bfs

    Path length: 45
    Path cost: 157
    Number of nodes expanded: 533 <-- or 507
    Processing time: 0.0082 (sec) <-- this will be different on your machine

python spartanquest.py sjsu.txt ucs

    Path length: 52
    Path cost: 144
    Number of nodes expanded: 553
    Processing time: 0.0090 (sec) . <-- this will be different on your machine