import random

def print_bold(msg, end='\n'):
    print("\033" + msg + "\033", end=end)


def weighted_random_selection(obj1, obj2):
    """Randomly select between two objects based on assigned 'weight'

    .. todo:: How about creating a utility module for common functionality?
    """
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2


class GameUnit:
    """A base class for creating various game characters"""
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    def info(self):
        """Information on the unit (overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of injury

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end='  ')
        enemy.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            # TODO: Do you see a bug here? it can exceed max hit points!
            self.health_meter += heal_by

        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        # TODO: what if there is no enemy?
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
