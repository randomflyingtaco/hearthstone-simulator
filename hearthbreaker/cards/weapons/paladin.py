from hearthbreaker.tags.action import Give, DecreaseDurability, Heal
from hearthbreaker.tags.event import MinionSummoned, Attack
from hearthbreaker.tags.selector import TargetSelector, HeroSelector, MinionSelector, RandomPicker
from hearthbreaker.tags.base import Buff, Effect, Battlecry
from hearthbreaker.tags.status import DivineShield, Taunt, ChangeAttack, ChangeHealth
from hearthbreaker.constants import CHARACTER_CLASS, CARD_RARITY
from hearthbreaker.game_objects import WeaponCard, Weapon


class LightsJustice(WeaponCard):
    def __init__(self):
        super().__init__("Light's Justice", 1, CHARACTER_CLASS.PALADIN, CARD_RARITY.FREE)

    def create_weapon(self, player):
        return Weapon(1, 4)


class SwordOfJustice(WeaponCard):
    def __init__(self):
        super().__init__("Sword of Justice", 3, CHARACTER_CLASS.PALADIN, CARD_RARITY.EPIC)

    def create_weapon(self, player):
        return Weapon(1, 5, effects=[Effect(MinionSummoned(), Give([Buff(ChangeAttack(1)), Buff(ChangeHealth(1))]),
                                            TargetSelector()),
                                     Effect(MinionSummoned(), DecreaseDurability(), HeroSelector())])


class TruesilverChampion(WeaponCard):
    def __init__(self):
        super().__init__("Truesilver Champion", 4, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON)

    def create_weapon(self, player):
        return Weapon(4, 2, effects=[Effect(Attack(), Heal(2), HeroSelector())])


class Coghammer(WeaponCard):
    def __init__(self):
        super().__init__("Coghammer", 3, CHARACTER_CLASS.PALADIN, CARD_RARITY.EPIC,
                         battlecry=Battlecry(Give([Buff(DivineShield()), Buff(Taunt())]),
                                             MinionSelector(picker=RandomPicker())))

    def create_weapon(self, player):
        return Weapon(2, 3)
