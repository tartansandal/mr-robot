from robot.position import Position, InvalidPosition

# XXX big temptation to implement direction as a ring, but there are only
# 4 cases, so a simple swith is probably less code and confusion


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
                new = Position(x - 1, y, f)
            elif f == 'SOUTH':
                new = Position(x, y - 1, f)
            elif f == 'WEST':
                new = Position(x + 1, y, f)
            self._position = new
        except InvalidPosition:
            pass

    def left(self):
        """Rotate the robot 90 degrees to the left"""
        if not self._position:
            return

        (x, y, f) = self._position.tuple()

        if f == 'NORTH':
            new = Position(x, y, 'EAST')
        elif f == 'EAST':
            new = Position(x, y, 'SOUTH')
        elif f == 'SOUTH':
            new = Position(x, y, 'WEST')
        elif f == 'WEST':
            new = Position(x, y, 'NORTH')
        else:
            raise InvalidPosition

        self._position = new

    def right(self):
        """Rotate the robot 90 degrees to the right"""
        if not self._position:
            return

        (x, y, f) = self._position.tuple()
        if f == 'NORTH':
            new = Position(x, y, 'WEST')
        elif f == 'WEST':
            new = Position(x, y, 'SOUTH')
        elif f == 'SOUTH':
            new = Position(x, y, 'EAST')
        elif f == 'EAST':
            new = Position(x, y, 'NORTH')
        else:
            raise InvalidPosition

        self._position = new

    def report(self):
        """Print the current position of the robot"""
        if not self._position:
            return
        print(self._position)
