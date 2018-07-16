

import os, glob
import random


# randomly samples some of the files from the directory
def select_files(directory, num):
    count  = 0
    list_files = []
    random.seed(1001)


    # deterministically retrieves the files. We need to randomly skip iterations then!

    for filename in glob.iglob(os.path.join(directory, "**", "*.txt"), recursive=True):
        if len(list_files) > num: break
        print (filename)
        # count+=1
        # if count>100:
        #     break

        if random.random() > 0.001:
            list_files.append(filename)


    return list_files


'''

Given a list of files, creates a concatenated text file in the style of ptb.test.txt

'''
def create_concat_file(files):

    for input_file in files:
        with open ("draft_test.txt", "a") as write_file, open(input_file, "r") as file:
            # essentially, just dump the content. Alternatively, there may be some preprocessing
            write_file.write(file.read())




    pass


print ("hello")
files = select_files("../pubmed_data/unzipped/", 100)
create_concat_file(files)