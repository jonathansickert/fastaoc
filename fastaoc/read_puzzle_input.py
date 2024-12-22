import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()


def get_puzzle_input_path(day: int) -> Path:
    return Path(__file__).parent / ("day" + str(day).rjust(2, "0") + ".txt")


def read_puzzle_input(day: int, year: int) -> str:
    path: Path = get_puzzle_input_path(day=day)
    if path.exists():
        with open(path, "r") as file:
            input: str = file.read()
        return input

    cookie: str | None = os.environ.get("SESSION_COOKIE")
    if cookie is not None:
        response: requests.Response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": cookie},
        )
        input: str = response.text
        with open(path, "w") as file:
            file.write(input)
        return input
    raise ValueError()  # TODO: come up with a good message
