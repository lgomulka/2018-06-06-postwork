'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle


class TurtleCommand:
    def __init__(self, args):
        self.args = args

    def run(self):
        raise NotImplementedError


class ForwardCommand(TurtleCommand):
    def run(self):
        turtle.forward(int(self.args))


class RightCommand(TurtleCommand):
    def run(self):
        turtle.right(int(self.args))


class LeftCommand(TurtleCommand):
    def run(self):
        turtle.left(int(self.args))


class HomeCommand(TurtleCommand):
    def run(self):
        turtle.home(int(self.args))


class CircleCommand(TurtleCommand):
    def run(self):
        turtle.circle(int(self.args))


class PositionCommand(TurtleCommand):
    def run(self):
        print('Current position is %d %d\n' % turtle.position())


class HeadingCommand(TurtleCommand):
    def run(self):
        print('Current heading is %d\n' % (turtle.heading(),))


class ResetCommand(TurtleCommand):
    def run(self):
        turtle.reset()


class TurtleRecorder(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def __init__(self):
        super().__init__()
        self._macro = []
        self._recording = False

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        self.run(ForwardCommand(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        self.run(RightCommand(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        self.run(LeftCommand(arg))

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        self.run(HomeCommand(arg))

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self.run(CircleCommand(arg))

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        self.run(PositionCommand(arg))

    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        self.run(HeadingCommand(arg))

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        self.run(ResetCommand(arg))

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    def do_record(self, arg):
        self._macro = []
        self._recording = True

    def do_stop(self, arg):
        self._recording = False

    def do_playback(self, arg):
        for command in self._macro:
            command.run()

    def run(self, command: TurtleCommand):
        if self._recording:
            self._macro.append(command)
        command.run()


if __name__ == '__main__':
    TurtleRecorder().cmdloop()
