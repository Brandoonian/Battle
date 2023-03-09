Battle is a project that aims to replicate a popular turn-based game.
We will start in the simplest form, with no graphics using pygame.
Once completed in this form, we will upgrade to a more complete and interactive version.
Also, we will be starting with only three monsters with hopes of 
expanding that number once a version of the game has been completed in 
pygame. Here, I will lay out the steps in my plan to creating the game in it's first
and simplest form.

Step 1: Create main file which will greet the player, let them choose their monster,
and run the game. 

Step 2: Create classes for each monster assigning them characteristics such as HP and attacks
that will make the game fun and interesting.

Step 3: Create a function to assign the cpu a monster at random.

Step 4: Create a function that allows cpu to control monster in a way that
makes the game fun and interesting.

Step 5: Create a loop that will simulate a battle between the player and cpu
letting the player give the monster commands.

Step 6: Exit loop once battle is over and explain the results.

Step 7: Ask player if they would like to play again.



UPDATE: 3/9/2023


The stage of the game has been completed. I hae 3 playable character who can execute
4 attacks. The gameplay is not interesting or entertaining yet so that will be the next main objective.
In order to accomplish this goal, I will attempt to add additional effects and limitations 
on the individual attack techniques that the monsters have. My idea for additional effects include things like healing,
poison damage, disabling, and fortification. As for new limitations, I'm going to try to add
limits to the number of times an attack can be used within one battle. This will have an inverse relationship with 
the amount of damage that each attack does. The new steps are as follows: 

Step 1: Make a new file to store all attacks.

Step 2: Make classes for the current attacks that are included in the game (possibly changing the name of some attacks)

Step 3: Within each class, make methods that inflict damage on opponent. The amount of damage will be a random amount 
within a specified range.

Step 4: Within each class, make methods that track PP.

Step 5: Within each class, make methods that add secondary effects to attacks.

Step 6: Thorough testing to confirm if the game functions as designed.
