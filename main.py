import sys

surface = [['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.']]

# for row in surface:
#
#     print(''.join(row))


#input = input()




# opens the file and reads the lines from given file
with open("tests/test1.in","r") as f:
    lines = [line.strip() for line in f]
print(lines)

# appends all related inputs to the related lists
# the reason is to making process easier
logo = [s for s in lines if "LOGO" in s]
engrave = [i for i in lines if "ENGRAVE" in i]
same = [j for j in lines if "SAME" in j]
print(logo)
print(engrave)
print(same)


# creating new lists inside list to compare logo names and proceed this lists
new_logo = []
for i in range(len(logo)):
    new_logo.append(logo[i].split())
new_engrave = []
for i in range(len(engrave)):
    new_engrave.append(engrave[i].split())
new_same = []
for i in range(len(same)):
    new_same.append(same[i].split())
print(new_logo)
print(new_engrave)
print(new_same)

#check the logo names and if input is engrave then initiliaz the starting point and draw the logo
for j in range(len(new_logo)):
    logo_name_l = new_logo[j][1]
    for k in range(len(new_engrave)):
        logo_name_e = new_engrave[k][1]
        if(logo_name_l == logo_name_e):
            start_x = int(new_engrave[k][2])
            start_y = int(new_engrave[k][3])
            print(start_x,start_y)

# this could be helpfull
#[(’logo’, 2, 4), (’logo2’, 3, 4), 3, ’CMPE326’]

surface[1][0] = "|"
surface[2][1] = "_"
# for printing the given matrix
for row in surface:
    print(''.join(row))






# while True:
#     line = f.readline()
#     if (line.split() == "LOGO"):
#         logo.append(line)
#     elif (line.split() ==  "ENGRAVE"):
#         engrave.append(line)
#     if not line:
#         break