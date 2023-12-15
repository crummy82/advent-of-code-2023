from pathlib import Path
import logging
import time

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "sample_input2.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
instructions = {}


def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
    command_str = data[0]

    for line in range(2, len(data)):
        instructions[data[line][:3]] = (data[line][7:10], data[line][12:15])

    new_instruction = "AAA"
    x = 0
    while new_instruction != 'ZZZ':
        cmd_num = x % len(command_str)
        if command_str[cmd_num] == "L":
            new_instruction = instructions[new_instruction][0]
        else:
            new_instruction = instructions[new_instruction][1]
        x += 1
    print(f'total: {x}')
    # logger.debug(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
