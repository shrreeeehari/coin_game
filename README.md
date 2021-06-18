# coin_game

The program is based on the following game:

There are N coins in a pile. There are two players, P1 and P2. Each take turn at picking coins from the pile. They can pick either one coin or two coins. The last player to pick coin(s) wins the game. 

For example, say N = 5 and Player P1 starts the game.

P1 picks 1 coin; 4 coins left.
P2 picks 1 coin; 3 coins left.

Now, no matter what P1 does, P2 will win. If P1 picks 1 coin then 2 coins are left. So now P2 can pick these coins and win. On the other hand, if P1 picks 2 coins then 1 coin is left. Again, P2 picks the last coin and so wins the game.

The progrm takes N (number of coins at the start of the game) as the input and generates all game steps in sequential order to find out the winner.

<h2>Winning strategies for players P1 and P2</h2>

<h4>For P1</h4>

If the number of coins initially is a multiple of 3,

i.e. if N%3 == 0, 

then P1 can never win the game (assuming equal intelligence for both player and assuming that P2 follows its winning strategy)

however if N is not a multiple of 3 then,

if N%3 == 1, then P1 is supposed to choose 1 coin or

if N%3 == 2, then P1 is supposed to choose 2 coins in order to win the game.


<h4>For P2</h4>

P2 should choose coins with the aim of making the count of the remaining coins to be a multiple of 3 at any point in the game.

However if the number of coins at the start of the game (N) is not a multiple of 3 and P1 follows its winning strategy (assuming equal intelligence for both players), then in such case P2 will never get a chance to implement its winning strategy and it will lose.
