#!/usr/bin/python3
"""This is the custom command line interpreter for the
airbnb clone project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The CLI class definition"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """This method defines how the program exits when
        the EOF is passed
        Args:
            line : Arguments passed into the command
        Return:
            None
        """
        return True

    def do_quit(self, line):
        """This method defines how the program exits when
        the EOF is passed
        Args:
            line : Arguments passed into the command
        Return:
            None
        """
        return True

    def emptyline(self):
        """Takes care of an empty line"""
        pass

    def class_exists(self, cls_name):
        """Checks if a class exists"""
        return cls_name in globals() and isinstance(globals()[cls_name], type)

    def do_create(self, line):
        """Creates new instance of BaseModel, saves it to JSON
        prints id"""
        arguments = line.split()
        if not arguments:
            print('** class name missing **')
        elif arguments[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints string representation of instance
        based on class name and id"""
        arguments = line.split()
        if not arguments:
            print('** class name missing **')
        elif not self.class_exists(arguments[0]):
            print('** class doesn\'t exist **')
        elif len(arguments) < 2:
            print('** instance id missing **')
        else:
            storage.reload()
            obj_dict = storage.all()
            local_key = "{}.{}".format(arguments[0], arguments[1])
            if local_key in obj_dict:
                print(obj_dict[local_key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arguments = line.split()
        if not arguments:
            print('** class name missing **')
        elif not self.class_exists(arguments[0]):
            print('** class doesn\'t exist **')
        elif len(arguments) < 2:
            print('** instance id missing **')
        else:
            storage.reload()
            obj_dict = storage.all()
            local_key = "{}.{}".format(arguments[0], arguments[1])
            if local_key in obj_dict:
                del obj_dict[local_key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances"""
        arguments = line.split()
        if not arguments or arguments[0] == 'BaseModel':
            storage.reload()
            instances = storage.all().values()
            local_list = [str(instance) for instance in instances]
            print(local_list)
        elif not self.class_exists(arguments[0]):
            print('** class doesn\'t exist **')

    def do_update(self, line):
        """Updates instance based on the class name and id
        by adding or updating attribute"""
        from ast import literal_eval
        arguments = line.split()
        if not arguments:
            print('** class name missing **')
            return
        cls_name = arguments[0]
        if cls_name != 'BaseModel':
            print('** class doesn\'t exist **')
            return
        if len(arguments) < 2:
            print('** instance id missing **')
            return
        storage.reload()
        obj_dict = storage.all()
        instance_id = arguments[1]
        local_key = "{}.{}".format(cls_name, instance_id)
        if local_key not in obj_dict:
            print('** no instance found **')
            return
        if len(arguments) < 3:
            print('** attribute name missing **')
            return
        if len(arguments) < 4:
            print('** value missing **')
            return
        instance = obj_dict[local_key]
        attr_name = arguments[2]
        attr_value = arguments[3]
        try:
            attr_value = literal_eval(attr_value)
        except (ValueError, SyntaxError):
            print('not acceptable attribute value format')
            return
        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
