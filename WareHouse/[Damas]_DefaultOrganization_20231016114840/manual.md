# User Manual - Juego de las Damas

## Introduction

Welcome to the user manual for the Juego de las Damas web application. This application allows you to play the game of checkers online. In this manual, you will find instructions on how to install the necessary dependencies, how to use the application, and an overview of its main functions.

## Installation

To install the Juego de las Damas web application, please follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download it from the official Python website (https://www.python.org/downloads/).

2. Clone the repository containing the game code to your local machine.

3. Open a terminal or command prompt and navigate to the directory where you cloned the repository.

4. Create a virtual environment by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you are ready to use the Juego de las Damas web application.

## Usage

To start the Juego de las Damas web application, follow these steps:

1. Make sure you have activated the virtual environment as described in the installation steps.

2. In the terminal or command prompt, navigate to the directory where you cloned the repository.

3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The application will start running, and you will see the game board displayed in the terminal.

5. Follow the on-screen instructions to play the game. Enter the starting position and ending position of your piece when prompted.

6. The game will continue until there is a winner or a draw. The winner will be displayed in the terminal.

7. To exit the application, press `Ctrl + C` in the terminal.

## Main Functions

The Juego de las Damas web application provides the following main functions:

- Displaying the game board: The application displays the current state of the game board in the terminal.

- Taking turns: The application prompts each player to enter their move, alternating between player 1 and player 2.

- Validating moves: The application checks if the entered move is valid and updates the game board accordingly.

- Determining the winner: The application determines the winner based on the number of remaining pieces on the board.

## Conclusion

Congratulations! You have successfully installed and used the Juego de las Damas web application. Enjoy playing the game of checkers online. If you have any further questions or need assistance, please don't hesitate to contact our support team.