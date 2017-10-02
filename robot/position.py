# These module level constants are used to restrict the possible positions on
# the table

# FIXME make these sets read_only
x_range = {0, 1, 2, 3, 4}
y_range = {0, 1, 2, 3, 4}
f_range = {'NORTH', 'EAST', 'SOUTH', 'WEST'}


class Position():
    _x = None
    _y = None
    _f = None

    def __init__(self, x, y, f):
        if x in x_range and y in y_range and f in f_range:
            self._x = x
            self._y = y
            self._f = f
        else:
            raise InvalidPosition

    # is there another way? __getitem__?
    def tuple(self):
        return self._x, self._y, self._f

    def __str__(self):
        return "{},{},{}".format(self._x, self._y, self._f)


class InvalidPosition(Exception):
    """Raised when a position is specified that does not fit on the table"""
    pass
