class Pokemon:
    def __init__(self, name: str, max_armor: int, max_hit: int):
        self.name = name
        self.armor = max_armor
        self.hit_points = max_hit
        self._ischarging = False

    def attack(self):
        print(f"{self.name} attacks")

    def defend(self):
        print(f"{self.name} defends itself")

#    def _change_attack(self):
#        print(f"{self.name} is changing attack type")

class ElectricPokemon(Pokemon):
    def wild_charge(self):
        print("Wild charge attack!")

class WaterPokemon(Pokemon):
    def __init__(self, name: str, max_armor: int, max_hit: int, speed: int):
        Pokemon.__init__(self, name, max_armor, max_hit)
        self.speed = speed
    def attack(self):
        print(f"{self.name} Special attack!")
    def aqua_tail(self):
        print("Aqua tail attack")

class FlyingPokemon(Pokemon):
    def dragon_ascent(self):
        print("Dragon ascent attack")

pikachu = ElectricPokemon("Pikachu", 100, 1000)
pikachu.attack()
pikachu.attack()
pikachu.defend()
pikachu.wild_charge() 
#pikachu._change_attack()

snorlax = Pokemon("Snorlax", 75, 900)
snorlax.attack()

charmander = Pokemon("Charmander", 1200, 600)
charmander.defend()

vaporeon = WaterPokemon("Vaporeon", 99, 1000, 20)
vaporeon.attack()

pokemons = (pikachu, snorlax, charmander, vaporeon)

for pokemon in pokemons:
    pokemon.attack() 