import os

for root, dir, files in os.walk("/home/ubuntu/hadoop/"):
    for file in files:
        if file.upper().startswith("LICENSE"):
            print(f"{root}/{file}")
