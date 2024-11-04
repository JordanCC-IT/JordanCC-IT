# Draw a Tree!!

#               *
#              ***
#             *****
#            *******
#           *********
#          ***********
#               *

#height = 6
# 6 * 2 = 12-1

def tree (height):
    # Your code goes here
    length = height * 2 - 1
    stars = 1
    for i in range(1, height + 1):
        print (("*" * stars).center (length))
        stars +=2
    print("*".center(length))

tree(9)
tree(20)