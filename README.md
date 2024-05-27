# Project Name

One or two paragraphs providing an overview of your project. This should include what your project does and the problem it solves.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Introduction

The ECS Ping Pong game provides an engaging simulation of a classic arcade game, utilizing Pygame for graphical rendering and ECS for an organized, maintainable codebase. This project demonstrates how ECS can be applied to game development, ensuring a clear separation of concerns and easy scalability.

## Installation

Steps to install your project locally:

```bash
git clone https://github.com/Johannes0508/ESC_PINGPONG_GAME
cd ESC_PINGPONG_GAME

pip install -r requirements.txt
```

## Usage

To start the game, simply run the main script:

bash:

python main.py

Here's an example of how to initialize the game within a Python script:


import pygame
from components import PositionComponent, RadiusComponent, RectComponent, SpeedComponent, WinnerComponent
from systems import MotionSystem, RenderingSystem
from entities import Entity

# Initialize pygame and set up the game window
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('ECS Ping Pong Game')

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update game state and render
    pygame.display.update()

pygame.quit()


## Features

 - Modular ECS Architecture: Components and systems are decoupled for flexibility and maintainability.
 - Realistic Game Physics: Simulates the motion of a ping pong ball and paddle interactions.
 - AI Opponent: An AI-controlled paddle that competes against the player.
 - Score Tracking: Keeps track of player and CPU scores, displaying them on the screen.
 - Responsive Controls: Smooth paddle control for an enjoyable gameplay experience.

 ## File Structure

 # Main Components Overview
 - components.py: Manages various components of game entities.

 - Purpose: Defines essential components like position, radius, rectangle, speed, and winner state for game entities.

 - systems.py: Manages the motion and rendering systems.

 - Function: Contains systems responsible for handling movement and rendering of game entities.

 - entities.py: Manages the entity framework.

 - Purpose: Defines the structure and behavior of game entities.

 # Modules Folder Structure
 - position_component.py: Introduces PositionComponent.

 - Function: Represents the position of an object with x and y coordinates.

 - radius_component.py: Incorporates RadiusComponent.

 - Role: Represents a circular shape with a specified radius.

 - rect_component.py: Introduces RectComponent.

 - Function: Represents a rectangle with specific dimensions.

 - speed_component.py: Incorporates SpeedComponent.

 - Role: Represents the speed of an object in both x and y directions.

 - winner_component.py: Introduces WinnerComponent.

 - Function: Keeps track of the winner state in the game.

 # Utilities Folder Contents
 - motion_system.py: Showcases MotionSystem.

 - Operation: Handles the movement of players, AI, and ball in the game.

 - rendering_system.py: Contains RenderingSystem.

 - Mechanism: Responsible for drawing game entities like paddles and ball on the screen.

## Contributing

State if you are open to contributions and what your requirements are for accepting them.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the [Unlicense](LICENSE) License. See `LICENSE` for more information.

## Contact

Johannes - [@Johannes0508](https://github.com/Johannes0508)

Ajob - [@Ajob1](https://github.com/Ajob1)

Project Link: [https://github.com/Johannes0508/ESC_PINGPONG_GAME](https://github.com/Johannes0508/ESC_PINGPONG_GAME)

## Acknowledgments

We would like to express our gratitude to the following individuals and projects that have contributed to the development of our Ping Pong Game:

- **Hat tip to anyone whose code was used**:
  - [Pygame](https://www.pygame.org/): A set of Python modules designed for writing video games, which provided the foundation for our game's development.
  - [Tutorials and Open Source Projects](https://github.com/pygame/pygame): Various open-source projects and tutorials that offered guidance and inspiration for implementing game mechanics and features.

- **Inspiration**:
  - Classic arcade ping pong games that sparked the idea for this project and provided a model for gameplay and mechanics.
  - Community feedback and suggestions that helped shape the game into a more enjoyable and polished experience.

- **Special Thanks**:
  - To all contributors who have submitted code, reported bugs, and shared ideas to improve the game.
  - To our beta testers for their invaluable feedback and support during the development process.

Your contributions and support have been instrumental in bringing this project to life. Thank you!