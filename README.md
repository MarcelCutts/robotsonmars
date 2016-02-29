# Robots on Mars
[![Build Status](https://travis-ci.org/MarcelCutts/robotsonmars.svg?branch=master)](https://travis-ci.org/MarcelCutts/robotsonmars)

Instruct brave little robots to fearlessly adventure across Mars.

Each robot is represented by some data in a text file, that then tries to navigate Mars like Turtle games of old. There's danger and excitement, as Robots can fly off the edge of this strangely rectangular Euclidean world.

Command your robots today!

## Getting up and running

1. Ensure you have **Python 2.7** installed
2. Pull or download this repo
3. In the project's root, run `python main.py`

That's all there is, no need for any extra packages.

## I'm just here because I love tests

Got you covered. Follow the _Getting up and running_ instructions. Then, in the project directory, run

```python -m unittest discover```

## Writing your own instructions

Want to move beyond the provided basic instructions? Here are the rules for writing your own.

The first line of input is the upper-right coordinates of the rectangular world, the lower-left coordinates are assumed to be 0, 0.

The remaining input consists of a sequence of robot positions and instructions (two lines per robot). A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all separated by whitespace on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line.

Each robot is processed sequentially, i.e., finishes executing the robot instructions before the next robot begins execution.

## Assumptions
This is a very basic piece of code, so sometimes the analogy of robots on Mars breaks down. These include, but are not limited to
+ No collision detection between robots
+ Validation exists, but it is in no way bulletproof
+ The euclidean plane of Mars is positive only
