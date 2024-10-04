""" Seminar Activity 3 in-class demos
"""

# filename = input("Filename: ")
# out_file = open("output.txt", 'w')
# in_file = open(filename, 'r')
# for line in in_file:
#     if line.startswith('#'):
#         print(line, file=out_file)
# in_file.close()
# out_file.close()

# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)
# print("Done")

strings = ["Bob", 'broadband', 'tab']
for i, string in enumerate(strings, 1):
    out_file = open(f"{string}.txt", 'w')
    print(string, i, file=out_file)
    out_file.close()
    
