from datetime import datetime
from functools import wraps
from typing import Callable, Protocol

from fastaoc.read_puzzle_input import read_puzzle_input


class SolveAocPuzzle(Protocol):
    def __call__(self, /, input: str) -> tuple[int, int]: ...


def solves_puzzle(
    day: int, year: int = 2024
) -> Callable[[SolveAocPuzzle], Callable[[], tuple[int, int]]]:
    def decorator(function: SolveAocPuzzle) -> Callable[[], tuple[int, int]]:
        @wraps(function)
        def wrapper() -> tuple[int, int]:
            input: str = read_puzzle_input(day=day, year=year)
            start: datetime = datetime.now()
            answer1, answer2 = function(input)
            print(answer1)
            print(answer2)
            print(f"{(datetime.now() - start).total_seconds():.6f}s")
            return answer1, answer2

        return wrapper

    return decorator
