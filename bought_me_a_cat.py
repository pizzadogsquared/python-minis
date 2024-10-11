def main():
    bought("cat")
    print(cat)
    bought("hen")
    to_add = hen + cat
    print(to_add)
    bought("duck")
    to_add = duck + to_add
    print(to_add)
    bought("goose")
    to_add = goose + to_add
    print(to_add)
    bought("sheep")
    to_add = sheep + to_add
    print(to_add)
    bought("pig")
    to_add = pig + to_add
    print(to_add)


cat = "Cat goes fiddle-i-fee.\n"

hen = "Hen goes chimmy-chuck, chimmy-chuck,\n"

duck = "Duck goes quack, quack,\n"

goose = "Goose goes hissy, hissy,\n"

sheep = "Sheep goes baa, baa,\n"

pig = "Pig goes oink, oink,\n"
    
def bought(animal):
    print("Bought me a", animal, "and the", animal, "pleased me,")
    print("I fed my", animal, "under yonder tree.")

main()
