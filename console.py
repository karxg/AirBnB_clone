#!/usr/bin/python3
"""this is the console class which contorls all the project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """this is the console class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """exit the app"""
        print()
        exit()

    def do_help(self, arg: str):
        """help you in understanding what every thing do"""
        return super().do_help(arg)

    def emptyline(self) -> bool:
        """a func to pass the func before it"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
