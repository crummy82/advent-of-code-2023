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

    # count rows with only "." and append to a new list
    empty_rows = []
    for x, line in enumerate(data):
        if line.count(".") == len(line):
            empty_rows.append(x)

    # Insert new rows to double up the "." only rows
    for i in range(len(empty_rows)):
        data.insert(empty_rows[i] + i, "." * len(data[0]))

    # Count columns with only "." and append to a new list
    empty_cols = []
    for y, char in enumerate(data[0]):
        if char == ".":
            blank_col = True
            for line in data:
                if line[y] != ".":
                    blank_col = False
            if blank_col:
                empty_cols.append(y)

    # Insert new columns to double up the "." only columns
    for j in range(len(empty_cols)):
        for z in range(len(data)):
            line_list = list(data[z])
            line_list.insert(empty_cols[j] + j, ".")
            data[z] = "".join(line_list)

    # Find all galaxies and add to a new list of tuples with their coords
    galaxies = []
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))

    total = 0

    # Find the distance between galaxies and sum them
    for x in range(len(galaxies)):
        for y in range(x + 1, len(galaxies)):
            x_diff = abs(galaxies[x][0] - galaxies[y][0])
            y_diff = abs(galaxies[x][1] - galaxies[y][1])
            total += x_diff + y_diff

    print("total: ", total)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
