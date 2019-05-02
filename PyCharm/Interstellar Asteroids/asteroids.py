# Hayden Whitney
# 5/19
# A Minecraft themed Asteroids game.

from superwires import games

games.init(screen_width=1020, screen_height=576, fps=60)


class Ship(games.Sprite):
    ship_img = games.load_image("Images/Ranger.png", transparent=True)

    def __init__(self):
        super(Ship, self).__init__(image=Ship.ship_img, x=games.screen.width/2, y=games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            self.y -= 2.5
        # if games.keyboard.is_pressed(games.K_DOWN) or games.keyboard.is_pressed(games.K_s):
            # self.y += 2.5
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= 3
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += 3

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():
    background_img = games.load_image("Images/Background.png", transparent=False)
    explosion_files = ["Images/explosion_1.png",
                       "Images/explosion_2.png",
                       "Images/explosion_3.png",
                       "Images/explosion_4.png",
                       "Images/explosion_5.png"]
    ship_img = Ship()
    explosion = games.Animation(images=explosion_files,
                                x=games.screen.width/2,
                                y=games.screen.height/2,
                                n_repeats=1,
                                repeat_interval=3)
    games.screen.add(ship_img)
    games.screen.add(explosion)
    games.screen.background = background_img
    games.screen.mainloop()


main()
