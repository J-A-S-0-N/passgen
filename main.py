import random 

lis = ["A", "B","A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",	"N",	"O","P","Q",	"R",	"S","T",	"U",	'V',"W",	"X",	"Y",	"Z"]
final = []

#  = ["q", ]

# def main():
inp = input(">> ")
# a = random.choice(lis)
for i in range(0, int(inp)):
    a = random.choice(lis)
    final.append(a)

final_str = "".join(final)
print(final_str)