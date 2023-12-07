from pathlib import Path
import logging
import time
import string

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

MAX_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()
    total = 0

    for line in data:
        cube_colors = ["red", "green", "blue"]
        table = str.maketrans(dict.fromkeys(string.punctuation))
        no_punc_line = line.translate(table)
        game_num = int(no_punc_line.split()[1])
        too_many = False

        for word in no_punc_line.split():
            if word.isdigit():
                num = int(word)
            elif word in cube_colors:
                if num > MAX_COLORS[word]:
                    too_many = True

        if not too_many:
            total += game_num

    print(f"total: {total}")

    logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
