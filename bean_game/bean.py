import pygame
pygame.init()

windowWidth = 800
windowHeight = 480
window = pygame.display.set_mode((windowWidth, windowHeight))
walkRight = [pygame.image.load('images/R1.png'),
             pygame.image.load('images/R2.png'),
             pygame.image.load('images/r4.png'),
             pygame.image.load('images/r5.png'),
            pygame.image.load('images/r6.png'),
            pygame.image.load('images/r7.png'),
            pygame.image.load('images/r8.png'),
            pygame.image.load('images/r9.png')]

walkLeft = [pygame.image.load('images/L1.png'),
            pygame.image.load('images/L2.png'),
            pygame.image.load('images/L3.png'),
            pygame.image.load('images/L4.png'),
            pygame.image.load('images/L5.png'),
            pygame.image.load('images/L6.png'),
            pygame.image.load('images/L7.png'),
            pygame.image.load('images/L8.png'),
            pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')
x = 50
y = 420
width = 64
height = 64
velocity = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

run = True

def redrawWin():
    global walkCount
    window.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        window.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        window.blit(char, (x, y))
    pygame.display.update()
    
def movement():
    global x, y,width,height,isJump,jumpCount, left, right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        left = True
        right = False
        x -= velocity
    elif keys[pygame.K_RIGHT] and x < windowWidth - width - velocity:
        right = True
        left = False
        x += velocity
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0 
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2)*0.5*neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
def events():
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
while run == True:
    pygame.time.delay(50)
    events()
    movement()
    redrawWin()



