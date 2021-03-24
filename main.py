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
    print(new_logo[j][2][1])
    for k in range(len(new_engrave)):
        logo_name_e = new_engrave[k][1]
        if(logo_name_l == logo_name_e):
            start_x = int(new_engrave[k][2])
            start_y = int(new_engrave[k][3])
            print(start_x,start_y)



def draw(start_x ,start_y):
    for i in range(len(new_logo)):
        for k in range(len(new_logo[i][2])):
            if (new_logo[1][2][k] == "L"):
                surface[2 * (start_x) - 2][2 * (start_y) - 3] = "_"
                start_x = start_x
                start_y = start_y - 1
            elif (new_logo[1][2][k] == "L"):
                surface[2 * (start_x) - 2][2 * (start_y) - 3] = "_"
                start_x = start_x
                start_y = start_y - 1
            elif (new_logo[1][2][k] == "U"):
                surface[2 * (start_x) - 3][2 * (start_y) - 2] = "|"
                start_x = start_x - 1
                start_y = start_y
            elif (new_logo[1][2][k] == "R"):
                surface[2 * (start_x) - 2][2 * (start_y) - 1] = "_"
                start_x = start_x
                start_y = start_y + 1
            elif (new_logo[1][2][k] == "D"):
                surface[2 * (start_x) - 1][2 * (start_y) - 2] = "|"
                start_x = start_x + 1
                start_y = start_y
            else:
                break
        for row in surface:
            print(''.join(row))


# this could be helpfull
#[(’logo’, 2, 4), (’logo2’, 3, 4), 3, ’CMPE326’]

draw(start_x,start_y)

# if(new_logo[1][2][0] == "L"):
#     surface[2*(start_x)-2][2*(start_y)-3] = "_"
#     start_x = start_x
#     start_y = start_y-1
# if(new_logo[1][2][1] == "L"):
#     surface[2 * (start_x) - 2][2 * (start_y) - 3] = "_"
#     start_x = start_x
#     start_y = start_y - 1
# if(new_logo[1][2][2] == "U"):
#     surface[2*(start_x)-3][2*(start_y)-2] = "|"
#     start_x = start_x -1
#     start_y = start_y
# if(new_logo[1][2][9] == "R"):
#     surface[2 * (start_x) - 2][2 * (start_y) - 1] = "_"
#     start_x = start_x
#     start_y = start_y +1
# if(new_logo[1][2][17] == "D"):
#     surface[2 * (start_x) - 1][2 * (start_y) - 2] = "|"
#     start_x = start_x +1
#     start_y = start_y
#print(start_x)
#print(start_y)
#surface[1][0] = "|"
#surface[2][1] = "_"
# for printing the given matrix


# while True:
#     line = f.readline()
#     if (line.split() == "LOGO"):
#         logo.append(line)
#     elif (line.split() ==  "ENGRAVE"):
#         engrave.append(line)
#     if not line:
#         break