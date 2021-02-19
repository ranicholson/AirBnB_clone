#!/usr/bin/python3

""" this is a single command interpreter for managing our objects """

import ast
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
                print("** class doesn't exist **")
            elif id not in store.keys():
                print("** no instance found **")
            else:
                print(str(store[id]))
        if len(tok) == 1:
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(tok) == 0:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        tok = arg.split()
        store = models.storage.all()

        if len(tok) == 2:
            id = tok[0] + "." + tok[1]
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            elif id not in store.keys():
                print("** no instance found **")
            else:
                del store[id]
                storage.save()
        if len(tok) == 1:
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(tok) == 0:
            print("** class name missing **")

    def do_all(self, arg):
        """ Prints all str rep of all instances based or not on the cls nm """
        store = []

        if len(arg) > 0:
            if arg not in self.classes_dict.keys():
                print("** class doesn't exist **")
            elif arg in self.classes_dict.keys():
                for key, value in storage.all().items():
                    if value.__class__.__name__ == arg:
                        store.append(str(value))
                print(str(store))
        else:
            for key, value in storage.all().items():
                store.append(str(value))
            print(str(store))

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
            if tok[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            elif self.id_check(id) is False:
                return
            else:
                print("** attribute name missing **")
        elif tok[0] not in self.classes_dict.keys():
            print("** class doesn't exist **")

        elif self.id_check(id) is False:
            return
        elif len(tok) == 3:
            print("** value missing **")
        else:
            this_obj = store[id]
            value = tok[3].replace("\"", "")
            setattr(this_obj, tok[2], value)
            this_obj.save()

    def default(self, line):
        """Override default error for specific commands"""

        com_list = line.split(".")
        classname = com_list[0]
        if len(com_list) > 1 and classname in self.classes_dict.keys():
            tmp = com_list[1].split("(")
            command = tmp[0]
            if command == "all" or command == "count":
                if command == "all":
                    self.do_all(classname)
                    return
                else:
                    self.count(classname)
                    return
            if command == "show" or command == "destroy":
                idl = tmp[1].split(")")
                idn = idl[0].replace("\"", "")
                glarg = classname + " " + idn
                if command == "show":
                    self.do_show(glarg)
                else:
                    self.do_destroy(glarg)
            elif command == "update":
                idl = tmp[1].split(",")
                idn = idl[0].replace("\"", "")
                glarg = classname + " " + idn
                tmp = com_list[1].split("(")
                updates = self.update_helper(classname, tmp[1])
                if type(updates) is str:
                    self.do_update(updates)
                else:
                    cid = glarg
                    for key, value in updates.items():
                        uarg = cid + " " + key + " " + str(value)
                        self.do_update(uarg)
                        uarg = ""
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

    @staticmethod
    def count(classname):
        """Method to count number of objects of specified class"""
        class_count = 0
        for key, value in storage.all().items():
            if value.__class__.__name__ == classname:
                class_count += 1
        print(class_count)

    @staticmethod
    def id_check(str):
        """ ID check """
        if str not in models.storage.all().keys():
            print("** no instance found **")
            return False
        else:
            return True

    @staticmethod
    def update_helper(classname, string):
        """ Method to break up values passed when overriding default"""
        flag = 0
        for element in string:
            if element == "{":
                flag = 1
                break
        upd_list = string.split(",")
        idl = upd_list[0]
        idn = idl.replace("\"", "")
        blarg = classname + " " + idn
        if flag == 0:
            if len(upd_list) < 2:
                attr = ""
            else:
                attr = upd_list[1].replace("\"", "").replace(" ", "")
            if len(upd_list) < 3:
                tmpvalue = []
                value = ""
            else:
                tmpvalue = upd_list[2].split(")")
                value = tmpvalue[0].replace("\"", "")
            blarg += " " + attr + " " + value
            return (blarg)
        else:
            strlist = string.split(",", 1)
            dstr = strlist[1].replace(")", "").replace(" ", "", 1)
            updatedict = ast.literal_eval(dstr)
            return (updatedict)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
