# Snake Game User Manual

## Introduction
Welcome to the Snake Game! This game is developed using Python and the Pygame library. The objective of the game is to control a snake and eat apples to increase its length. However, be careful not to hit the boundaries of the window or collide with yourself, as that will end the game. The game features an interactive interface and displays the current length of the snake and the number of apples eaten.

## Installation
To play the Snake Game, you need to install Python and the Pygame library. Follow the steps below to install the necessary dependencies:

1. Install Python: Visit the official Python website at https://www.python.org and download the latest version of Python for your operating system. Follow the installation instructions provided.

2. Install Pygame: Open a terminal or command prompt and run the following command to install Pygame using pip:

   ```
   pip install pygame
   ```

   If you prefer using conda, you can run the following command instead:

   ```
   conda install pygame -c conda-forge
   ```

## How to Play
Once you have installed the necessary dependencies, you can start playing the Snake Game. Follow the steps below to play the game:

1. Open a terminal or command prompt and navigate to the directory where you have saved the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. The game window will open, and you will see a snake and an apple. Use the arrow keys on your keyboard to control the snake's movement. The snake will move in the direction of the pressed arrow key.

4. The objective of the game is to eat as many apples as possible without hitting the boundaries of the window or colliding with yourself. Each time the snake eats an apple, its length will increase by one.

5. If the snake hits the boundaries of the window or collides with itself, the game will end, and a "Game Over" message will be displayed.

6. At the top of the window, you will see a visible counter that displays the number of apples eaten by the snake.

7. To start a new game, close the game window and run the `python main.py` command again.

## Customization
You can customize the game by modifying the code in the `main.py` file. Here are some possible customizations:

- Change the window dimensions: Modify the `window_width` and `window_height` variables to set the desired width and height of the game window.

- Change the snake's speed: Modify the `snake_speed` variable to adjust the speed at which the snake moves.

- Change the colors: Modify the `black`, `white`, `red`, and `green` variables to set different colors for the game elements.

- Change the font style: Modify the `font_style` variable to use a different font for displaying text.

Feel free to experiment with these customizations to create your own unique version of the Snake Game!

## Conclusion
Congratulations! You have successfully installed and played the Snake Game. Enjoy the game and have fun controlling the snake to eat as many apples as possible. If you have any questions or encounter any issues, please don't hesitate to reach out to our support team for assistance. Happy gaming!