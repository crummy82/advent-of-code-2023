import logging
import time
from pathlib import Path

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    galaxies = []
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "#":
                galaxies.append([x, y])
    print(f"coords before: {galaxies}")

    galaxy_xs = [x[0] for x in galaxies]
    galaxy_ys = [y[1] for y in galaxies]
    empty_rows = {row for row in range(len(data))}.difference(galaxy_xs)
    empty_cols = {col for col in range(len(data[0]))}.difference(galaxy_ys)
    print(f'empty rows: {empty_rows}')
    print(f'empty cols: {empty_cols}')
    total = 0
    add_size = 999999
    added_rows = 0
    added_cols = 0

    for x in range(len(galaxies)):
        for y in range(x + 1, len(galaxies)):
            for empty_row in empty_rows:
                if galaxies[x][0] < empty_row < galaxies[y][0] or galaxies[y][0] < empty_row < galaxies[x][0]:
                    added_rows += add_size
            for empty_col in empty_cols:
                if galaxies[x][1] < empty_col < galaxies[y][1] or galaxies[y][1] < empty_col < galaxies[x][1]:
                    added_cols += add_size
            x_diff = abs(galaxies[x][0] - galaxies[y][0]) + added_rows
            y_diff = abs(galaxies[x][1] - galaxies[y][1]) + added_cols
            total += (x_diff + y_diff)
            added_rows = 0
            added_cols = 0

    print("total: ", total)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
