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
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
    total = 0
    for line in data:
        nums = re.findall(r'\d', line)
        new_num = nums[0] + nums[-1]
        total += int(new_num)
        print(new_num)
    print(total)
    logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
