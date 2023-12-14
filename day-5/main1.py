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
    seeds = []
    mapping = {}
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    for piece in range(1, len(data[0].split())):
        seeds.append(data[0].split()[piece])

    for line in data:
        broken_line = line.split()

        if line and broken_line[0].isdigit():
            dest_min = int(broken_line[0])
            src_min = int(broken_line[1])
            src_max = src_min + int(broken_line[2])
            for seed in seeds:
                if src_min <= int(seed) <= src_max:
                    seed_diff = int(seed) - src_min
                    dest_num = dest_min + seed_diff
                    mapping[seed] = dest_num

        elif not line:
            for i in range(len(seeds)):
                if seeds[i] in mapping:
                    seeds[i] = mapping[seeds[i]]
            mapping = {}

    for i in range(len(seeds)):
        if seeds[i] in mapping:
            seeds[i] = mapping[seeds[i]]
    
    lowest = int(seeds[0])

    for seed in seeds:
        if int(seed) < lowest:
            lowest = int(seed)
    print(f"lowest: {lowest}")
    # logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
