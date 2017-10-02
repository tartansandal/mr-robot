from robot.position import Position, InvalidPosition

# XXX big temptation to implement direction as a ring, but there are only
# 4 cases, so a simple switch is probably less code and confusion

compass = {
    'NORTH': {
        'left': 'WEST',
        'right': 'EAST'
    },
    'WEST': {
        'left': 'SOUTH',
        'right': 'NORTH'
    },
    'SOUTH': {
        'left': 'EAST',
        'right': 'WEST'
    },
    'EAST': {
        'left': 'NORTH',
        'right': 'SOUTH'
    },
}


class Robot():
    _position = None

    def place(self, args):
        """Place robot at the specified position on the table"""
        try:
            self._position = Position(**args)
        except InvalidPosition:
            pass

    def move(self):
        """Move the robot one unit in the direction it is currently facing"""
        if not self._position:
            print('ERROR')
            return

        (x, y, f) = self._position.tuple()
        try:
            if f == 'NORTH':
                new = Position(x, y + 1, f)
            elif f == 'EAST':
                new = Position(x + 1, y, f)
            elif f == 'SOUTH':
                new = Position(x, y - 1, f)
            elif f == 'WEST':
                new = Position(x - 1, y, f)
            self._position = new
        except InvalidPosition:
            pass

    def left(self):
        """Rotate the robot 90 degrees to the left"""
        if not self._position:
            return

        (x, y, f) = self._position.tuple()
        self._position = Position(x, y, compass[f]['left'])

    def right(self):
        """Rotate the robot 90 degrees to the right"""
        if not self._position:
            return

        (x, y, f) = self._position.tuple()
        self._position = Position(x, y, compass[f]['right'])

    def report(self):
        """Print the current position of the robot"""
        if not self._position:
            return
        print(self._position)
