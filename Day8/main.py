import os

data_folder = "data"
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

for i in range(1, 11):
    directory = os.path.join(data_folder, "day" + str(i))
    os.mkdir(directory)
