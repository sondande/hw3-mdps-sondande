import sys


def main():
    # Create Dictionaries
    states = {}
    actions = {}
    stateTransitions = {}
    rewards = {}

    # Read file in from arguments
    filename = sys.argv[1]

    # Open File
    f = open(filename)

    # Iterating through the file, placing data into the dictionaries
    line = next(f)
    line = next(f)

    # Going through states, splitting into id and label, removing \n and putting in dictionary
    while (line != '\n'):
        data = line.split(",")
        label = data[1]
        label = label[:-1]
        states[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through actions, splitting into id and label, removing \n and putting in dictionary
    while (line != '\n'):
        data = line.split(",")
        label = data[1]
        label = label[:-1]
        actions[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through state transitions, splitting into 4 parts and nesting them into layers in the dictionary
    while line != '\n':
        data = line.split(",")
        label = data[3]
        label = label[:-1]
        last = {}
        last[data[2]] = label
        slast = {}
        slast[data[1]] = last
        stateTransitions[data[0]] = slast
        line = next(f)
    line = next(f)
    line = next(f)

    # going through rewards, splitting into 4 parts and nesting them into layers in the dictionary
    for line in f:
        data = line.split(",")
        label = data[3]
        label = label[:-1]
        last = {}
        last[data[2]] = label
        slast = {}
        slast[data[1]] = last
        rewards[data[0]] = slast


main()
