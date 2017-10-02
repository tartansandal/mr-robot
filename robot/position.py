# These module level constants are used to restrict the possible positions on
# the table

# FIXME make these sets read_only -- not sure there is such a thing in python
x_range = {0, 1, 2, 3, 4}
y_range = {0, 1, 2, 3, 4}
f_range = {'NORTH', 'EAST', 'SOUTH', 'WEST'}


class Position():
    _x = None
    _y = None
    _f = None

    def __init__(self, c):
        if c['x'] in x_range and c['y'] in y_range and c['f'] in f_range:
            self._x = c['x']
            self._y = c['y']
            self._f = c['f']
        else:
            raise InvalidPosition

    def coords(self):
        return dict(x=self._x, y=self._y, f=self._f)

    def __str__(self):
        return "{},{},{}".format(self._x, self._y, self._f)


class InvalidPosition(Exception):
    """Raised when a position is specified that does not fit on the table"""
    pass
