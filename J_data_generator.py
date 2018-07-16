

import os, glob



# randomly samples some of the files from the directory
def select_files(directory):
    for filename in glob.iglob(os.path.join(directory, "**", "*.txt"), recursive=True):
        print (filename)
        # with open(filename) as file:
        #     for line in file:


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
select_files()
