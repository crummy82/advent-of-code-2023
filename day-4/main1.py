from pathlib import Path
import logging
import time
import re

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()

    total = 0
    cards = {}

    for line in data:
        score = 0
        matches = 0
        winning_nums = []
        card_num = re.search(r'\d+(?=:)', line)
        parts = line.split()

        for part_num in range(2, 12):
            winning_nums.append(int(parts[part_num]))

        for part_num in range(13, 38):
            if int(parts[part_num]) in winning_nums:
                matches += 1

        if matches:
            score = 1
            for x in range(matches - 1):
                score *= 2

        cards[card_num] = score

    for k in cards:
        total += cards[k]

    print("total:", total)

    #logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)

