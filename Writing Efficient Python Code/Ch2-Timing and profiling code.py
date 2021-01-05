#Chapter 2 - Timing and profiling code

#Using %timeit: your turn!
# Create a list of integers (0-50) using list comprehension
import timeit as timeit
import numpy as np

nums_list_comp = [num for num in range(51)]
print(nums_list_comp)
# Create a list of integers (0-50) by unpacking range
nums_unpack = [*(nums_list_comp)]
print(nums_unpack)

print("=========================================================")


#Using %timeit: specifying number of runs and loops
#############################
#  run code in the console  #
#############################
heroes = ['A-Bomb', 'Abe Sapien', 'Abin Sur', 'Abomination', 'Absorbing Man', 'Adam Strange', 'Agent 13', 'Agent Bob', 'Agent Zero', 'Air-Walker', 'Ajax', 'Alan Scott', 'Alfred Pennyworth', 'Alien', 'Amazo', 'Ammo', 'Angel', 'Angel Dust', 'Angel Salvadore', 'Animal Man', 'Annihilus', 'Ant-Man', 'Ant-Man II', 'Anti-Venom', 'Apocalypse', 'Aqualad', 'Aquaman', 'Arachne', 'Archangel', 'Arclight', 'Ardina', 'Ares', 'Ariel', 'Armor', 'Atlas', 'Atom', 'Atom Girl', 'Atom II', 'Aurora', 'Azazel', 'Bane', 'Banshee', 'Bantam', 'Batgirl', 'Batgirl IV', 'Batgirl VI', 'Batman', 'Batman II', 'Battlestar', 'Beak', 'Beast', 'Beast Boy', 'Beta Ray Bill', 'Big Barda', 'Big Man', 'Binary', 'Bishop', 'Bizarro', 'Black Adam', 'Black Bolt', 'Black Canary', 'Black Cat', 'Black Knight III', 'Black Lightning', 'Black Mamba', 'Black Manta', 'Black Panther', 'Black Widow', 'Black Widow II', 'Blackout', 'Blackwing', 'Blackwulf', 'Blade', 'Bling!', 'Blink', 'Blizzard II', 'Blob', 'Bloodaxe', 'Blue Beetle II', 'Boom-Boom', 'Booster Gold', 'Box III', 'Brainiac', 'Brainiac 5', 'Brother Voodoo', 'Buffy', 'Bullseye', 'Bumblebee', 'Cable', 'Callisto', 'Cannonball', 'Captain America', 'Captain Atom', 'Captain Britain', 'Captain Mar-vell', 'Captain Marvel', 'Captain Marvel II', 'Carnage', 'Cat', 'Catwoman', 'Cecilia Reyes', 'Century', 'Chamber', 'Changeling', 'Cheetah', 'Cheetah II', 'Cheetah III', 'Chromos', 'Citizen Steel', 'Cloak', 'Clock King', 'Colossus', 'Copycat', 'Corsair', 'Cottonmouth', 'Crimson Dynamo', 'Crystal', 'Cyborg', 'Cyclops', 'Cypher', 'Dagger', 'Daredevil', 'Darkhawk', 'Darkseid', 'Darkstar', 'Darth Vader', 'Dash', 'Dazzler', 'Deadman', 'Deadpool', 'Deadshot', 'Deathlok', 'Deathstroke', 'Demogoblin', 'Destroyer', 'Diamondback', 'Doc Samson', 'Doctor Doom', 'Doctor Doom II', 'Doctor Fate', 'Doctor Octopus', 'Doctor Strange', 'Domino', 'Donna Troy', 'Doomsday', 'Doppelganger', 'Drax the Destroyer', 'Elastigirl', 'Electro', 'Elektra', 'Elongated Man', 'Emma Frost', 'Enchantress', 'Etrigan', 'Evil Deadpool', 'Evilhawk', 'Exodus', 'Fabian Cortez', 'Falcon', 'Feral', 'Fin Fang Foom', 'Firebird', 'Firelord', 'Firestar', 'Firestorm', 'Flash', 'Flash II', 'Flash III', 'Flash IV', 'Forge', 'Franklin Richards', 'Franklin Storm', 'Frenzy', 'Frigga', 'Galactus', 'Gambit', 'Gamora', 'Genesis', 'Ghost Rider', 'Giganta', 'Gladiator', 'Goblin Queen', 'Goku', 'Goliath IV', 'Gorilla Grodd', 'Granny Goodness', 'Gravity', 'Green Arrow', 'Green Goblin', 'Green Goblin II', 'Green Goblin III', 'Green Goblin IV', 'Groot', 'Guy Gardner', 'Hal Jordan', 'Han Solo', 'Harley Quinn', 'Havok', 'Hawk', 'Hawkeye', 'Hawkeye II', 'Hawkgirl', 'Hawkman', 'Hawkwoman', 'Hawkwoman III', 'Heat Wave', 'Hela', 'Hellboy', 'Hellcat', 'Hellstorm', 'Hercules', 'Hobgoblin', 'Hope Summers', 'Howard the Duck', 'Hulk', 'Human Torch', 'Huntress', 'Husk', 'Hybrid', 'Hydro-Man', 'Hyperion', 'Iceman', 'Impulse', 'Ink', 'Invisible Woman', 'Iron Fist', 'Iron Man', 'Jack of Hearts', 'Jack-Jack', 'James T. Kirk', 'Jean Grey', 'Jennifer Kale', 'Jessica Jones', 'Jigsaw', 'John Stewart', 'John Wraith', 'Joker', 'Jolt', 'Jubilee', 'Juggernaut', 'Justice', 'Kang', 'Karate Kid', 'Killer Croc', 'Kilowog', 'Kingpin', 'Klaw', 'Kraven II', 'Kraven the Hunter', 'Krypto', 'Kyle Rayner', 'Lady Deathstrike', 'Leader', 'Legion', 'Lex Luthor', 'Light Lass', 'Lightning Lad', 'Lightning Lord', 'Living Brain', 'Lizard', 'Lobo', 'Loki', 'Longshot', 'Luke Cage', 'Luke Skywalker', 'Mach-IV', 'Machine Man', 'Magneto', 'Man-Thing', 'Man-Wolf', 'Mandarin', 'Mantis', 'Martian Manhunter', 'Marvel Girl', 'Master Brood', 'Maverick', 'Maxima', 'Medusa', 'Meltdown', 'Mephisto', 'Mera', 'Metallo', 'Metamorpho', 'Metron', 'Micro Lad', 'Mimic', 'Miss Martian', 'Mister Fantastic', 'Mister Freeze', 'Mister Sinister', 'Mockingbird', 'MODOK', 'Molten Man', 'Monarch', 'Moon Knight', 'Moonstone', 'Morlun', 'Morph', 'Moses Magnum', 'Mr Immortal', 'Mr Incredible', 'Ms Marvel II', 'Multiple Man', 'Mysterio', 'Mystique', 'Namor', 'Namora', 'Namorita', 'Naruto Uzumaki', 'Nebula', 'Nick Fury', 'Nightcrawler', 'Nightwing', 'Northstar', 'Nova', 'Odin', 'Omega Red', 'Omniscient', 'One Punch Man', 'Onslaught', 'Oracle', 'Paul Blart', 'Penance II', 'Penguin', 'Phantom Girl', 'Phoenix', 'Plantman', 'Plastic Man', 'Plastique', 'Poison Ivy', 'Polaris', 'Power Girl', 'Predator', 'Professor X', 'Professor Zoom', 'Psylocke', 'Punisher', 'Purple Man', 'Pyro', 'Question', 'Quicksilver', 'Quill', "Ra's Al Ghul", 'Raven', 'Ray', 'Razor-Fist II', 'Red Arrow', 'Red Hood', 'Red Hulk', 'Red Robin', 'Red Skull', 'Red Tornado', 'Rhino', 'Rick Flag', 'Ripcord', 'Robin', 'Robin II', 'Robin III', 'Robin V', 'Rocket Raccoon', 'Rogue', 'Ronin', 'Rorschach', 'Sabretooth', 'Sage', 'Sandman', 'Sasquatch', 'Scarecrow', 'Scarlet Spider', 'Scarlet Spider II', 'Scarlet Witch', 'Scorpion', 'Sentry', 'Shadow King', 'Shadow Lass', 'Shadowcat', 'Shang-Chi', 'Shatterstar', 'She-Hulk', 'She-Thing', 'Shocker', 'Shriek', 'Sif', 'Silver Surfer', 'Silverclaw', 'Sinestro', 'Siren', 'Siryn', 'Skaar', 'Snowbird', 'Solomon Grundy', 'Songbird', 'Space Ghost', 'Spawn', 'Spider-Girl', 'Spider-Gwen', 'Spider-Man', 'Spider-Woman', 'Spider-Woman III', 'Spider-Woman IV', 'Spock', 'Spyke', 'Star-Lord', 'Starfire', 'Stargirl', 'Static', 'Steel', 'Steppenwolf', 'Storm', 'Sunspot', 'Superboy', 'Superboy-Prime', 'Supergirl', 'Superman', 'Swarm', 'Synch', 'T-1000', 'Taskmaster', 'Tempest', 'Thanos', 'The Comedian', 'Thing', 'Thor', 'Thor Girl', 'Thunderbird', 'Thunderbird III', 'Thunderstrike', 'Thundra', 'Tiger Shark', 'Tigra', 'Tinkerer', 'Toad', 'Toxin', 'Trickster', 'Triplicate Girl', 'Triton', 'Two-Face', 'Ultragirl', 'Ultron', 'Utgard-Loki', 'Vagabond', 'Valerie Hart', 'Valkyrie', 'Vanisher', 'Vegeta', 'Venom', 'Venom II', 'Venom III', 'Vertigo II', 'Vibe', 'Vindicator', 'Violet Parr', 'Vision', 'Vision II', 'Vixen', 'Vulture', 'Walrus', 'War Machine', 'Warbird', 'Warlock', 'Warp', 'Warpath', 'Wasp', 'White Queen', 'Winter Soldier', 'Wiz Kid', 'Wolfsbane', 'Wolverine', 'Wonder Girl', 'Wonder Man', 'Wonder Woman', 'Wyatt Wingfoot', 'X-23', 'X-Man', 'Yellow Claw', 'Yellowjacket', 'Yellowjacket II', 'Yoda', 'Zatanna', 'Zoom']

# %timeit -r5 -n25 set(heroes)
print("=========================================================")


#Using %timeit: formal name or literal syntax
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))
print("=========================================================")


#Using cell magic mode (%%timeit)
#############################
#  run code in the console  #
#############################
wts = [441.0, 65.0, 90.0, 441.0, 122.0, 88.0, 61.0, 81.0, 104.0, 108.0, 90.0, 90.0, 72.0, 169.0, 173.0, 101.0, 68.0, 57.0, 54.0, 83.0, 90.0, 122.0, 86.0, 358.0, 135.0, 106.0, 146.0, 63.0, 68.0, 57.0, 98.0, 270.0, 59.0, 50.0, 101.0, 68.0, 54.0, 81.0, 63.0, 67.0, 180.0, 77.0, 54.0, 57.0, 52.0, 61.0, 95.0, 79.0, 133.0, 63.0, 181.0, 68.0, 216.0, 135.0, 71.0, 54.0, 124.0, 155.0, 113.0, 95.0, 58.0, 54.0, 86.0, 90.0, 52.0, 92.0, 90.0, 59.0, 61.0, 104.0, 86.0, 88.0, 97.0, 68.0, 56.0, 77.0, 230.0, 495.0, 86.0, 55.0, 97.0, 110.0, 135.0, 61.0, 99.0, 52.0, 90.0, 59.0, 158.0, 74.0, 81.0, 108.0, 90.0, 116.0, 108.0, 74.0, 74.0, 86.0, 61.0, 61.0, 62.0, 97.0, 63.0, 81.0, 50.0, 55.0, 54.0, 86.0, 170.0, 70.0, 78.0, 225.0, 67.0, 79.0, 99.0, 104.0, 50.0, 173.0, 88.0, 68.0, 52.0, 90.0, 81.0, 817.0, 56.0, 135.0, 27.0, 52.0, 90.0, 95.0, 91.0, 178.0, 101.0, 95.0, 383.0, 90.0, 171.0, 187.0, 132.0, 89.0, 110.0, 81.0, 54.0, 63.0, 412.0, 104.0, 306.0, 56.0, 74.0, 59.0, 80.0, 65.0, 57.0, 203.0, 95.0, 106.0, 88.0, 96.0, 108.0, 50.0, 18.0, 56.0, 99.0, 56.0, 91.0, 81.0, 88.0, 86.0, 52.0, 81.0, 45.0, 92.0, 104.0, 167.0, 16.0, 81.0, 77.0, 86.0, 99.0, 630.0, 268.0, 50.0, 62.0, 90.0, 270.0, 115.0, 79.0, 88.0, 83.0, 77.0, 88.0, 79.0, 4.0, 95.0, 90.0, 79.0, 63.0, 79.0, 89.0, 104.0, 57.0, 61.0, 88.0, 54.0, 65.0, 81.0, 225.0, 158.0, 61.0, 81.0, 146.0, 83.0, 48.0, 18.0, 630.0, 77.0, 59.0, 58.0, 77.0, 119.0, 207.0, 65.0, 65.0, 81.0, 54.0, 79.0, 191.0, 79.0, 14.0, 77.0, 52.0, 55.0, 56.0, 113.0, 90.0, 88.0, 86.0, 49.0, 52.0, 855.0, 81.0, 104.0, 72.0, 356.0, 324.0, 203.0, 97.0, 99.0, 106.0, 18.0, 79.0, 58.0, 63.0, 59.0, 95.0, 54.0, 65.0, 95.0, 360.0, 230.0, 288.0, 236.0, 36.0, 191.0, 77.0, 79.0, 383.0, 86.0, 225.0, 90.0, 97.0, 52.0, 135.0, 56.0, 81.0, 110.0, 72.0, 59.0, 54.0, 140.0, 72.0, 90.0, 90.0, 86.0, 77.0, 101.0, 61.0, 81.0, 86.0, 128.0, 61.0, 338.0, 248.0, 90.0, 101.0, 59.0, 79.0, 79.0, 72.0, 70.0, 158.0, 61.0, 70.0, 79.0, 54.0, 125.0, 85.0, 101.0, 54.0, 83.0, 99.0, 88.0, 79.0, 83.0, 86.0, 293.0, 191.0, 65.0, 69.0, 405.0, 59.0, 117.0, 89.0, 79.0, 54.0, 52.0, 87.0, 80.0, 55.0, 50.0, 52.0, 81.0, 234.0, 86.0, 81.0, 70.0, 90.0, 74.0, 68.0, 83.0, 79.0, 56.0, 97.0, 50.0, 70.0, 117.0, 83.0, 81.0, 630.0, 56.0, 108.0, 146.0, 320.0, 85.0, 72.0, 79.0, 101.0, 56.0, 38.0, 25.0, 54.0, 104.0, 63.0, 171.0, 61.0, 203.0, 900.0, 63.0, 74.0, 113.0, 59.0, 310.0, 87.0, 149.0, 54.0, 50.0, 79.0, 88.0, 315.0, 153.0, 79.0, 52.0, 191.0, 101.0, 50.0, 92.0, 72.0, 52.0, 180.0, 49.0, 437.0, 65.0, 113.0, 405.0, 54.0, 56.0, 74.0, 59.0, 55.0, 58.0, 81.0, 83.0, 79.0, 71.0, 62.0, 63.0, 131.0, 91.0, 57.0, 77.0, 68.0, 77.0, 54.0, 101.0, 47.0, 74.0, 146.0, 99.0, 54.0, 443.0, 101.0, 225.0, 288.0, 143.0, 101.0, 74.0, 288.0, 158.0, 203.0, 81.0, 54.0, 76.0, 97.0, 81.0, 59.0, 86.0, 82.0, 105.0, 331.0, 58.0, 54.0, 56.0, 214.0, 79.0, 73.0, 117.0, 50.0, 334.0, 52.0, 71.0, 54.0, 41.0, 135.0, 135.0, 63.0, 79.0, 162.0, 95.0, 54.0, 108.0, 67.0, 158.0, 50.0, 65.0, 117.0, 39.0, 473.0, 135.0, 51.0, 171.0, 74.0, 117.0, 50.0, 61.0, 95.0, 83.0, 52.0, 17.0, 57.0, 81.0]
hero_wts_lbs = []
# %%timeit
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)


# %%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
print("=========================================================")


#Using %lprun: spot bottlenecks
#############################
#  run code in the console  #
#############################
# %load_ext line_profiler
# %lprun -f convert_units convert_units(heroes, hts, wts)
print("=========================================================")


#Using %lprun: fix the bottleneck
#############################
#  run code in the console  #
#############################
# %load_ext line_profiler
# %lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)
print("=========================================================")


#Using %mprun: Hero BMI
#############################
#  run code in the console  #
#############################
# from bmi_lists import calc_bmi_lists
# %load_ext line_profiler
# %lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)
print("=========================================================")


#Using %mprun: Hero BMI
#############################
#  run code in the console  #
#############################
# from bmi_arrays import calc_bmi_arrays
# %load_ext memory_profiler
# %mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)
print("=========================================================")


#Bringing it all together: Star Wars profiling
# Use get_publisher_heroes() to gather Star Wars heroes
# star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')
#
# print(star_wars_heroes)
# print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
# star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

# print(star_wars_heroes_np)
# print(type(star_wars_heroes_np))
print("=========================================================")

#############################
#  run code in the console  #
#############################
# %load_ext line_profiler
# %lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
# %lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

#############################
#  run code in the console  #
#############################
# from hero_funcs import get_publisher_heroes
# from hero_funcs  import get_publisher_heroes_np
# %load_ext memory_profiler
# %mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
# %mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')