import sys, pygame

pygame.init()

size = width, height = 750, 1000
v_x, v_y = 0, 0
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
ballrect.bottom = height
t = 0

pressed_left = pressed_right = False

while True:
    ballrect = ballrect.move([v_x, v_y])

    if ballrect.bottom > height:
        # Hit ground
        ballrect.bottom = height
        v_y = t = 0

    print('v_y: {}, t: {}'.format(v_y, t))

    if v_y != 0:
        v_y = v_y + .015 * t * t
        t += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
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
    pygame.display.update()
    clock.tick(100)
