import os
import numpy as np



# all the possible file names from data/grasps
possible_grasps = os.listdir('data/grasps')

# randomly choose 5 of them
random_grasps = np.random.choice(possible_grasps, 5)

# print the object names
print('The objects are: ')
for grasp in random_grasps:
    # ignore the string after '_'
    print(grasp.split('_')[0], end='  ')
print()

# format the command to run the scene generator
command = """python3.8 scripts/acronym_generate_scene.py --objects \\
           data/grasps/{} \\
           data/grasps/{} \\
           data/grasps/{} \\
           data/grasps/{} \\
           data/grasps/{} --support \\
           data/grasps/Table_99cf659ae2fe4b87b72437fd995483b_0.009700376721042367.h5
           """
print("To use the scene generator, run the following command:")
print(command.format(*random_grasps))