from turtle import Turtle
import time
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")
HIGH_SCORE = 0
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("hotpink") 
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
            
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()      
         
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.getscreen().update()
        time.sleep(2)  # Optional: Pause for 2 seconds to let the player see the message
        self.clear()