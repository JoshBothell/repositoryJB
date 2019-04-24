
from superwires import games, color
import random

SCORE = 0

games.init(screen_width=990, screen_height=743, fps=50)


class Soldier(games.Sprite):
    """A US marine controlled by the mouse"""
    def update(self):
        """Move to mouse coordinates"""
        self.x = games.mouse.x
        # self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        for oil in self.overlapping_sprites:
            oil.handle_collision()


class Oil(games.Sprite):
    def update(self):
        global SCORE
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            SCORE += 1
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
            SCORE += 1

        # global SCORE
        # if self.left > games.screen.width:
        #     self.right = 0
        #     SCORE += 1
        # if self.right < 0:
        #     self.left = games.screen.width
        #     SCORE += 1
        # if self.top > games.screen.height:
        #     self.top = 0
        #     SCORE += 1
        # if self.top < 0:
        #     self.bottom = games.screen.height
        #     SCORE += 1
    def handle_collision(self):
        self.dx = -self.dx
        self.dy = -self.dy


class ScText(games.Text):
    def update(self):
        self.value = SCORE


def main():
    bg_img = games.load_image('sprites/background.jpg', transparent=False)
    oil_img = games.load_image("sprites/oil.png")
    soldier_img = games.load_image("sprites/soldier.png")

    games.screen.background = bg_img

    oil = Oil(image=oil_img,
              x=games.screen.width/2,
              y=games.screen.height/2,
              dx=random.randint(-10, 10),
              dy=random.randint(-10, 10),
              )
    score = ScText(value=SCORE,
                   size=60,
                   color=color.black,
                   x=900,
                   y=30,
                   is_collideable=False)
    soldier = Soldier(image=soldier_img,
                      x=games.mouse.x,
                      y=100)

    add = games.screen.add

    add(oil)
    add(score)
    add(soldier)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()


#game_over = games.Message(value="Game Over",
# )


main()
