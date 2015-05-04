![Game of Life Logo](http://i.imgur.com/FOG2tBV.png)
# gameoflife
graphic implementation of Conway's Game of Life.

<hr>
## inspiration
the fact that such a fixed initial configuration and a simple set of rules can make a system behave so chaotically determined me to implement and test it by myself.

rules of the game (explained by its creator [here](https://www.youtube.com/watch?v=R9Plq-D1gEk) and [here](https://www.youtube.com/watch?v=E8kUJL04ELA)):
* the game is a [zero-player game](http://en.wikipedia.org/wiki/Zero-player_game)
* it is played on an infinte two-dimensional orthogonal grid of squre cells
* each cell is in one of two possible states: **alive** or **dead**
* every cell interacts with its eight neighbours (cells situated at the distance of one unit)
* at each step in time, the following transitions occur:
    * any live cell with fewer than two live neighbours dies, as if caused by under-population
    * any live cell with two or three live neighbours lives on to the next generation
    * any live cell with more than three live neighbours dies, as if by overcrowding
    * any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
* the initial pattern constitutes the seed of the system
* the first generation is created by applying the above rules simultaneously to every cell in the seed (births and deaths occur simultaneously)

## requirements

firstly, you need to have python2.7 and pygame installed:
```console
sudo apt-get install python2.7 python-pygame
```

you need an initial configuration for the game. in order to generate one, run the following command:
```console
python2.7 state-generator.py
```

also, be sure to check the `settings.cfg` file for any alteration to the user preferences.
finally, you can run the simulator with the following command:
```console
python2.7 main.py
```

## configuration

all configurable settings are stored in `settings.cfg`.
in order to change a setting, append a `key value` line in the config file.
these are all the possible keys:


     key                 | default value  | note
     ------------------- |:---------------|:----------------------------------------------------
     `height`            | `440`          | `height of the board (in pixels)`
     `width`             | `770`          | `width of the board (in pixels)`
     `bgRed`             | `115`          | `/-----------------------------`
     `bgGreen`           | `203`          | `| RGB value for the background`
     `bgBlue`            | `179`          | `\-----------------------------`
     `gridRed`           | `46`           | `/----------------------------`
     `gridGreen`         | `159`          | `| RGB value for the gridlines`
     `gridBlue`          | `157`          | `\----------------------------`
     `cellRed`           | `46`           | `/-------------------------`
     `cellGreen`         | `159`          | `| RGB value for live cells`
     `cellBlue`          | `157`          | `\-------------------------`
     `cellSize`          | `20`           | `size of each cell edge (in pixels)`
     `secondsInbetween`  | `0.05`         | `time gap between consecutive frames (in seconds)`
     `displayGrid`       | `1`            | `boolean value. whether or not to display gridlines`
