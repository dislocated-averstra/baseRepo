import random

import yaml

f = open('../../Main/Resources/game_data.yml', 'r')
result = yaml.full_load(f)
samples = random.sample(list(result), 3)
for sample in samples:
    team = result.get(sample)
    for member in team:
        member_name = list(member.keys())[0]
        member_dict = member.get(member_name)
        print(member_dict.get('location'))
print("end of experiment")
