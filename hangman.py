import pygame

def draw():
    window.fill(background_colour)

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter

        if visible:
            pygame.draw.circle(window, button_colour, (x,y), RADIUS, 3)
            text = letter_font.render(ltr, 1, button_colour)
            window.blit(text, (x-text.get_width()/2, y-text.get_width()/2))

    window.blit(imgs[hangman_status], (400, 250))
    pygame.display.update()


# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

background_colour = (0,0,0)
button_colour = (255,255,255)
letter_font = pygame.font.SysFont('comicsans', 40)

RADIUS, GAP = 20, 15
letters = []
x_start = round((WIDTH-(RADIUS*2+GAP)*13)/2)
y_start = 400
A = 65
for r in range(26):
    x = x_start + GAP*2 + ((RADIUS*2+GAP)*(r%13))
    y = y_start + ((r//13)*(GAP+RADIUS*2))
    letters.append([x, y, chr(A + r), True])



# load hangman status images
imgs = []
for i in range(7):
    img = pygame.image.load("hangman" + str(i) + ".png")
    imgs.append(img)


# game variables
hangman_status = 0


# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter

                if visible:
                    dis = math.sqrt((x-x_mouse)**2 + (y-y_mouse)**2)
                    if dis < RADIUS:
                        letter[3] = False
        

pygame.quit()