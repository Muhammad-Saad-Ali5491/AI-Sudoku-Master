# test_solver.py

import pytest
from solver import (
    parse_sudoku, board_to_string,
    solve, solve_timed, count_solutions
)

# === Fixtures ===

@pytest.fixture
def sample_puzzle_and_solution():
    puzzle_str = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    solution_str = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
    board = parse_sudoku(puzzle_str)
    expected_board = parse_sudoku(solution_str)
    return board, expected_board, solution_str

@pytest.fixture
def unsolvable_puzzle():
    # Same number repeated in the same row, invalid puzzle
    puzzle_str = "111111111" + "0" * 72
    board = parse_sudoku(puzzle_str)
    return board

# === Tests ===

def test_parse_and_board_conversion(sample_puzzle_and_solution):
    _, expected_board, solution_str = sample_puzzle_and_solution
    # Ensure board_to_string can reverse parse_sudoku
    assert board_to_string(expected_board) == solution_str

def test_sudoku_solver_solves_correctly(sample_puzzle_and_solution):
    board, expected_board, _ = sample_puzzle_and_solution
    solved = solve(board)
    assert solved is True
    assert board == expected_board

def test_unsolvable_puzzle_returns_false(unsolvable_puzzle):
    solved = solve(unsolvable_puzzle)
    assert solved is False

def test_count_solutions_unique(sample_puzzle_and_solution):
    board, _, _ = sample_puzzle_and_solution
    solution_count = count_solutions(board)
    assert solution_count == 1

def test_solve_timed_works_and_returns_time(sample_puzzle_and_solution):
    board, expected_board, _ = sample_puzzle_and_solution
    duration = solve_timed(board)
    assert isinstance(duration, float)
    assert board == expected_board
