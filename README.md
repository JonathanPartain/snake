A simple snake game!

Installation (Linux):
 1 Make sure you have pygame installed
 2 Download or clone into directory of your choice
 3 $chmod +x snake.py
 4 $./snake.py
 5 Enjoy!





Known bugs:

 * Making a U-turn too fast will cause the program to not update the first
    position in time for the second input. This causes the game to think that
    the head collides with the tail and will result in the game thinking you
    lost.



 * Solution (not really): Don't input 2 keys that will cause a
     u-turn  within ~0.1 s.
