#!/usr/bin/python3
"""this is the console class which contorls all the project"""
import cmd
import os
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """this is the console class"""

    prompt = "(hbnb) "
    class_names_list = ["BaseModel", "User"]
    class_attr = ["id", "created_at", "updated_at"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_var = args_list[0]
        if class_var not in self.class_names_list:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """show the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.class_names_list:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        storage.reload()
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        else:
            print(all_objs[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_name = args_list[0]

        if class_name not in self.class_names_list:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        storage.reload()
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of
        all instances based or not on the class name."""
        storage.reload()

        if not args:
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
        else:
            args_list = args.split()
            class_name = args_list[0]

            if class_name not in self.class_names_list:
                print("** class doesn't exist **")
                return

            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)

    def do_update(self, args):
        """
        Updates an instance based on the classname
        and id by adding or updating attribute
        """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.class_names_list:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        storage.reload()
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        attr_name = args_list[2]
        if attr_name in self.class_attr:
            return

        attr_value = json.loads(args_list[3])

        if isinstance(attr_value, str) and attr_value.isdigit():
            attr_value = int(attr_value)

        setattr(all_objs[key], attr_name, attr_value)
        storage.save()

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

    def do_clear(self, args):
        """Clears the console screen."""
        os.system("clear")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
