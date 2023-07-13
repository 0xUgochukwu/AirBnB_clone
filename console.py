#!/usr/bin/python3

"""HBNBCommand Class"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, arg):
        'Creates a new BaseModel Instance'
        if not arg:
            print("** class name missing **")
            return
        if arg not in globals() or arg != "BaseModel":
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        print(obj.id)

    def do_show(self, arg):
        'Displays string representation of a class based on its id'

        args = shlex.split(arg)
        print(globals().keys())

        if len(args) == 0:
            print("** class name missing **")
            return

        if arg[0] not in globals().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        objects = storage.all()
        key = args[0] + '.' + args[1]

        if key not in objects.keys():
            print("** no instance found **")
        else:
            print(objects[key])



    def emptyline(self):
        'Does nothing'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
