'''
Creating star patterns using user defined functions
Create a function starline(n)  that takes an integer and prints a line of n stars.
Create a function starsquare(n) that will print an n X n square of stars; use starline.
Create a function starrect(n,m) the will print m lines, each with n stars
Create a function brokenline(n) that will print one star, n-2 spaces and a final star.
Create a function hollowsquare(n) that will print an n X n square, with stars on the
'''

# def starline(number_of_stars):
#     print(number_of_stars * "*")
#
# number_of_stars = input("Please enter your number here: ").strip()
# starline(int(number_of_stars))

#-------------------------------------------------
# def starsquare(top_of_square):
#     print(top_of_square * "x")
#     print(top_of_square * "x")
#     print(top_of_square * "x")
#     print(top_of_square * "x")
#
# top_of_square = 4
# starsquare(int(top_of_square))

#-------------------------------------------------
# def starrect(n, m):
#     print(n * "*", "\n", m * "*")
# n = 5
# m = 5
# starrect(n, m)
#--------------------------------------------------
def hollowsquare(square_hollow):
    for index_one in range(square_hollow):
        for index_two in range(square_hollow):
            if index_one==0 or index_one==square_hollow-1 or index_two==0 or index_two==square_hollow-1:
                print("*", end="")

square_hollow = 4
hollowsquare(square_hollow)