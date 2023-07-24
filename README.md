# ALX SE

![HBNB Logo](https://github.com/Adeniyii/AirBnB_clone/blob/ac567ac0aea8e6bccafc650f0389131d5ee06202/assets/hbnb_logo.png)


<h1 align="center">AirBnB Clone Project (V1) - The Console<h1>

#### Description
> Welcome to the Console section of our remarkable AirBnB clone project! Within this repository, we proudly present a powerful and
> versatile command interpreter, accompanied by a diverse range of essential classes. These classes are meticulously designed to ensure the
> smooth functioning of our application, including the fundamental BaseModel class, and various others such as Amenity, City, State, Place,
> and Review, each inheriting from the aforementioned BaseModel.
>
> At the heart of our console lies a sophisticated command interpreter that exhibits striking similarities to a shell interface. Through
> this ingeniously crafted interpreter, users are granted the power to activate, interact with, and harness the true potential of our
> object instances. The console eagerly awaits user input, opening the gateway to a world of possibilities, where actions such as
> manipulation of object instances, method execution, and attribute handling are just a few of the seamless tasks that can be performed.
>
> With an intuitive and user-friendly interface, our command interpreter empowers developers and users alike, facilitating smooth
> navigation and interaction with the rich set of classes and functionalities we have thoughtfully curated for this AirBnB clone project.
> Unlock the full potential of your application effortlessly, as the console becomes your loyal companion, responding promptly to your
> commands and illuminating the path to efficient object management.
>
> Delve into the realm of object-oriented programming with confidence, as our console supports a myriad of commands that allow you to
> effortlessly create, modify, and interact with instances of various classes. Explore the depths of each class's capabilities and gain
> unparalleled control over your data, as the console seamlessly guides you through each step, like a knowledgeable mentor eager to assist
> you in achieving your goals.
>
> As you embark on this journey with our AirBnB clone project's console, rest assured that you are equipped with a robust and versatile
> toolset that simplifies complex tasks and empowers you to concentrate on building extraordinary features and functionalities for your
> application. Embrace the boundless potential that our console has to offer, as you delve into the realm of programming excellence and
> innovation. So why wait? Unleash your creativity, elevate your coding prowess, and embark on an exciting adventure with our Console for
> the AirBnB clone project!

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

