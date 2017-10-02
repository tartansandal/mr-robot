#! ./env/bin/python

import sys
from re import compile, X
from robot import Robot
from robot.command import parse, InvalidCommand


def main():
    """Run Mr Robot, run!

    Perform the robot simulation interactively."""
    robot = Robot()

    for line in sys.stdin:
        try:

            (cmd, coords) = parse(line)
            if cmd == 'PLACE':
                robot.place(coords)
            else:
                # Assume Robot has a method for each valid command.
                # (A potential weak point, but this is covered sufficiently by
                # the command_pattern testing)
                getattr(robot, cmd.lower())()

        except InvalidCommand:
            # Silently ignore invalid commands
            pass


if __name__ == "__main__":
    main()
