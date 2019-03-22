import sys, pygame, random

pygame.init()

size = width, height = 750, 1000
v_x, v_y = 0, 0
black = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
ballrect.bottom = height
t = 0

pressed_left = pressed_right = False
bells = []


class Bell(object):
    def __init__(self):
        self.image = pygame.image.load("ball.gif")
        self.x = random.randint(0, width - 250)
        self.y = random.randint(height / 4, height)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


bells = [Bell() for x in range(5)]

while True:
    ballrect = ballrect.move([v_x, v_y])

    if ballrect.bottom > height:
        ballrect.bottom = height
        v_y = t = 0

    if v_y != 0:
        delta = + .015 * t * t
        v_y = v_y + delta
        for bell in bells:
            bell.y += v_y + delta
        t += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and v_y == 0:
                v_y = -40

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False

    if pressed_left and ballrect.left - 20 >= 0:
        ballrect.left -= 20
    if pressed_right and ballrect.right + 20 <= width:
        ballrect.right += 20

    screen.fill(black)
    screen.blit(ball, ballrect)
    for bell in bells:
        bell.draw(screen)
    pygame.display.update()
    clock.tick(100)
