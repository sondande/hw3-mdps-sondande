[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6501687&assignment_repo_type=AssignmentRepo)
# hw3-mdps
HW3: Robotic Wildfire Suppression (Markov Decision Processes)

1. A paragraph discussing how 𝛾 impacted the average utility earned by the agent – do you see any trends? What do you think these trends imply, and why did they occur?

   We noticed that the 𝛾 value impacted our average utility by how precise and how long our program would run. 𝛾 appears to be positively correlated with the average utility earned by the agent. When we started with a 𝛾 of 0.1, we had a negative utility(-8.2). As we increased 𝛾, it became positive at 0.5 and then continued to increase to 0.9. This trend implies that larger 
   gamma values when creating policy leads to more utility in a simulation. By using the gamma value as a determinant of when we define convergence occurs with our values, the depth of "accuracy" alongside utilizing the information gained from our tables was transparent. We can see through our line chart, the larger our Gamma value, the larger our average utility becomes. 
   From this, we are able to use that information to give us a time frame of gains. The larger our gamma value allows us to see long-term benefits from making a decision compared to a smaller gamma value, which can give us more information regarding short-term gains. This can be beneficial by how we define and interpret our domain. If we need to use this with a time constraint, 
   we can determine which response we need to take in order to reap desired benefits, if that may be short or long term. By having a larger gamma value, we are allowing more time to determine our average utility in the grand scheme. It will take longer to find our policy when the value is closer but still less than 1. We have more room to find possible options because we are looking
   for the utility over a longer period of time, which results in more care and methodical actions compared to a smaller value as we can find that a lot faster. We can see why this occurs due to how we utilize the value in our bellman equation alongside as our determinant. Overall, the trends we can see from our V, Q, and P tables show how the gamma value can determine the time frame 
   we are looking for and finding the average utility and best course of action for that time frame of benefits. 

2. A couple paragraphs documenting how you designed and implemented the MDP in your program? What design options did you consider, and how did you decide on this implementation?
   
   In this project, we designed and implemented the MDP in our program by utilizing dictionaries as our main data structures for the MDP and stored all the dictionaries in a list for easy access throughout our program. Through this, we took the file given to us, parsed it and stored the data to their respective data structures. We wanted to use 3D arrays to be able to store all the necessary information in our dictionaries for easy access
   and to be utilized in our value iteration function. In our value iteration function, we used our Q_table and V_table to keep our utility values and had a policy array that holds the state where we found the max q value four our state s in our v_table[s] at index s. From there, initialize and set all the values in our tables to 0 for the start of the function.
   After, we use a while loop that runs until convergence occurs for the max change in our V values. During this, we use the Bellman equation to update our tables and calculate our max change. After that, we apply save everything into our policy file. 

   Overall, we utilized this structure to allow our program to be malleable and could be used in a variety of situations. We wanted to have access to all the information given in our MDP files easily for the purpose of adhering changes between different files, types of information we are distinguishing, being able to identify information through unique identifiers,
   ensuring that everything had a unique identifier that could be utilized overall. Through this, we found it easier and more intuitive for programmers alongside users. We originally used layered dictionaries that would store dictionaries inside of dictionaries. This was a useful method but caused a ton of grief due to figuring out ways to filtering and accessing the 
   information we are searching to use. Using 3D arrays and maintaining it in this format allowed us to have easier access than before to the information in our dictionaries, be able to import it into our functions faster, and limit confusion overall.
    
3. A short paragraph describing your experience during the assignment (what did you enjoy, what was difficult, etc.)
   We really enjoyed ourselves working on this assignment. Understanding the purpose of Bellman equation and diving into the fundamentals of deep learning was fascinating. We spent a lot of time working on how we wanted to organize our code, rated the advantages and the disadvantages of using different data structures, and how to implement it into our algorithms. 
   The difficult parts were the structuring of our layered dictionary for all the states of the MDP. The structure of the Bellman equation was personally difficult for me (Sagana) for the terms of seeing how to structure and apply all the variety of variable and access the information 
   Accordingly so that I could utilize and store the information easily.

4. Probably about 20 Hours.
5. We have affirmed to the Honor Code on this Assignment. - Sagana Ondande & Oliver Rippen
