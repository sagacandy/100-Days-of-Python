import os

for i in range(1, 101):
    if not (os.path.exists(f"Python-Projects/Day{i}")):
        os.mkdir(f"Python-Projects/Day{i}")

        read_path = os.path.join(f"Python-Projects/Day{i}", "readme.md")
        with open(read_path, "w"):
            pass
