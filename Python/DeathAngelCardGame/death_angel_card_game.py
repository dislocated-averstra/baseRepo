import pygame

from GameObjects.space_marine import SpaceMarine

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 60

BLACK = (0, 0, 0)
BLUE = (0, 0, 155)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
def main():
    global FPSCLOCK, DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Death Angel')
    run_game()

def run_game():

    render_update_group = pygame.sprite.RenderUpdates()
    SpaceMarine.containers = render_update_group

    first_test_sprite = SpaceMarine("SpriteImages/chaplain_raziel.png")
    background = DISPLAYSURF.copy()
    background.fill(BLACK)

    while True:

        DISPLAYSURF.blit(background, (0, 0))
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (20, 20, 500, 740), 5)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, background)

        # update all the sprites
        render_update_group.update()

        dirty = render_update_group.draw(DISPLAYSURF)
        pygame.display.update(dirty)
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()