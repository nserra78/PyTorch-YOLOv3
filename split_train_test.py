import os
import random

directory = os.getcwd()+"/data/custom/"


files_img = os.listdir(directory+"images/")
random.shuffle(files_img)

print(files_img)

test_sample = int(0.15*len(files_img))

train_files = files_img[test_sample:]
test_files = files_img[:test_sample]


print("**************************")
print("Train sample: {}/{} ".format(len(train_files), len(files_img)))
print("Test sample: {}/{} ".format(len(test_files), len(files_img)))
print("**************************")


with open(directory+"train.txt", "w") as ftrain, open(directory+"valid.txt", "w") as fval:
    for ifile in train_files:
        fname = directory+"images/"+ifile+"\n"
        ftrain.write(fname)

    for ifile in test_files:
        fname = directory+"images/"+ifile+"\n"
        fval.write(fname)








