from turtle import Screen
from snake import Snake
from food import Food
from score import Score

window = Screen()
window.setup(1280,768)

score = Score()

food = Food()
food.create_food()

cobra = Snake()
cobra.create_snake()

speed_input = window.textinput("Difficulty", "slow(s)\nnormal(n)\nfast(f)\nfastest(v)").lower()

snake_speed = 0.2
if speed_input=="s":
    snake_speed = 0.2
elif speed_input=="n":
    snake_speed = 0.09
elif speed_input=="f":
    snake_speed = 0.06
elif speed_input=="v":
    snake_speed = 0.02

def move_cobra():
    gameOn = True
    global snake_speed
    while gameOn:
        if food.distance(cobra.snake_cells[0].pos()) <= 15.0:
            score.clear()
            score.update_score()
            score.show_score()
            food.create_food()
            x, y = cobra.snake_cells[-1].pos()
            cobra.add_cell(x, y)

        if cobra.snake_cells[0].xcor() >= 660.0 or cobra.snake_cells[0].xcor() <= -660.0 or cobra.snake_cells[0].ycor() >= 330.0 or cobra.snake_cells[0].ycor() <= -330.0:
            score.over()
            break
        else:
            cobra.move(snake_speed)
            for cells in cobra.snake_cells[1:]:
                if cobra.snake_cells[0].distance(cells)<15.0:
                    score.over()
                    gameOn=False
                    break

window.listen()
window.onkeypress(move_cobra)
window.onkeypress(cobra.up, "w")
window.onkeypress(cobra.down, "s")
window.onkeypress(cobra.right, "d")
window.onkeypress(cobra.left, "a")

window.exitonclick()
