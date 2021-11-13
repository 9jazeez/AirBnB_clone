#!/usr/bin/python3

"""
This is the module for interactive console

"""

import cmd
import sys
import string
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """The base case that inherits from the cmd lib"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = "HBNB Clone for Alx"
        self.prompt = '(hbnb) '
    
    def do_create(self, arg):
        """To create a new model use create <nameofmodel>"""
        if arg:
            if arg == "BaseModel":
                arg = BaseModel()
                arg.name = "Model@"+ arg.created_at.strftime("%M")
                arg.number = arg.id[0:5]
                arg.save()
                print(arg.id)
            elif arg not in ["BaseModel", "user"]:
                print("** Class doesn't exists **")
        else:
            print("** Class name missing **")

    def do_show(self, arg):
        """This prints the string representation of an instance
        based on the class name and id

        """
        if arg:
            if len(arg.split()) > 1:

                arg1 = arg.split()[0]
                arg2 = arg.split()[1]
                argc = arg1 + "." + arg2   
                if arg1 not in ["BaseModel", "user"]:
                    print("** Class doesn't exit **")
                elif arg2:
                    ids = storage.all()
                    if argc in ids.keys():
                        print(ids[argc])
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** Class name missing **")

    def do_destroy(self, arg):
        """This command deletes the class instance

        Usage: destroy <class name> <class id> 

        """
        if arg:
            if len(arg.split()) > 1:

                arg1 = arg.split()[0]
                arg2 = arg.split()[1]
                argc = arg1 + "." + arg2  
                if arg1 not in ["BaseModel", "user"]:
                    print("** Class doesn't exit **")
                elif arg2:
                    ids = storage.all()
                    if argc in ids.keys():
                        del(ids[argc])
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** Class name missing **")

    def do_all(self, arg):
        """This prints all string representation of the all instances
        based on or not the class name
        """
        if arg:
            if arg not in ["BaseModel", "user"]:
                print("** class doesn't exit **")
            else:
                obj = storage.all()
                for val in obj.values():
                    print(val)
        else:
            obj = storage.all()
            for val in obj.values():
                print(val)

    def do_update(self, arg):
        """This Updates an instance based on the class name,
        and id by adding or updating attritubes then saves the
        changes.

        Usage: update <class name> <class id> <attr> <attr value>
        """
        if arg:
            ar = arg.split()
            length = len(ar)
            if length >= 4:
                clName = ar[0]
                if clName not in ["BaseModel", "user"]:
                    print("** class doesn't exit **")
                else:
                    id = ar[1]
                    attr = ar[2]
                    attr_value = ar[3]
                    class_tag = clName + "." + id
                    obj = storage.all()
                    if class_tag in obj.keys():
                        model_instance = obj[class_tag]
                        setattr(model_instance, attr, attr_value)
                        model_instance.save()
                    else:
                        print("** no instance found **")
            elif length == 3:
                print("** value missing **")
            elif length == 2:
                print("** attribute name missing **")
            elif length == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to end the program\n"""
        quit()
        return True
    
    def close(self):
        self.close()
        return True

    def do_EOF(self, arg):
        """This uses EOF to stop the program\n"""
        sys.exit(1)

    def default(self, arg):
        """Let shell to use flags and short hand\n"""
        if arg == 'q' or arg == 'x':
            self.do_quit(arg)
        else:
            cmd.Cmd.default(self, arg)

    def emptyline(self):
        """ Empty line should pass\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
