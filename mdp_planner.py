import sys

"""
Value Iteration 
"""


def value_iteration(mdp):
    # 1. Initialize Q table and V values to all zeros
    q_table = []
    v_table = []
    for state in range(len(mdp[0])):
        # the index in the q_table should be equal to the unique identifier of the state
        q_table.append(0)

        # the index in the v_table should be equal to the unique identifier of the action
        action_list = []
        for action in range(len(mdp[1])):
            action_list.append(0)
        v_table.append(action_list)

    # (Aka step 4. Repeat Steps 2-3 until V values converge * Largest change in V(s) is less than e)
    # While loop (until the largest change in V < e aka the covergence criteria is met)
    # TODO add after testing 2-3 and ensuring it is correct

    # Step 2: Update entire Q table using Bellman equation
    for s in mdp[0]:
        for a in mdp[1]:
            # Calculate Q(s, a) with Bellman
            value = 0
            # See if the reward from our state to the next state is in our MDP. If not, use the value 0 where we need it


            # TODO if we run into an error that a possible transition doesn't have a reward or a reward doens't have a transition, the value is zero. Was specified in the homework assignment listing as
            # The ones not listed in the MDP have values of 0 for probability or reward value. Dependant on which one is missing


    return


"""
Main function to call program
"""


def main():
    # Create Dictionaries
    states = {}
    actions = {}
    stateTransitions = {}
    rewards = {}

    # Creation of Markov Decision Process
    mdp = [states, actions, stateTransitions, rewards]

    # Read file in from arguments
    filename = sys.argv[1]

    # Open File
    f = open(filename)

    # Iterating through the file, placing data into the dictionaries
    line = next(f)
    line = next(f)

    # Going through states, splitting into id and label, removing \n and putting in dictionary
    while line != '\n':
        data = line.split(",")
        label = data[1]
        label = label[:-1]
        states[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through actions, splitting into id and label, removing \n and putting in dictionary
    while line != '\n':
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
        if(data[0] in stateTransitions):
            newList = stateTransitions[data[0]]
            newList.append(slast)
            stateTransitions[data[0]] = newList
        else:
            newList = []
            newList.append(slast)
            stateTransitions[data[0]] = newList
        line = next(f)
    line = next(f)
    line = next(f)

    # going through rewards, splitting into 4 parts and nesting them into layers in the dictionary
    # TODO when using a debugger, I found that the size of the dictionary for rewards was only 9 instead of the expected 18. This also happens in state transitions
    for line in f:
        data = line.split(",")
        label = data[3]
        label = label[:-1]
        last = {}
        last[data[2]] = label
        slast = {}
        slast[data[1]] = last
        if(data[0] in rewards):
            newList = rewards[data[0]]
            newList.append(slast)
            rewards[data[0]] = newList
        else:
            newList = []
            newList.append(slast)
            rewards[data[0]] = newList
    

    print(rewards['4'])
    #value_iteration(mdp)


main()
