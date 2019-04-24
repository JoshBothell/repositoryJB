# Super Saudi Oil Snatchers
# By JoshBothell
# 4/19

# import
from superwires import games, color
import random
import pygame

game_over = False
# screen creation
games.init(screen_width=990,
           screen_height=743,
           fps=60)
pygame.display.set_caption("Somewhere in Saudi Arabia, probably near civilians.")
icon = games.load_image("sprites/saudi icon.jpg", transparent=True)
pygame.display.set_icon(icon)


# classes
class Oil(games.Sprite):
    # load the image
    global game_over
    image = games.load_image("sprites/oil.png")

    def __init__(self, x, y=123):
        super(Oil, self).__init__(image=Oil.image, x=x, y=y, dy=random.randrange(1, 10))

    def update(self):
        if self.top > games.screen.height:
            self.destroy()
            self.end_game()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        global game_over
        end_message = games.Message(value="GAME OVER",
                                    size=120,
                                    color=color.dark_red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=10*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)
        game_over = True


class Soldier(games.Sprite):
    global game_over
    image = games.load_image("sprites/soldier.png")

    def __init__(self):
        super(Soldier, self).__init__(image=Soldier.image,
                                      x=games.mouse.x,
                                      bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width-10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
        if game_over:
            self.end_game()

    def check_catch(self):
        for oil in self.overlapping_sprites:
            oil.handle_caught()
            self.score.value += 10
            self.score.right = games.screen.width - 10

    def end_game(self):
        self.destroy()


class CrownPrince(games.Sprite):
    image = games.load_image("sprites/saudi.png", transparent=True)

    def __init__(self, y=55, speed=5, odds_change=100):
        super(CrownPrince, self).__init__(image=CrownPrince.image,
                                          x=games.screen.width/2,
                                          y=y,
                                          dx=speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_oil = Oil(x=self.x)
            games.screen.add(new_oil)
            self.time_til_drop = random.randrange(10, 200)


class ScText(games.Text):
    pass


# main
def main():
    # load images
    bg_img = games.load_image("sprites/background.jpg", transparent=False)

    # create objects
    soldier = Soldier()
    crown_prince = CrownPrince()
    # oil = Oil(200)

    # draw objects
    games.screen.background = bg_img
    add = games.screen.add
    add(soldier)
    add(crown_prince)
    # add(oil)
    # set up mouse

    # start game loop
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()


# startup
main()
