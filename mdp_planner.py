import sys
from operator import itemgetter
"""
CSCI 364: Professor Adam Eck
HW3 MDPs
12/09/2021
By: Sagana Ondande & Oliver Rippen
"""


"""
Saving Policy from Value Iteration to a File
"""


def save_to_file(v_table, filename):
    # clearing the file
    with open(filename, 'r+') as f:
        f.truncate(4)
    file = open(filename, 'w')  # opening file to write into
    for i in range(len(v_table)):  # iterating through each state in the v_table
        curr = str(i) + "," + str(v_table[i][1])  # putting state, action into correct format
        file.write(curr)  # writing line to the file
        file.write("\n")
    file.close()


"""
Value Iteration 

BIG NOTE: because we set all the values for the q and v tables to 0, if the transition or reward is not in the mdp 
file, the values will stay zero and no need to check and assign it/ calculate it 
"""


def value_iteration(mdp, gamma_value, policyFileName):
    # 1. Initialize Q table and V values to all zeros
    q_table = []  # Stores expected utilities using the bellman equation
    v_table = []  # Stores possible utilities for each action a state can take
    policy = []
    for state in range(len(mdp[0])):
        # the index in the q_table should be equal to the unique identifier of the state
        v_table.append(0.0)
        policy.append(0)

        # the index in the v_table should be equal to the unique identifier of the action
        action_list = []
        for action in range(len(mdp[1])):  # for the number of possible actions for every state
            action_list.append(0.0)
        q_table.append(action_list)

    # (Aka step 4. Repeat Steps 2-3 until V values converge * Largest change in V(s) is less than e)
    # While loop (until the largest change in V < e aka the covergence criteria is met)

    # Grab dictionaries
    states = mdp[0]
    actions = mdp[1]
    state_transitions = mdp[2]
    rewards = mdp[3]
    max_change = 1
    while max_change > gamma_value:
        max_change = 0
        # Step 2: Update entire Q table using Bellman equation
        for s in range(len(states)):  # returns the state uniqueID key
            for a in range(len(actions)):  # returns the action uniqueID key
                q_function = 0
                for next_state in state_transitions[str(s)][str(a)]:
                    probability = state_transitions[str(s)][str(a)][next_state]
                    if next_state in rewards[str(s)][str(a)]:
                        reward = rewards[str(s)][str(a)][next_state]
                    else:
                        reward = 0
                    v_state_value = v_table[int(next_state)]
                    
                    q_function += (probability * (reward + gamma_value * v_state_value))
                # Update Q table
                toup = (q_function, a)  # add what action leads to what q level in a tuple
                q_table[s][a] = toup  # put tuple into the q_table at state and action

        # Update V table
        for s in range(len(states)):
            # Test case to show we are grabbing the max value for state s in Q_table # q_table[0][1] = (5.0, 1)
            # finds the max of tuples and then allows us to store the second value in the tuple

            # This is where we store the max value of our Q values for state s
            new_v_value = max(q_table[s], key=itemgetter(0))[0]

            # We check to see if the value at index s is an integer. If so, we assign it as 0, if not, we take the first value in our tuple which is the v value for that prior state
            old_v_value = v_table[s]

            # we calculate to see if there was a larger max change. If so, we edit our max_change variable to be used for our next iteration of the while loop
            # from before, we just switch the values. This should go until our max value is less than 0.1 since that is the gamma value.
            if max_change < abs(new_v_value - old_v_value):

                max_change = abs(new_v_value - old_v_value)

            #This is where we store
            v_table[s] = new_v_value 
            policy[s] = (max(q_table[s], key=itemgetter(0))[0], max(q_table[s], key=itemgetter(0))[1])  # put the state at which the maximum q value is found into v_table[s]

    save_to_file(policy, policyFileName)  # call function to save the optimal actions at each state
    return


"""
Main function to call program

Values are stored in the stateTransition and Rewards dictionary in the format of the key being the currentState, 
and every element in the list are possible state transitions given or rewards for that current state 

StateTransition: State(key), [Action, Next_State, Probability] (list of state transition options for State)
Reward: State(key), [Action, Next_State, Reward] (list of reward options for State)
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

    # Read in gamma value from arguments
    gamma_value = float(sys.argv[2])

    # Read in policyFileName from arguments
    policyFileName = sys.argv[3]

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

    for state in states:
        stateTransitions[state] = {}

        for action in actions:
            stateTransitions[state][action] = {}

    while line != '\n':
        line = line.strip()
        data = line.split(",")  # Removes commas

        state = data[0]
        action = data[1]
        next_state = data[2]
        label = float(data[3])  # Grabs the last value in the state transitions

        stateTransitions[state][action][next_state] = label
        line = next(f)
    line = next(f)
    line = next(f)


    for state in states:
        rewards[state] = {}

        for action in actions:
            rewards[state][action] = {}

    # going through rewards, splitting into 4 parts and nesting them into layers in the dictionary
    for line in f:
        line = line.strip()
        data = line.split(",")  # Removes commas

        state = data[0]
        action = data[1]
        next_state = data[2]
        label = float(data[3])  # Grabs the last value in the state transitions
        rewards[state][action][next_state] = label

    value_iteration(mdp, gamma_value, policyFileName)


main()
