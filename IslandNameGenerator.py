import random

#Lists made during a stream on Twitch with my beloved viewers : Ayu and DTMark
nouns = ["Murkwood", "Treasure", "Death", "Lizard", "Magic", "Wonders", "Devil", "Seagulls", "Bounty", "Last wish", "Powder" ]
descriptors = ["Bay", "Rock", "Isle", "Enclave", "Atoll", "Cove", "Cay", "Shallow", "Lagoon", "Island", "Harbour"]
adjectives = ["Golden", "Dark", "Green", "Black", "Bloody", "Wild", "Forgotten", "Lost" ]


def generateName():
    #3 simples grammars
    if len(nouns) == 0 :
        return ""
    noun = random.sample(nouns, 1)[0]
    nouns.remove(noun)
    descriptor = random.sample(descriptors, 1)[0]
    rand = random.randrange(0, 3)
    if rand == 0:
        return (noun + " " + descriptor)
    if rand == 1:
        return (descriptor + " of the " + noun)
    if rand == 2:
        return (noun + "'s " + descriptor)
    if rand == 3:
        nouns.append(noun)
        adj = random.sample(adjectives, 1)[0]
        adjectives.remove(adj)
        return (adj + " " + descriptor)
