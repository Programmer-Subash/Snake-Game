from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


class SnakeGame:

    def __init__(self, title="Snake Game", width=800, height=800, window_color="white", snake_color="black",
                 food_color="green"):
        self.width = width
        self.height = height
        self.snake_color = snake_color
        self.food_color = food_color
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.setup(width=width, height=height)
        self.screen.title(title)
        self.screen.tracer(0)
        self.screen.bgcolor(window_color)
        self.snake = Snake(snake_color)
        self.snake.create_snake()
        self.food = Food(width, height, food_color)
        self.food.move_to_random_location()
        self.score = Score(self.width, self.height)
        self.game_over = False

    def start_game(self):
        self.screen.clear()
        self.game_over = False
        self.snake = Snake(self.snake_color)
        self.snake.create_snake()
        self.food.move_to_random_location()
        self.score = Score(self.width, self.height)

    def is_shake_eat_food(self):
        if self.snake.segments[0].distance(self.food) < 15:
            self.food.move_to_random_location()
            self.score.update_score(1)
            last_segment_position = self.snake.segments[-1].position()
            self.snake.add_segment(last_segment_position)

    def detect_collisions_with_snake(self):
        border = 5
        head = self.snake.segments[0]
        x, y = head.position()
        if x > (self.width // 2 - border) or x < (-self.width // 2 + border) or y > (self.height // 2 - border) or y < (
                -self.height // 2 + border):
            self.score.update_highest_score()
            self.score.game_over_message()
            self.game_over = True

    def detect_collisions_with_tail(self):
        head = self.snake.segments[0]
        for segment in self.snake.segments[1:-1]:
            if segment.distance(head) < 15:
                self.score.update_highest_score()
                self.score.game_over_message()
                self.game_over = True

    def game_loop(self):
        while True:
            self.screen.update()
            self.score.show_score()
            time.sleep(0.030)
            self.screen.onkeypress(self.snake.up, "Up")
            self.screen.onkeypress(self.snake.down, "Down")
            self.screen.onkeypress(self.snake.left, "Left")
            self.screen.onkeypress(self.snake.right, "Right")
            self.screen.listen()
            self.snake.move()
            self.is_shake_eat_food()
            self.detect_collisions_with_snake()
            if self.game_over:
                break

                
window = SnakeGame()
window.game_loop()
window.screen.mainloop()
