Your task this week is to guide our agent to a treasure hidden at the bottom of the ocean.

You can play the game in discovery mode (without help) by typing:

	python treasurehunt.py 6 discovery
To play the game on a bigger grid, you can try:

	python treasurehunt.py 10 discovery
Click on the 'SONAR' button to start taking sonar measurements. When you are ready to make a decision and dive, click on the 'DIVE' button.

Your task is to help the player/agent find the treasure more reliably by implementing the following:

1. The update method in the beliefs.py module. The Belief class is used to track the belief distribution (where we think the treasure is) based on the sonar sensing evidence we have so far.
The distribution is initialized to a uniform distribution in _init_. Your task is to update it with each evidence. Don't forget to normalize!
To see the distribution on the grid, start the game in 'guided' (default) mode:
		python treasurehunt.py 8 guided

2. The recommend_sensing method in the beliefs.py module. The method returnw the position where we should take the next sonar measurement in the grid. The position should be the most promising unobserved location. If all remaining unobserved locations have a probability of 0, the method should return the unobserved location that is closest to the (observed) location with the highest probability. The recommended location is displayed in purple on the grid ­ as shown in the screenshot below.
![Screenshot]()