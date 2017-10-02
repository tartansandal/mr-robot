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
    """Simulate a robot moving on a 5x5 grid"""

    _position = None

    def place(self, coords):
        """Place robot at the specified position on the table"""
        try:
            self._position = Position(coords)
        except InvalidPosition:
            pass

    def move(self):
        """Move the robot one unit in the direction it is currently facing"""
        if not self._position:
            return

        c = self._position.coords()
        try:
            f = c['f']
            if f == 'NORTH':
                c['y'] += 1
            elif f == 'EAST':
                c['x'] += 1
            elif f == 'SOUTH':
                c['y'] -= 1
            elif f == 'WEST':
                c['x'] -= 1

            self._position = Position(c)
        except InvalidPosition:
            pass

    def left(self):
        """Rotate the robot 90 degrees to the left"""
        if not self._position:
            return

        c = self._position.coords()
        try:
            f = c['f']
            c['f'] = compass[f]['left']
            self._position = Position(c)
        except InvalidPosition:
            pass

    def right(self):
        """Rotate the robot 90 degrees to the right"""
        if not self._position:
            return

        c = self._position.coords()
        try:
            f = c['f']
            c['f'] = compass[f]['right']
            self._position = Position(c)
        except InvalidPosition:
            pass

    def report(self):
        """Print the current position of the robot"""
        if not self._position:
            return

        print(self._position)
