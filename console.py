#!/usr/bin/python3

"""HBNBCommand Class"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """A HBNBCommand class"""
    prompt = '(hbnb) '

    def __class_validity(self, args):

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in globals().keys():
            print("** class doesn't exist **")
            return False
        return args

    def __func(self, commmand, args):

        args = self.__class_validity(args)
        if args is False:
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        objects = storage.all()
        key = args[0] + '.' + args[1]

        if key not in objects.keys():
            print("** no instance found **")
        elif commmand == "destroy":
            del objects[key]
            storage.save()
        else:
            print(objects[key])

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, args):
        'Creates a new Instance of a class'
        args = self.__class_validity(args)
        if args is False:
            return
        obj = globals()[args[0]]()
        print(obj.id)

    def do_show(self, args):
        'Prints the string repr of an instance based on the class name and id'
        self.__func("show", args)

    def do_destroy(self, args):
        'Deletes an instance based on the class name and id'
        self.__func("destroy", args)

    def do_all(self, args):
        """
        Prints all string repr of all instances based or not on the class name
        """
        if self.__class_validity(args) is False:
            return
        objects = storage.all()
        objects_arr = []
        for value in objects.values():
            objects_arr.append(str(value))
        print(objects_arr)

    def do_update(self, args):
        'Updates an instance based on the class name and id'
        args = self.__class_validity(args)
        storage.reload()
        objects = storage.all()
        key = args[0] + '.' + args[1]

        if args is False:
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif key not in objects.keys():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            obj = vars(objects[key])
            attr = args[2]
            value = args[3]
            if attr in obj.keys():
                attr_type = type(obj[attr])
                value = attr_type(args[3])
            obj[attr] = value
            storage.save()

    def emptyline(self):
        'Does nothing'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
