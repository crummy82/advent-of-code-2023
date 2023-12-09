
from pathlib import Path
import logging
import time

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

    total = 1
    full_time = ""
    full_distance = ""

    for line in data:
        broken_line = line.split()
        if broken_line[0] == "Time:":
            for x in range(1, len(broken_line)):
                full_time += broken_line[x]
        else:
            for x in range(1, len(broken_line)):
                full_distance += broken_line[x]

    time_int = int(full_time)
    count = 0
  
    for millis in range(time_int + 1):
        dist = int(millis) * (time_int - int(millis))
        if dist > int(full_distance):
            count += 1

    total *= count

    print(f"total: {total}")

    # logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
