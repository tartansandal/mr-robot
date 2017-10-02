from re import compile, X

# We assume (although it is not specified) that commands must strictly match
# the breif, i.e., leading or trailing spaces are not allowed, commands are
# case sensitive, exactly one space between the PLACE command and its
# arguments.  We could tighten this even further by limiting values of the
# input x and y coordinates, however, that is not made explicit in the brief.
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


class InvalidCommand(Exception):
    """Raised when an invalid command is given"""
    pass
