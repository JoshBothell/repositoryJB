# Parker Dean
# Astroids 2.0
# 5/6/19
# major overhaul, final revision


# imports
from superwires import games
import random
import math

games.init(screen_width=1000, screen_height=500, fps=60)


# Global variables

# Classes
class Wrapper(games.Sprite):
    def update(self):
        """ Wrap around screen. """
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """Destroy object."""
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()
        # check if ship overlaps any other object
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPAWN = 2
    images = {SMALL: games.load_image("images/small_tie.png"),
              MEDIUM: games.load_image("images/med_tie.png"),
              LARGE: games.load_image("images/big_tie.png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x,
            y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size

    def die(self):
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x=self.x, y=self.y, size=self.size - 1)
                games.screen.add(new_asteroid)
        super(Asteroid, self).die()


class Ship(Collider):
    image = games.load_image("images/ship.png")
    sound = games.load_sound("sounds/thruster.wav")

    ROTATION_STEP = 5
    VELOCITY_STEP = .075
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.missile_wait = 0

    def update(self):
        super(Ship, self).update()
        # missile counter
        if self.missile_wait > 0:
            self.missile_wait -= 1

        # key setups
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Ship.ROTATION_STEP

        # apply thrust
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            angle = self.angle * math.pi / 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # fire missile if spacebar pressed
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait <= 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY


class Missile(Collider):
    image = games.load_image("images/laserbeam.jpg")
    sound = games.load_sound("sounds/laser_shot.wav")
    BUFFER = 58
    VELOCITY_FACTOR = 12
    LIFETIME = 20

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y, dx=dx, dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    sound = games.load_sound("sounds/explosion.wav")
    images = ["images/explosion_1.png",
              "images/explosion_2.png",
              "images/explosion_3.png",
              "images/explosion_4.png",
              "images/explosion_5.png", ]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x, y=y,
                                        repeat_interval=4, n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


# main
def main():
    # loading data
    bg_img = games.load_image("images/background.png")
    # create objects
    for i in range(4):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)
    player = Ship(x=games.screen.width / 2, y=games.screen.height / 2)
    # draw to screen
    games.screen.background = bg_img
    games.screen.add(player)
    # set up game
    # start main loop
    games.screen.mainloop()


main()