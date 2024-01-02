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

    lines = []
    for line in data:
        lines.append(line.split())

    total = 0

    for line in lines:
        diff_list = []
        diff_row = []
        for x in range(len(line) - 1):
            diff_row.append(int(line[x + 1]) - int(line[x]))
        diff_list.append(diff_row)
        row = 0
        while sum(diff_row) != 0:
            diff_row = []
            for x in range(len(diff_list[row]) - 1):
                diff_row.append(int(diff_list[row][x + 1]) - int(diff_list[row][x]))
            diff_list.append(diff_row)
            row += 1

        new_num = 0

        for n in reversed(range(len(diff_list) - 1)):
            if not new_num:
                new_num = (diff_list[n][-1] + diff_list[n - 1][-1])
            else:
                new_num += diff_list[n - 1][-1]

        new_last_num = int(line[-1]) + new_num

        total += new_last_num
    print(f"total: {total}")

    # logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
