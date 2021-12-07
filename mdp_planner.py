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
    # Grab dictionaries
    states = mdp[0]
    actions = mdp[1]
    state_transitions = mdp[2]
    rewards = mdp[3]

    # Step 2: Update entire Q table using Bellman equation
    for s in states: # returns the state uniqueID key
        for a in actions: # returns the action uniqueID key
            # Calculate Q(s, a) with Bellman
            # See if the reward from our state to the next state is in our MDP. If not, use the value 0 where we need it
            value = 0

            # TODO first! Find out how to access calues we put in dictionary to be able to calculate Q values
            # print(mdp[s][a])
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
        print(data)
        label = data[1]
        label = label[:-1]
        states[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through actions, splitting into id and label, removing \n and putting in dictionary
    while line != '\n':
        data = line.split(",")
        print(data)
        label = data[1]
        label = label[:-1]
        actions[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # TODO fix for the overhead that occures in the dictionary
    # going through state transitions, splitting into 4 parts and nesting them into layers in the dictionary
    # counter is used to assign each transition a unique identifier to avoid overhead
    counter = 0
    while line != '\n':
        data = line.split(",") # Removes commas
        print(data)
        label = data[3] # Grabs the last value in the state transitions
        label = label[:-1] # Eliminates the \n from the integer
        last = {}
        last[data[2]] = label # Assigns the last value in State Transition as the value for the key of the value before it
        slast = {}
        slast[data[1]] = last # Assigns the second value as the key to the dictionary last that stores the 3 and 4 values in State Transitions
        third_last = {}
        third_last[data[0]] = slast # Assigns the first value as the key to the dictionary last that stores the 2, 3, and 4 values in State Transitions
        # Checks to see if the key is in our stateTransition already and goes to the next
        stateTransitions[counter] = third_last # Assigns the dictionary of the last 3 items in the list to our stateTransitions dictionary with the first value as the key
        counter += 1 # Increases unique identifier
        line = next(f) # Goes to the next line in our file
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
        rewards[data[0]] = slast

    value_iteration(mdp)


main()
