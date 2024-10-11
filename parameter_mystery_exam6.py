def clue(suspect, room, weapon):
    print(room, "in the", weapon, "with the", suspect)
    return room                

def main():
    scarlett = "mustard"
    suspect = "peacock"
    lounge = "ballroom"
    pipe = "study"
    dagger = "pipe"
    weapon = "dagger"

    clue(weapon, suspect, pipe)
    clue(scarlett, pipe, suspect)
    dagger = clue(dagger, "lounge", scarlett)
    clue(dagger, lounge, "dagger")

main()
