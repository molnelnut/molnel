class Spacecraft():

    def __init__(self,name,hp,atk) -> None:
        super().__init__()
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, enemy, me):
        self.enemy = enemy
        self.me = me
        self.enemy.hp =self.enemy.hp-self.me.atk

    def __str__(self) -> str:
        return '{} attack enemy enemy is damaged {} Ememy HP is {}'.format(self.name,self.atk,self.enemy.hp)