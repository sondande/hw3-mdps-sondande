import sys
from operator import itemgetter

"""
Saving Policy from Value Iteration to a File
"""


def save_to_file(v_table, filename):
    # clearing the file
    #print(filename)
    with open(filename, 'r+') as f:
        f.truncate(4)
    file = open(filename, 'w')  # opening file to write into
    for i in range(len(v_table)):  # iterating through each state in the v_table
        curr = str(i) + "," + str(v_table[i][1])  # putting state, action into correct format # TODO Changed becasue the value is no longer a tuple and just an assigned value
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
    for state in range(len(mdp[0])):
        # the index in the q_table should be equal to the unique identifier of the state
        v_table.append(0.0)

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
        #max_change = 0
        # Step 2: Update entire Q table using Bellman equation
        for s in range(len(states)):  # returns the state uniqueID key
            for a in range(len(actions)):  # returns the action uniqueID key
                # Calculate Q(s, a) with Bellman
                # See if the reward from our state to the next state is in our MDP. If not, use the value 0 where we need it

                probability = state_transitions.get(str(s),
                                                    0)  # grabs second layer dictionary if it exists, if not found, assigned probability the integer value 0
                if probability != 0:  # checks if it the integer value 0. If it is, we skip right to finding the reward value
                    for transitions in probability:
                        probability = transitions.get(str(a),
                                                      0)  # grabs third layer dictionary if it exists, if not found, assigned probability the integer value 0
                        if probability != 0:
                            next_state = transitions[str(a)]
                            probability = float(next(iter(next_state.values())))
                            # Just in case to break for loop
                            break

                # Grab reward if it exists from rewards
                reward = rewards.get(str(s), 0)  # grabs second layer dictionary if it exists, if not found, assigned probability the integer value 0
                if reward != 0:  # checks if it the integer value 0. If it is, we skip right to calculating the bellman equation
                    for r in reward:
                        reward = r.get(str(a),
                                       0)  # grabs third layer dictionary if it exists, if not found, assigned probability the integer value 0
                        if reward != 0:
                            next_state = r[str(a)]
                            reward = float(next(iter(next_state.values())))
                            # Just in case to break for loop
                            break

                # Created to prevent out of index error when working with the v_table
                if s + 1 == len(states):
                    v_state_value = 1  # as it wouldn't cause any change like not moving
                else:
                    #if not isinstance(v_table[s + 1], int):
                    if type(v_table[s+1]) is not float:
                        print(type(v_table[s+1]))
                        print(v_table[s + 1])
                        v_state_value = v_table[s + 1][0]  # takes next value in the v_table
                    else:
                        v_state_value = v_table[s + 1]
                # Bellman equation to solve for the Q value for the currentState s and the action a
                q_function = probability * (reward + gamma_value * v_state_value)

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
            if(isinstance(v_table[s], float)):
                print("here")
                old_v_value = 0.0
            else:
                old_v_value = v_table[s][0]
            #print(abs(new_v_value - old_v_value))

            # we calculate to see if there was a larger max change. If so, we edit our max_change variable to be used for our next iteration of the while loop
            # TODO changed from < to > because we want to see if the change in max value is less than the gamma value. As a result, we want to take the prior value and the new calculated and substratct them. If our change was greater
            # from before, we just switch the values. This should go until our max value is less than 0.1 since that is the gamma value.
            if max_change > abs(new_v_value - old_v_value):

                max_change = abs(new_v_value - old_v_value)

            #This is where we store
            v_table[s] = (max(q_table[s], key=itemgetter(0))[0], max(q_table[s], key=itemgetter(0))[1])  # put the state at which the maximum q value is found into v_table[s]
            #print(v_table)

    save_to_file(v_table, policyFileName)  # call function to save the optimal actions at each state
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

    while line != '\n':
        data = line.split(",")  # Removes commas
        label = data[3]  # Grabs the last value in the state transitions
        label = label[:-1]  # Eliminates the \n from the integer
        last = {}
        last[data[2]] = label  # Assigns the last value in State Transition as the value for the key of the value before it
        slast = {}
        slast[data[1]] = last  # Assigns the second value as the key to the dictionary last that stores the 3 and 4 values in State Transitions
        if (data[0] in stateTransitions):  # We see if the leading current state in the state transition is in our dictionary. If so, add new reward to list
            newList = stateTransitions[data[0]]
            newList.append(slast)
            stateTransitions[data[0]] = newList
        else:  # if not, append it to our stateTransition dictionary
            newList = []
            newList.append(slast)
            stateTransitions[data[0]] = newList
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
        if (data[0] in rewards):
            newList = rewards[data[0]]
            newList.append(slast)
            rewards[data[0]] = newList
        else:
            newList = []
            newList.append(slast)
            rewards[data[0]] = newList

    # print(rewards['4'])
    value_iteration(mdp, gamma_value, policyFileName)


main()
