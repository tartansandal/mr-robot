# Mr Robot - Toy Robot Simulator

## Description

This is a simple command line application described by
[specification.md](specification.md)

## Preamble

This coding challenge was origionally designed by Jon Eaves in 2007 while recruiting for ANZ. See

    https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/

for a nice break down of its intent and limitations as a filtering tool for
recruitment purposes.

Ostensibly, it is a Object Oriented programing task with a clear focus on
testing, which is typical of its time. A more modern challenge might have
a stronger focus on user iterfaces, services, data, or even functional
programming, however, it still a prefectly adequate filtering tool.

A quick google search shows a number of attempts at this challenge in
a variety of languages. The first Python attempt I came across was:

    https://github.com/jessehon/robot-simulator

which seems to be a fairly adequate solution in Python 2.

I will attempt to do this Python 3 using more modern tooling.

### Initial Plan

* Use Python 3

* Test using pytest

* Use a virtual env and pip

* Not distributing a library, so no need for setuptools

* There is bound to be a command line parser that supports both interactive
  and streaming input. Although its pretty simple, I would rather not reinvent
  that wheel. _Edit: Looking around, it seems a simple regexp matcher will do fine --
  anything else is overkill._

* I can't really see anyway around having a class for the coordinates on the
  table. We can build a lot of the key constraints into that class.  Having
  (essentially singleton) classes for Robot and Table seems to be namespace
  overkill.  We can create them later if the problem changes to include
  multiple Tables or Robots. _Edit: Ended up with a singleton class for Robot
  since it made some tests cleaner. Still not sure if its really necessary_

* I would love to throw a generator into this somehow, just to show off, but
  I can't see how we would do that in any meaningful way.

## Usage

This is a coding challenge so we do not expect it to be installed on any
system or distrubuted in anyayh other than a git checkout.

To setup your virtual environment:

    make env

To activate your virtual environment:

    source env/bin/activate

To run tests:

    make test

To run the simulator interactively:

    ./run.py


... and I'm bored about now :-)

