#! ./env/bin/python

import sys
from re import compile, X
from robot import Robot
from robot.position import InvalidPosition


class InvalidCommand(Exception):
    """Raised when an invalid command is given"""
    pass


# We assume (although it is not specified) that commands must strictly match
# the specification, i.e., leading or trailing spaces are not allowed, commands
# are case sensitive, exactly one space between the PLACE command and its
# arguments.  We could tighten this even further by limiting values of the
# input x and y coordinates, however, that is not made explicit in the
# specification.
command_pattern = compile(
    r"""
        ^                                     # start
        (?P<cmd>MOVE|LEFT|RIGHT|REPORT|PLACE) # command
        (?:
            \s                           # space
            (?P<x>\d+),                  # x coord
            (?P<y>\d+),                  # y coord
            (?P<f>NORTH|EAST|SOUTH|WEST) # facing
        )?
        $                                     # end
        """, X
)


def parse(line):
    """Parse one command line and return valid components

    An exception is raised if the line does not correspond to a valid command
    string.
    """

    valid = command_pattern.search(line)
    if not valid:
        raise InvalidCommand()

    coords = None
    cmd = valid.group('cmd')
    if cmd == 'PLACE':
        coords = dict(
                x=int(valid.group('x')),  # regexp ensures the str is a digit
                y=int(valid.group('y')),
                f=valid.group('f'),
                )

    return cmd, coords


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
