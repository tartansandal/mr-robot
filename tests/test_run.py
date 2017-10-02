from run import main, parse


class TestParsing:
    def test_valid_place_cmd(self):
        (cmd, args) = parse('PLACE 1,2,NORTH\n')
        assert cmd == 'PLACE'
        assert args['x'] == 1
        assert args['y'] == 2
        assert args['f'] == 'NORTH'

    def test_valid_move_cmd(self):
        (cmd, args) = parse('MOVE\n')
        assert cmd == 'MOVE'
        assert args == None

    def test_valid_left_cmd(self):
        (cmd, args) = parse('LEFT\n')
        assert cmd == 'LEFT'
        assert args == None

    def test_valid_right_cmd(self):
        (cmd, args) = parse('RIGHT\n')
        assert cmd == 'RIGHT'
        assert args == None

    def test_valid_report_cmd(self):
        (cmd, args) = parse('REPORT\n')
        assert cmd == 'REPORT'
        assert args == None

    # FIXME test some invalid values


class TestRuntime:
    # FIXME howto test command line and file stuff
    # do I have to monkey patch input?
    # do I have to fork and actually run the test?
    # should I use a fixture for that?

    def test_run_example_a(self):
        pass

    def test_run_example_b(self):
        pass

    def test_run_example_c(self):
        pass
