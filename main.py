import pygame

# screen
scrwidth = 600
scrheight = 600
win = pygame.display.set_mode((scrwidth, scrheight))

# Sprites
plane1 = pygame.image.load('plane1.png')
plane2 = pygame.image.load('plane2.png')
bg = pygame.image.load('backdrop.png')



class p1(object):
    def __init__(self):
        self.x1 = 300
        self.y1 = 0
        self.vel1 = 20
        self.hitobx = (self.x1 + 17, self.y1 + 3, 57, 65)
        self.health = 10
        self.visible = True

    def draw(self, win):
        if self.visible:
            win.blit(plane1, (self.x1, self.y1))
            self.hitbox = (self.x1 + 2, self.y1 + 11, 35, 52)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            # healthbar
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 5, self.hitbox[1] + 60, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0] - 5, self.hitbox[1] + 60, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x1 + 17, self.y1 + 2, 31, 57)
        else:
            text = font.render("Player 2 Wins", 1, (255, 255, 255))
            win.blit(text, (250, 250))

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


class p2(object):
    def __init__(self):
        self.x2 = 300
        self.y2 = 530
        self.vel2 = 20
        self.hitobx = (self.x2 + 17, self.y2 + 10, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        if self.visible:
            win.blit(plane2, (self.x2, self.y2))
            self.hitbox = (self.x2 + 9, self.y2 + 11, 45, 52)
            # pygame.draw.rect(win, (55, 0, 0), self.hitbox, 2)

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 3, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0] - 3, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x2 + 17, self.y2 + 2, 31, 57)
        else:
            text = font.render("Player 1 Wins", 1, (255, 255, 255))
            win.blit(text, (250, 250))


    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit1')


def gamewin():
    #win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    pn1.draw(win)
    pn2.draw(win)

    # bullets
    for bullet in bullets:
        bullet.draw(win)
    for bullet in bullets1:
        bullet.draw(win)
    pygame.display.update()


class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 40

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


pygame.init()
font = pygame.font.SysFont('comicsans', 30, True)
pygame.display.set_caption("PlaneJAM")
bullets = []
bullets1 = []

pn1 = p1()
pn2 = p2()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:

        if bullet.y < 600:
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

        # plane2 hitbox
        if bullet.y - bullet.radius < pn2.hitbox[1] + pn2.hitbox[3] and bullet.y + bullet.radius > pn2.hitbox[
            1]:
            if bullet.x + bullet.radius > pn2.hitbox[0] and bullet.x - bullet.radius < pn2.hitbox[0] + pn2.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                pn2.hit()

    for bullet1 in bullets1:
        if bullet1.y > 0:
            bullet1.y -= bullet1.vel
        else:
            bullets1.pop(bullets1.index(bullet1))

        # plane 1 hit
        if bullet1.y - bullet1.radius < pn1.hitbox[1] + pn1.hitbox[3] and bullet1.y + bullet1.radius > pn1.hitbox[
            1]:
            if bullet1.x + bullet1.radius > pn1.hitbox[0] and bullet1.x - bullet1.radius < pn1.hitbox[0] + pn1.hitbox[
                2]:
                bullets1.pop(bullets1.index(bullet1))
                pn1.hit()

    # plane1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pn1.x1 > pn1.vel1:
        pn1.x1 -= pn1.vel1
    if keys[pygame.K_RIGHT] and pn1.x1 < 600 - pn1.vel1 - 40:
        pn1.x1 += pn1.vel1
    if keys[pygame.K_SPACE]:
        if len(bullets) < 10:
            bullets.append(
                projectile(round(pn1.x1 + 40 // 2), round(pn1.y1 + 64 // 2), 6, (255, 255, 255)))

    # plane2
    keys1 = pygame.key.get_pressed()
    if keys1[pygame.K_a] and pn2.x2 > pn2.vel2:
        pn2.x2 -= pn2.vel2
    if keys1[pygame.K_d] and pn2.x2 < 600 - pn2.vel2 - 62:
        pn2.x2 += pn2.vel2
    if keys1[pygame.K_g]:
        if len(bullets1) < 10:
            bullets1.append(
                projectile(round(pn2.x2 + 40 // 2), round(pn2.y2 + 64 // 2), 6, (0, 255, 255)))

    gamewin()
pygame.quit()
