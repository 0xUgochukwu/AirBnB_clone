# ALX SE

## AirBnB Clone Project (V1) - The Console

![HBNB Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230718%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230718T094125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9701853aa596e709f1bba7ee09b9b43f915a915d12b53fe7f43bc95dca2db2)

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

