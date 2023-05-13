# AirBnB clone - The console
![AirBnB logo](https://www.tabbykatz.com/hbnb.png)

The AirBnB clone project has the goal to deploy on my server a simple copy of the AirBnB website.
What Is Airbnb? Airbnb, as in “Air Bed and Breakfast,” is a service that lets property owners rent
out their spaces to travelers looking for a place to stay. Travelers can rent a space for multiple
people to share, a shared space with private rooms, or the entire property for themselves.
Airbnb is an online marketplace that connects people who want to rent out their homes with
people who are looking for accommodations in specific locales.

Not all the features are implemented, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, a complete web application composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## General Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Concepts learned

The concept of the project is not to build the application all at once, but step by step.
Each step will link to a concept:
* **Unittest**
* **Python packages**
* **Serialization/Deserialization**
* `*args and **kwargs`
* **datetime**
* **The console**
* **Web static**
* **Web framework - templating**
* **RESTful API**
* **Web dynamic**
* **Files and Directories**
* **Storage**

## The console

The first piece is to manipulate a powerful storage system. This storage engine will give us an
abstraction between “My object” and “How they are stored and persisted”.

A program called `console.py` contains the entry point of the command interpreter base on the `python` inbuilt module `cmd`.
The console implement:
* `quit` and `EOF` to `exit` the program
* `help` (this action is provided by default by `cmd` but can be updated and documented as you work through tasks)
* a custom prompt: `(hbnb)`

The console is a tool that validates the storage engine with the following processes:
* create data model
* manage (create, update, destroy, etc) objects
* store and persist objects to a file (JSON file)
This means: from console code (the command interpreter itself) and from the front-end and RestAPI, no attention will be paid (take care) of how objects are stored.

This abstraction allow you to change the type of storage easily without updating all of your codebase.

**Execution of console**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
###Usage

**Does nothing when command is emptyline**
```
(hbnb)
(hbnb)
(hbnb)
(hbnb)
(hbnb)
```

**To disply avialable commands type help**
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

**To know about a command type help and command name**
```
(hbnb) help destroy
Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.

(hbnb)
```
**To exit type quit**
```
(hbnb) quit
$
```
**Create an object**
```
(hbnb) create User
f9a71c9f-aed0-4f96-bff6-7e43278869bc
(hbnb) all User
```

**Check all objects of a class**
```
(hbnb) all User
["[User] (f9a71c9f-aed0-4f96-bff6-7e43278869bc) {'id': 'f9a71c9f-aed0-4f96-bff6-7e43278869bc', 'created_at': datetime.datetime(2023, 5, 11, 11, 14, 21, 103611), 'updated_at': datetime.datetime(2023, 5, 11, 11, 14, 21, 103618)}"]
(hbnb)
```

**Count objects**
```
(hbnb) count User
1
(hbnb)
```
**To delete an object**
```
(hbnb) create User
6359491d-76a5-4697-a7c9-3b342536145f
(hbnb) count User
2
(hbnb) User.destroy(f9a71c9f-aed0-4f96-bff6-7e43278869bc)
(hbnb) count User
1
(hbnb)
```
**You can also update an object**
```
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
```
**To use the comand _update_, _show_ and _destroy_, _id_ of object is needed**
```
(hbnb) User.destroy()
** instance id missing **
(hbnb) User.update()
** instance id missing **
(hbnb) User.show()
** instance id missing **
(hbnb)
```
