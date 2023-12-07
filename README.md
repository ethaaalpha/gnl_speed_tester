# gnl_speed_tester

## What's the goal
This project has been designed make **run** multiples _get_next_line_ and calculate the fatest one !<br>

## How run to it 
Just **git clone** the projet, then you'll need to have **python3**. <br>
In a bash terminal, at the **root project** run `python3 main.py <where are located all the gnls>` <br>

## Structure of gnl's folder
The *input folder* that you will give to the program for running it should be **structured** like that : <br>
-- *folder*<br>
--- *gnlA*<br>
----- get_next_line.c<br>
----- get_next_line.h<br>
----- get_next_line_utils.c<br>
--- *gnlB*<br>
----- get_next_line.c<br>
----- get_next_line.h<br>
----- get_next_line_utils.c<br>
--- .. <br>
--

## Informations
This program could be long to run depending on the tests because it doesn't do **multi threading**.<br>