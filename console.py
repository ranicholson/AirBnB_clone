#!/usr/bin/python3

""" this is a single command interpreter for managing our objects """

import models
from models import storage
import cmd, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ defines a single command interpreter to manage our objects """
    prompt = '(hbnb)'
    classes_dict = {'BaseModel': BaseModel}

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

        if arg[0] not in self.classes_dict.keys():
            print("** class doesn't exit **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
