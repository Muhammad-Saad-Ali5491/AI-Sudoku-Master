# Sudoku Master: A Comprehensive Sudoku Game and Generator

Sudoku Master is a Python-based project that provides a fully functional Sudoku game with a graphical user interface (GUI) built using Pygame, along with tools for generating, solving, and validating Sudoku puzzles. The project includes a puzzle generator, a solver with performance metrics, a dataset processing script, and a test suite for ensuring reliability. This README provides a detailed overview of the project, its structure, functionality, and setup instructions.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Downloading the Dataset](#downloading-the-dataset)
- [Usage](#usage)
  - [Running the Sudoku Game](#running-the-sudoku-game)
  - [Generating Puzzles](#generating-puzzles)
  - [Processing the Dataset](#processing-the-dataset)
  - [Validating the Solver](#validating-the-solver)
  - [Running Tests](#running-tests)
- [How It Works](#how-it-works)
  - [Sudoku Solver](#sudoku-solver)
  - [Puzzle Generator](#puzzle-generator)
  - [Game Interface](#game-interface)
  - [Dataset Processing](#dataset-processing)
  - [Validation and Testing](#validation-and-testing)
- [Difficulty Measurement](#difficulty-measurement)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Sudoku Master is designed to provide an engaging Sudoku experience while also serving as a robust tool for generating and validating puzzles. The project leverages Python's Pygame library for the GUI, a backtracking algorithm with Minimum Remaining Values (MRV) heuristic for solving puzzles, and the Kaggle API for dataset integration. It is suitable for both casual players and developers interested in Sudoku algorithms or game development.

## Features
- **Interactive Sudoku Game**: A Pygame-based GUI with features like pause/resume, timer reset, puzzle generation, and solver activation.
- **Puzzle Generator**: Generates valid Sudoku puzzles with unique solutions, adjustable difficulty, and saves them to files.
- **Sudoku Solver**: Uses a backtracking algorithm with MRV heuristic to solve puzzles efficiently, with timing and solution counting capabilities.
- **Dataset Processing**: Converts a Kaggle Sudoku dataset into a format suitable for validation and testing.
- **Validation**: Evaluates the solver's accuracy against a dataset of known puzzles and solutions.
- **Testing Suite**: Includes unit tests to verify solver functionality and puzzle parsing.
- **Difficulty Assessment**: Measures puzzle difficulty based on solving time (Easy, Medium, Hard).

## File Structure
The project consists of the following key files:

- **`datasetinstall.py`**: Downloads the Sudoku dataset from Kaggle using the `kagglehub` library.
- **`generator.py`**: Generates valid Sudoku puzzles with unique solutions and saves them to text files.
- **`datafixing.py`**: Processes the Kaggle Sudoku dataset (`sudoku.csv`) into separate puzzle and solution text files.
- **`sudoku_game.py`**: Implements the Pygame-based Sudoku game with a GUI for playing and solving puzzles.
- **`solver.py`**: Contains the core Sudoku solving logic, including parsing, validation, and solution counting.
- **`validator.py`**: Evaluates the solver's accuracy using the processed dataset.
- **`test_solver.py`**: Contains Pytest unit tests for the solver and related functions.
- **`requirements.txt`**: Lists all Python dependencies required for the project.

Generated files:
- **`generated_puzzles.txt`**: Stores generated puzzles.
- **`generated_solutions.txt`**: Stores solutions for generated puzzles.
- **`sudoku_puzzles.txt`**: Stores puzzles extracted from the dataset.
- **`sudoku_solutions.txt`**: Stores solutions extracted from the dataset.

## Dependencies
The project relies on the following Python libraries (listed in `requirements.txt`):
- `pygame==2.6.1`: For the GUI.
- `kagglehub==0.3.12`: For downloading the Kaggle dataset.
- `tqdm==4.67.1`: For progress bars during validation.
- `pytest==8.4.1`: For running unit tests.
- Other dependencies (e.g., `requests`, `python-dateutil`) are used for dataset handling and utilities.

## Installation

### Setting Up the Environment
1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/Muhammad-Saad-Ali5491/AI-Sudoku-Master.git
   cd sudoku-master
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Downloading the Dataset
The project uses a Sudoku dataset from Kaggle for validation. To download it:
1. Ensure you have a Kaggle account and API key set up (`~/.kaggle/kaggle.json`).
2. Run the dataset download script:
   ```bash
   python datasetinstall.py
   ```
   This downloads the dataset to a local path, which is printed to the console.
3. Move the downloaded `sudoku.csv` to the project directory if necessary.

## Usage

### Running the Sudoku Game
To play the Sudoku game:
```bash
python sudoku_game.py
```
- **Controls**:
  - Click a cell to select it.
  - Type numbers (0-9) to fill cells (0 clears the cell).
  - **Buttons**:
    - **Pause**: Pauses the timer.
    - **Resume**: Resumes the timer.
    - **Timer R**: Resets the timer.
    - **All Solve**: Solves the entire puzzle with a fade-in animation.
    - **Generate**: Generates a new puzzle.
  - The interface displays the current time, difficulty, and hints (e.g., invalid cell warnings).

### Generating Puzzles
To generate a new puzzle and its solution:
```bash
python generator.py
```
- Outputs the puzzle and solution to the console.
- Saves them to `generated_puzzles.txt` and `generated_solutions.txt`.
- Displays the puzzle's difficulty based on solving time.

### Processing the Dataset
To convert `sudoku.csv` into text files for puzzles and solutions:
```bash
python datafixing.py
```
- Reads `sudoku.csv` and creates `sudoku_puzzles.txt` and `sudoku_solutions.txt`.

### Validating the Solver
To evaluate the solver's accuracy using the dataset:
```bash
python validator.py
```
- Compares solver output against known solutions.
- Outputs accuracy, number of correct solutions, and total time taken.

### Running Tests
To run the unit tests:
```bash
pytest test_solver.py
```
- Tests include puzzle parsing, solver correctness, handling unsolvable puzzles, solution counting, and timed solving.

## How It Works

### Sudoku Solver (`solver.py`)
- **Parsing**: `parse_sudoku` converts an 81-character string into a 9x9 grid.
- **Validation**: `valid` checks if a number can be placed in a cell without violating Sudoku rules.
- **MRV Heuristic**: `find_mrv_cell` selects the cell with the fewest possible values to optimize backtracking.
- **Solving**: `solve` uses backtracking to fill the grid, leveraging the MRV heuristic.
- **Solution Counting**: `count_solutions` counts unique solutions (stops at 2 for efficiency).
- **Timed Solving**: `solve_timed` measures solving time for difficulty assessment.

### Puzzle Generator (`generator.py`)
- **Full Grid Generation**: Fills diagonal 3x3 boxes randomly, then solves the grid using `solve`.
- **Cell Removal**: Removes cells randomly while ensuring the puzzle retains a unique solution.
- **Difficulty Assessment**: Uses solving time to classify puzzles as Easy, Medium, or Hard.
- **Saving**: Saves puzzles and solutions to text files.

### Game Interface (`sudoku_game.py`)
- **Pygame GUI**: Displays a 9x9 grid with a neumorphic design, buttons, and status indicators.
- **Interactivity**: Allows cell selection, number input, and button actions.
- **Animations**: Fade-in effect for solved cells.
- **Difficulty Display**: Shows puzzle difficulty based on solving time.

### Dataset Processing (`datafixing.py`)
- Reads `sudoku.csv` (format: `quizzes,solutions`).
- Extracts valid 81-character puzzle and solution strings.
- Writes them to `sudoku_puzzles.txt` and `sudoku_solutions.txt`.

### Validation and Testing
- **Validator (`validator.py`)**: Tests the solver against the dataset, reporting accuracy and performance.
- **Tests (`test_solver.py`)**: Verifies solver functionality with a sample puzzle, an unsolvable puzzle, and edge cases.

## Difficulty Measurement
Puzzle difficulty is determined by the solving time in `measure_difficulty_time`:
- **Easy**: ≤ 0.0005 seconds
- **Medium**: ≤ 0.0012 seconds
- **Hard**: > 0.0012 seconds
This is based on empirical observations of solving times (0.00028–0.00171 seconds).

## Future Improvements
- Add difficulty selection for puzzle generation.
- Implement additional solving algorithms (e.g., constraint propagation).
- Enhance the GUI with sound effects and customizable themes.
- Support loading puzzles from `sudoku_puzzles.txt` in the game.
- Optimize solver performance for very hard puzzles.
- Add a hint system that suggests valid moves.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Please ensure code follows PEP 8 style guidelines and includes tests for new functionality.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (if applicable).
