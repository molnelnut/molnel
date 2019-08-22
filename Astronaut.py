from tot.Spacecraft import Spacecraft

if __name__ == '__main__':
    modon = Spacecraft('modon', 10000, 423)
    goldern = Spacecraft('goldern', 15000, 342)
    modon.attack(goldern,modon)
    goldern.attack(modon,goldern)
    print(goldern)
    print(modon)
