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


def main():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()
    total = 0

    for line in data:
        cube_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
            }
        table = str.maketrans(dict.fromkeys(string.punctuation))
        no_punc_line = line.translate(table)

        for word in no_punc_line.split():
            if word.isdigit():
                num = int(word)
            elif word in cube_colors:
                if num > cube_colors[word]:
                    cube_colors[word] = num

        line_power = cube_colors["red"] * cube_colors["green"] * cube_colors["blue"]
        total += line_power

    print(f"total: {total}")

    #logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)

