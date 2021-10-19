import random

def get_hero_traits(filepath):
    heroes_dict = {}
    try:
        file = open(filepath, "r")

    except FileNotFoundError:
        print("ERROR: FILE {} NOT FOUND.".format(filepath))


    else:
        for line in file:
            traits_dict = {}

            line = line.strip().split(",")


            hero = line[0]
            heroes_dict[str(hero)] = ""
            weapon = line[1].split(":")
            strength = line[2].split(":")
            health = line[3].split(":")

            traits_dict["weapon"] = weapon[1]
            traits_dict["strength"] = int(strength[1])
            traits_dict["health"] = int(health[1])


            heroes_dict[str(hero)] = traits_dict








        file.close()


    finally:
        return heroes_dict


def battle(hero_traits, hero1, hero2):
    print("{} using {} is battling {} using {}".format(hero1, hero_traits[hero1]["weapon"], hero2, hero_traits[hero2]["weapon"]))

    rare_chance = random.randrange(1,101)

    if rare_chance == 1:

         if hero_traits[hero1]["weapon"] < hero_traits[hero2]["weapon"]:
             print("{} wins!".format(hero1))

         elif hero_traits[hero2]["weapon"] < hero_traits[hero1]["weapon"]:
             print("{} wins!".format(hero2))
    else:
        if hero_traits[hero1]["weapon"] < hero_traits[hero2]["weapon"]:
          print("{} wins!".format(hero2))

        else:
            print("{} wins!".format(hero1))





def main():
    get_hero_traits("heroes.csv")




if __name__ == '__main__':
    main()
