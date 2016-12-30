A simple snake game!


Known bugs:

 * Making a U-turn too fast will cause the program to not update the first
    position in time for the second input. This causes the game to think that
    the head collides with the tail and will result in the game thinking you
    lost.
        Solution (not really): Don't input 2 keys that will cause a
         u-turn  within ~0.1 s.
