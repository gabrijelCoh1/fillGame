import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("epic game")
#BG = pygame.transform.scale(pygame.image.load("pygamepic.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 5

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('move with arrow keys!! fill everything!!', True, "white")
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2)

def draw(player):
    WIN.blit(text, textRect)
    #WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "orange", player)
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) #x, y, width, height  - screen height minus player height = top left corner

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >= 0:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
            player.y += PLAYER_VELOCITY

        draw(player) 

    pygame.quit()



if __name__ == "__main__":
    main()