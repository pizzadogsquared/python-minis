def carbonated(coke, soda, pop):
    print("say", soda, "not", pop, "or", coke)

def main():
    soda = "coke"
    pop = "pepsi"
    coke = "pop"
    pepsi = "soda"
    say = pop

    carbonated(coke, soda, pop)
    carbonated(pop, pepsi, pepsi)
    carbonated("pop", pop, "koolaid")
    carbonated(say, "say", pop)

main()
