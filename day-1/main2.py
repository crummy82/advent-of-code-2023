from pathlib import Path
import logging
import time
import re

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "sample_input2.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

NUM_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9"
}


def main():
    total = 0
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
    for line in data:
        first_num = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        if first_num[0].isdigit():
            num1 = first_num[0]
        else:
            num1 = NUM_WORDS[first_num[0]]

        line_backwards = "".join(str(x) for x in list(reversed(line)))

        last_num = re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line_backwards)

        if last_num[0].isdigit():
            num2 = last_num[0]
        else:
            num2 = NUM_WORDS[last_num[0]]

        new_num = num1 + num2
        total += int(new_num)
    print(total)
    logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
