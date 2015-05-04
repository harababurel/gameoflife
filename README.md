![Game of Life Logo](http://i.imgur.com/FOG2tBV.png)
# gameoflife
graphic implementation of Conway's Game of Life.

<hr>

## requirements

firstly, you need to have python2.7 and pygame installed:
```console
sudo apt-get install python2.7 python-pygame
```

you need an initial configuration for the game. in order to generate one, run the following command:
```console
python2.7 state-generator.py
```

## configuration

all configurable settings are stored in `settings.cfg`. in order to change a setting, append a `key = value` line in the config file.
these are all the possible keys:


     key                 | default value  | note
     ------------------- |:---------------|:--------------------
     `height`            | `440`          | `height of the board (in pixels)`
     `width`             | `770`          | `width of the board (in pixels)`
     `bgRed`             | `115`          | `/`
     `bgGreen`           | `203`          | `| RGB value for the background`
     `bgBlue`            | `179`          | `\`
     `gridRed`           | `46`           | `/`
     `gridGreen`         | `159`          | `| RGB value for the gridlines`
     `gridBlue`          | `157`          | `\`
     `cellRed`           | `46`           | `/`
     `cellGreen`         | `159`          | `| RGB value for live cells`
     `cellBlue`          | `157`          | `\`
     `cellSize`          | `20`           | `size of each cell edge (in pixels)`
     `secondsInbetween`  | `0.05`         | `time gap between consecutive frames (in seconds)`
     `displayGrid`       | `1`            | `boolean value. whether or not to display gridlines`
