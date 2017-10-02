#! ./env/bin/python

import sys
from re import compile, X
from robot import Robot


class InvalidCommand(Exception):
    pass


# We assume (although it is not specified) that commands must strictly match the
# specification, i.e., leading or trailing spaces are not allowed, commands are
# case sensitive, exactly one space between the PLACE command and its arguments.
# We could tighten this even further by limiting values of the input x and
# y coordinates, however, that is not made explicit in the specification.
command_pattern = compile(
    r"""
        ^                                    # start
        (?P<cmd>
            MOVE   |
            LEFT   |
            RIGHT  |
            REPORT |
            PLACE                            # command
            (?=                              # ...with args
                \s                           # space
                (?P<x>\d+),                  # x coord
                (?P<y>\d+),                  # y coord
                (?P<d>NORTH|EAST|SOUTH|WEST) # direction
                )
            )
        $                                    # end
        """, X
)


def parse(line):
    """Parse one command line and return valid components

    An exception is raised if the line does not correspond to a valid command
    string
    """

    # NB: we use search instead of match so we don't have to strip EOL chars
    valid = command_pattern.search(line)
    if not valid:
        raise InvalidCommand()

    cmd = valid.group('cmd')
    args = dict(
        x=int(valid.group('x')),  # regexp ensures the string is a digit
        y=int(valid.group('y')),
        d=valid.group('d'),
    )

    return cmd, args


def main():
    """Run robot, run!

    """

    robot = Robot()

    for line in sys.stdin:
        try:
            (cmd, args) = parse(line)
            if cmd == 'PLACE':
                robot.place(args)
            else:
                # Assume Robot has a method for each valid command
                getattr(robot, cmd.lower())()
        except InvalidCommand:
            # Silently ignore invalid commands
            pass


if __name__ == "__main__":
    main()
