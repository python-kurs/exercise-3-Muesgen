# Exercise 3
from pathlib import Path
# import functions from utils here

data_dir = Path("C:/Users/mmues/Documents/Python/exercise-3-Muesgen/data/")
output_dir = Path("C:/Users/mmues/Documents/Python/exercise-3-Muesgen/solution/")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

path_txt = Path(data_dir, "cars.txt")

# 2. Read the text file [2P]

with open(path_txt) as file:
    cars = [line.rstrip() for line in file]

# 3. Count the occurences of each item in the text file [2P]

carnumbers = dict((x,cars.count(x)) for x in set(cars))

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

subdir = output_dir
# check if path exists
dir_exists = subdir.exists()
print("Directory exists: {}".format(dir_exists))
# create path if is not excisting
subdir.mkdir(parents = True, exist_ok = True)
print("Directory exists after creation: {}".format(subdir.exists()))

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

import csv

with open(output_dir / 'counts.csv', "w") as myfile:
    writer = csv.DictWriter(myfile, fieldnames=["item", "count"]) 
    writer.writeheader()
    for key in carnumbers.keys():
            myfile.write("%s,%s\n"%(key,carnumbers[key])) 