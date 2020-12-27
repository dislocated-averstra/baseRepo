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

    first_test_sprite = SpaceMarine('SpriteImages/chaplain_raziel.png')
    second_test_sprite = SpaceMarine('SpriteImages/brother_metraen.png')
    third_test_sprite = SpaceMarine('SpriteImages/brother_zael.png')
    forth_test_sprite = SpaceMarine('SpriteImages/brother_omnio.png')
    background = DISPLAYSURF.copy()
    background.fill(BLACK)

    while True:
        DISPLAYSURF.blit(background, (0, 0))
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (394, 50, 250, 485), 5)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, background)

        # update all the sprites
        render_update_group.update()

        first_test_sprite.move(400, 52)
        second_test_sprite.move(400, 172)
        third_test_sprite.move(400, 292)
        forth_test_sprite.move(400, 412)
        dirty = render_update_group.draw(DISPLAYSURF)
        pygame.display.update(dirty)
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
