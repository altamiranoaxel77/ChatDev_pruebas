# Chess Game User Manual

## Introduction
Welcome to the Chess Game user manual! This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use and play the game.

## Installation
To install the Chess Game, please follow the steps below:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website (https://www.python.org/downloads/).

2. Clone or download the Chess Game repository from GitHub (https://github.com/your-repository-link).

3. Open a terminal or command prompt and navigate to the directory where you downloaded the Chess Game.

4. Create a virtual environment (optional but recommended) by running the following command:
   ```
   python -m venv myenv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:
   - For Windows:
     ```
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source myenv/bin/activate
     ```

6. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you are ready to use the Chess Game!

## Main Functions
The Chess Game provides the following main functions:

1. Displaying the chessboard: The game starts by displaying an 8x8 chessboard on the screen.

2. Moving pieces: You can move the chess pieces by clicking on a piece and then clicking on the desired destination square. The game will validate the move and update the chessboard accordingly.

3. Validating moves: The game checks if a move is valid based on the rules of chess. It considers factors such as piece type, position, and the presence of other pieces on the board.

4. Capturing opponent pieces: When a piece moves to a square occupied by an opponent's piece, the opponent's piece is captured and removed from the board.

5. Game termination: The game can be terminated by either player by closing the application window.

## How to Play
To play the Chess Game, follow these steps:

1. Launch the game by running the `main.py` file using Python:
   ```
   python main.py
   ```

2. The game window will appear, displaying the initial chessboard configuration.

3. To move a piece, click on the piece you want to move and then click on the destination square. The game will validate the move and update the chessboard accordingly.

4. Continue moving pieces until the game is complete. You can terminate the game by closing the application window.

## Conclusion
Congratulations! You have successfully installed the Chess Game and learned how to use and play it. Enjoy playing chess and have fun! If you have any questions or encounter any issues, please refer to the documentation or contact our support team for assistance.