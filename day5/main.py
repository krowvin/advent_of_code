# 12/05/2023
# Start: 7:42PM -06:00
# End  : 9:41PM -06:00
# /u/krowvin
# https://adventofcode.com/2023/day/5

import time
# Enable extra output
DEBUG = False
INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"
# Run test_input.txt and see if you get the expected lowest location of 35:
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
# PASSING

almanac = {}    
seeds = []

# Import the file data
def readInputFile(filename: str):
    print(f"Reading {filename}...")
    with open(filename) as input_file:
        # Remove any empty lines
        return [l.strip() for l in input_file.readlines()]

def parseInput(lines: str):
    global seeds
    a_map = "overflow"
    for line in lines:
        # Skip empty lines
        if not line: continue
        # Determine our almanac map keys
        if line.find(" map:") >= 0:
            a_map = line.split(" map:")[0]
        # Seeds? (might not be on the first line!)
        elif line.startswith("seeds: "):
            seeds = list(map(int, line.split(": ")[1].split(" ")))
        else:
            # dest range start, source range start, range length
            drs, srs, rl = list(map(int, line.split(" ")))
            if a_map not in almanac:
                almanac[a_map] = [[drs, srs, rl]]
            else:
                almanac[a_map].append([drs, srs, rl])

def sourceToDestination(a_map, requested_src):
    # dest range start, source range start, range length
    for drs, srs, rl in almanac[a_map]:
        # Determine our source range
        MIN_SRS_VAL = srs
        MAX_SRS_VAL = srs + rl
        # See if our requested source value falls in that range
        if MIN_SRS_VAL <= requested_src <= MAX_SRS_VAL:
            # Get a positive value from the minimum
            delta = abs(MIN_SRS_VAL - requested_src)
            # Add that value to our destination range start
            return drs + delta
    # Return the entry if it does not exist
    return requested_src

def getDestination(a_map, src):
    try:
        return almanac[a_map]["dst"][almanac[a_map]["src"].index(src)]
    except ValueError as err:
        return src


def run():
    start_ns = time.perf_counter()
    # Populate the almanac with our data
    parseInput(readInputFile(INPUT_FILE))
    output = {"seeds": [], "locations": []}
    for seed in seeds:
        output_str = ""
        dst = seed
        output[seed] = None
        output_str += f"Seed {seed}, "
        for entry in almanac:
            # Map the previous destination to the next entry in the almanac
            dst = sourceToDestination(entry, dst)
            output_str += f'{entry.split("-")[-1]} {dst}, '
        print("".join(output_str[:-2]))
        # Set the seed locations
        output["seeds"].append(seed)
        output["locations"].append(dst)
    lowest_loc = min(output["locations"])
    print(f'The lowest location number is {lowest_loc} for seed {output["seeds"][output["locations"].index(lowest_loc)]}')
    print(f"Completed in {round(time.perf_counter() - start_ns, 4)}s")

if __name__ == "__main__":
    run()
