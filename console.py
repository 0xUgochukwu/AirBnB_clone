#!/usr/bin/python3

"""HBNBCommand Class"""
import cmd
import shlex
import re
import json
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

        args = re.split(r" (?![^{}[\]()]*[}\]])", args)
        if args[0] == '':
            print("** class name missing **")
            return None

        if args[0] not in globals().keys():
            print("** class doesn't exist **")
            return None

        return args

    def __func(self, commmand, args):

        args = self.__class_validity(args)
        if args is None:
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

    def __parse(self, arg_str):
        parsed_arg = re.split(r"\(|, (?![^{}[\]()]*[}\]])", arg_str[:-1])
        return parsed_arg

    def __get_instances(self, objects, classname):
        objects_arr = []
        for key in objects.keys():
            class_type = key.split('.')[0]
            if class_type == classname:
                objects_arr.append(str(objects[key]))
        return objects_arr

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, args):
        'Creates a new Instance of a class'
        args = self.__class_validity(args)
        if args is None:
            return
        obj = globals()[args[0]]()
        print(obj.id)

    def do_show(self, args):
        'Prints the string repr of an instance based on the class name and id'
        self.__func("show", args)

    def do_destroy(self, args):
        'Deletes an instance based on the class name and id'
        self.__func("destroy", args)

    def do_count(self, args):
        'Retrieves the number of instances of a class'
        args = self.__class_validity(args)
        if args is None:
            return
        storage.reload()
        objects = storage.all()
        print(len(self.__get_instances(objects, args[0])))

    def do_all(self, args):
        """
        Prints all string repr of all instances based on the class name
        """
        args_count = len(shlex.split(args))

        storage.reload()
        objects = storage.all()
        objects_arr = []

        if args_count < 1:
            for value in objects.values():
                objects_arr.append(str(value))
        else:
            args = self.__class_validity(args)
            if args is None:
                return
            else:
                objects_arr = self.__get_instances(objects, args[0])

        print(objects_arr)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = self.__class_validity(args)
        if args is None:
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        objects = storage.all()
        key = args[0] + '.' + args[1]

        if key not in list(objects):
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif '}' in args[2]:
            for key, value in eval(args[2]).items():
                argument = f"{args[0]} {args[1]} {key} {value}"
                self.do_update(argument)
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
            objects[key].save()

    def precmd(self, args):
        if "." in args:
            args = args.split('.', 1)
            classname = args[0]
            arguments = self.__parse(args[1])
            function = arguments[0]
            line = f"{function} {classname} {(' ').join(arguments[1:])}"
            return cmd.Cmd.precmd(self, line)
        else:
            return cmd.Cmd.precmd(self, args)
        return

    def emptyline(self):
        'Does nothing'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
