# access.log 
access = "/home/franksteps/Área de trabalho/programming/python/split/access.log"

# count
with open(access, "r") as f:
    length_acess = sum(1 for _ in f)

# split
with open(access, "r") as f:
   for row_num in range(length_acess):
        line = f.readline()
        part = line.split()
        for column_num in range(5):
            print(part[column_num])
        print("**************")

