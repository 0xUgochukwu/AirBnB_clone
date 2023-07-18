# ALX SE

## AirBnB Clone Project (V1)


#### Description
> Console part of the AirBnB clone project.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: Amenity, City, State, Place,
> Review), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances methods and attributes.

#### How to Use Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `<class>.update('<id>', {'name' : 'Julien'})`  | updates attribute of an object             |
| `destroy` | `<class>.destroy('<id>')`                         | destroys specified object                  |
| `show`    | `<class>.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `<class>.all()`                                  | display all objects in class               |
| `count`   | `<class>.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |

#### Installation
```bash
git clone https://github.com/0xUgochukwu/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```bash
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
Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Environment
* Language: Python v3.8.5
* OS: Ubuntu 20.04 LTS

### Authors
- Ugochukwu Chukwuma
- Oluoha Stephanie

