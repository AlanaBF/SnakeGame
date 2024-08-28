# Snake Game

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle%20Graphics-Python-green?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-1.0%2B-blue?logo=visual-studio-code&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to the Snake Game! This is a classic snake game built with Python and the Turtle graphics library. This README will guide you on how to run the game and provide a beginner's tutorial on important programming concepts demonstrated in the code.

## Table of Contents

- [Technology Used](#technology-used)
- [How to Run the Game](#how-to-run-the-game)
- [Demo](#demo)
- [Code Tutorial](#code-tutorial)
  - [List Slicing](#list-slicing)
  - [Class Inheritance](#class-inheritance)
  - [Object-Oriented Programming](#object-oriented-programming)
- [Contributing](#contributing)
- [License](#license)
- [Connect With Me](#connect-with-me)

## Technology Used

The following technologies and libraries were used to develop this project:

- Python: The main programming language used for the game's logic.
- Turtle Graphics: A standard Python library used for drawing graphics on the screen, which powers the visual elements of the game.
- VS Code: The integrated development environment (IDE) used to write and debug the code.

## How to Run the Game

To play the Snake Game, follow these steps:

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Download or clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>

3. Install any required dependencies. For this game, you need the turtle module, which comes pre-installed with Python, so no additional installation is needed.

4. Run the game by executing:

    ```bash
    python main.py
    ```

5. Use the arrow keys to control the snake. The objective is to eat the food and avoid collisions with the wall or the snake's tail.

## Demo

![Snake Game Demo](/snake-game.gif)

## Code Tutorial

This section introduces some fundamental programming concepts demonstrated in the code, explaining what they are, how they work, and how they are applied in this project.

### List Slicing

**What It Is:**
List slicing in Python is a technique to extract a portion of a list. This can be useful for operations that need to focus on a specific segment of the list, such as iterating over certain elements, copying parts of the list, or creating new lists.

**How It Works:**
The syntax for slicing is `list[start:end]`, where `start` is the index to begin the slice (inclusive), and `end` is the index to end the slice (exclusive). If `start` is omitted, it defaults to `0`, and if `end` is omitted, it defaults to the length of the list.

**Example in This Project:**
In the Snake game, list slicing is used to iterate over the segments of the snake, excluding the head. This is crucial when checking for collisions between the snake's head and its body, as the head should not be compared with itself.

```python
# Detect collision with tail
for segment in self.segments[1:]:
    if self.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
```

Here, self.segments[1:] slices the self.segments list to exclude the first element (the head of the snake) when checking for collisions with the tail. The code then iterates over each segment to check if the distance from the head is less than a certain threshold, indicating a collision.

### Class Inheritance

What It Is: Class inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reuse and the creation of more complex behaviors by building on existing functionalities.

How It Works: When a class inherits from another, it automatically gains all the properties and methods of the parent class. The child class can override these methods or add new ones, enhancing or altering the behavior inherited from the parent class.

Example in This Project: In this game, the Scoreboard and Food classes inherit from the Turtle class provided by the Turtle graphics library. By doing so, these classes can leverage Turtle's built-in methods to handle graphical elements on the screen while adding their own unique functionality.

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Additional initialization code
```

Here, the Scoreboard class uses ```super().__init__()``` to call the initializer of the Turtle class, allowing it to use Turtle’s graphical capabilities, such as drawing on the screen, while also adding specific behaviors like updating the score.

### Object-Oriented Programming

What It Is: Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which are instances of classes. OOP allows for organizing code into logical units that represent real-world entities, making it easier to manage and scale large codebases.

How It Works: OOP is built around four main principles:

1. Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data into a single unit or class.
2. Abstraction: Hiding the complex implementation details and exposing only the necessary parts of the object.
3. Inheritance: Creating a new class that reuses, extends, or modifies the behavior of an existing class.
4. Polymorphism: Allowing objects of different classes to be treated as objects of a common superclass.

Example in This Project: OOP principles are applied throughout the Snake Game to create well-organized and reusable code. Each component of the game, such as the snake, the food, and the scoreboard, is represented by a class with specific responsibilities.

- Encapsulation:

  - The Snake class encapsulates data (e.g., the list of segments) and behaviors (e.g., movement and collision detection).
  - The Food class manages the food’s appearance and location, while the Scoreboard class handles scoring.
- Methods in Action: The move method in the Snake class demonstrates encapsulation and method usage within OOP:

    ```python
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    ```

    This method updates the position of each segment to follow the segment in front of it, ensuring the snake moves smoothly across the screen. The method encapsulates the movement logic within the Snake class, making it easy to manage and modify without affecting other parts of the code.

By using OOP, the game code is more modular, easier to understand, and simpler to extend or modify. For example, adding new features like power-ups or a multiplayer mode would involve creating new classes or extending existing ones, without disrupting the core functionality.

## Contributing

Feel free to contribute to the project! To do so:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Connect with Me

- [![GitHub Badge](https://img.shields.io/badge/GitHub-AlanaBF-black?style=for-the-badge&logo=github)](https://github.com/AlanaBF)
- [![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alanabarrettfrew/)
- [![Medium Badge](https://img.shields.io/badge/Medium-%2312100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@alana.barrettfrew)
- [![Instagram Badge](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/teacherturnsturtle81/)
- [![Facebook Badge](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/teacherturnsturtle/)
