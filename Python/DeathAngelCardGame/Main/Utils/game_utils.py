import random

import yaml

from Python.DeathAngelCardGame.Main.Emuns.facing_emun import Facing
from Python.DeathAngelCardGame.Main.GameObjects.space_marine import SpaceMarine


def init_game():
    space_marines = []
    # open the game data and read it to a file
    f = open('Main/Resources/game_data.yml', 'r')
    result = yaml.full_load(f)
    # from the data pick three teams at random
    samples = random.sample(list(result), 3)
    for sample in samples:
        team = result.get(sample)
        for member in team:
            member_name = list(member.keys())[0]
            member_dict = member.get(member_name)
            space_marines.append(SpaceMarine(member_dict.get('location')))
    random.shuffle(space_marines)
    for i in range(1, len(space_marines)):
        if i >= 3:
            space_marines[i].set_facing(Facing.RIGHT)
    return space_marines


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()
