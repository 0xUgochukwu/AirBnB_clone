#!/usr/bin/python3

"""HBNBCommand Class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        'Does nothing'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
