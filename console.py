#!/usr/bin/python3

""" this is a single command interpreter for managing our objects """

import models
from models import storage
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ defines a single command interpreter to manage our objects """
    prompt = '(hbnb)'
    classes_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review}

    def emptyline(self):
        """ does not execute last command """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if len(arg) < 1:
            print("** class name missing **")
            return
        for keys in self.classes_dict.keys():
            if arg == keys:
                new_instance = self.classes_dict[keys]
                new = new_instance()
                new.save()
                print(new.id)
                return
        print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        """ based on the class name and id """
        tok = arg.split()
        store = models.storage.all()

        if len(tok) == 2:
            id = tok[0] + "." + tok[1]
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exit **")
            elif id not in store.keys():
                print("** no instance found **")
            else:
                print(store[id])
        if len(tok) == 1:
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(tok) == 0:
            print("** class name is missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        tok = arg.split()
        store = models.storage.all()

        if len(tok) == 2:
            id = tok[0] + "." + tok[1]
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exit **")
            elif id not in store.keys():
                print("** no instance found **")
            else:
                del store[id]
        if len(tok) == 1:
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(tok) == 0:
            print("** class name is missing **")

    def do_all(self, arg):
        """ Prints all str rep of all instances based or not on the cls nm """
        store = []

        if len(arg) > 0:
            if arg not in self.classes_dict.keys():
                print("** class doesn't exit **")
            elif arg in self.classes_dict.keys():
                for key, value in storage.all().items():
                    if value.__class__.__name__ == arg:
                        store.append(str(value))
                print(store)
        else:
            for key, value in storage.all().items():
                store.append(str(value))
            print(store)

    def do_update(self, arg):
        """ Updates an intance based on class name and id
        by adding or updating attr """
        tok = arg.split()
        store = models.storage.all()

        if len(tok) >= 2:
            id = tok[0] + "." + tok[1]

        if len(tok) == 0:
            print("** class name missing **")

        elif len(tok) == 1:
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

        elif len(tok) == 2:
            print(id)
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exit **")
            elif self.id_check(id) is False:
                return
            else:
                print("** attribute name missing **")

        elif self.id_check(id) is False:
            return
        elif len(tok) == 3:
            print("** value missing **")
        else:
            this_obj = store[id]
            setattr(this_obj, tok[2], tok[3])
            this_obj.save()

    @staticmethod
    def id_check(str):
        """ ID check """
        if str not in models.storage.all().keys():
            print("** no instance found **")
            return False
        else:
            return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
