from run import main, parse

import fileinput


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
    def test_run_example_a(self, monkeypatch, capsys):
        def example():
            yield "PLACE 0,0,NORTH\n"
            yield "MOVE\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "0,1,NORTH\n"

    def test_run_example_b(self, monkeypatch, capsys):
        def example():
            yield "PLACE 0,0,NORTH\n"
            yield "LEFT\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "0,0,WEST\n"

    def test_run_example_c(self, monkeypatch, capsys):
        def example():
            yield "PLACE 1,2,EAST\n"
            yield "MOVE\n"
            yield "MOVE\n"
            yield "LEFT\n"
            yield "MOVE\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "3,3,NORTH\n"
