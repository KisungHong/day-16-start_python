# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.canvheight
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["피카츄", "라이츄", "파이리", "꼬부기"])
table.add_column("Pokemon Type", ["전기", "전기", "불", "물"])

print(table.align)
table.align = "l"
print(table)
