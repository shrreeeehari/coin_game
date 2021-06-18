# coin_game

The program is based on the following game:

There are N coins in a pile. There are two players, P1 and P2. Each take turn at picking coins from the pile. They can pick either one coin or two coins. The last player to pick coin(s) wins the game. 

For example, say N = 5 and Player P1 starts the game.

P1 picks 1 coin; 4 coins left.
P2 picks 1 coin; 3 coins left.

Now, no matter what P1 does, P2 will win. If P1 picks 1 coin then 2 coins are left. So now P2 can pick these coins and win. On the other hand, if P1 picks 2 coins then 1 coin is left. Again, P2 picks the last coin and so wins the game.

The progrm takes N (number of coins at the start of the game) as the input and generates all game steps in sequential order to find out the winner.
