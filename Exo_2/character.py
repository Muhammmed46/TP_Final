import logging
import random
log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""
                        


class Character:
    """Class to represent a basic character"""
    def __init__(self, name: str) -> None:
        self._name = name
        self._life = 100
        self._attack = 20
        self._defense = 0.1
    
    def take_damages(self, damage_value: float):
        """Take damages"""
        self._life -= damage_value * (1 - self._defense)
        if self._life < 0:
            self._life = 0
        return None

    def attack(self, target: "Character"):
        """Attack another character"""
        damage_value = self._attack
        target.take_damages(damage_value)
        return None

    def __str__(self) -> str:
        """String representation of the character"""
        return f"{self.name} (hp : {self._life:.2f})"
    
    @property
    def name(self) -> str:
        """"Get name"""
        return self._name

    @property
    def is_dead(self) -> bool:
        """Check if character is dead"""
        if self._life <=0 :
            return  True
        return False
    
class Weapon:
    """Class to represent a weapon"""
    def __init__(self, name: str, attack: float) -> None:
        self._name = name   # ← underscore !
        self._attack = attack
    
    def __str__(self) -> str:
        """String representation of the weapon"""
        return f"{self.name} (attack : {self.attack})"

    @property
    def name(self) -> str:
        """Get name"""
        return self._name   # ← pas self.name, mais self._name (évite boucle infinie)

    @property
    def attack(self) -> float:
        """Get attack value"""
        return self._attack

    @classmethod
    def default(cls) -> "Weapon":
        """Get default weapon"""
        return cls("Wood stick", 1.0)


class Warrior(Character):
    """Create a warrior"""
    def __init__(self, name: str, weapon: Weapon = Weapon.default()) -> None:
        super().__init__(name)
        self._life = self._life * 1.5
        self._defense = self._defense * 1.2
        self._weapon = weapon
        self._attack += weapon.attack

    def is_raging(self):
        """Check if the warrior is raging"""
        if self._life < 30:
            self._attack *= 1.2
            return True
        return False


class Magician(Character):
    """Create a magician"""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._life = self._life * 0.8
        self._attack = self._attack * 2

    def activate_magic_shield(self) -> bool:
        """Activate magic shield"""
        if random.randint(1, 3) == 3:
            return True
        return False
    
    def take_damages(self, damage_value):
        """Take damages"""
        if self.activate_magic_shield():#if magic shield is activated
            return None #no damage taken
        #if magic shield is not activated, take damage
        return super().take_damages(damage_value)
