from gameutils import print_bold

class Hut:
    """Class to create hut objects in the game Attack of the Orcs

    :arg int number: Hut number to be assigned
    :arg AbstractGameUnit occupant: The new occupant of the Hut

    :ivar int number: A number assigned to this hut
    :ivar boolean is_acquired: A boolean flag to indicate if the
                   hut is acquired. In the current implementation
                   this is viewed from the player's perspective.
    :ivar AbstractGameUnit occupant: The occupant of this hut.
                   Needs to be an instance of the subclass of
                  `AbstractGameUnit`.

    .. seealso:: Where it is used --
            :py:meth:`attackoftheorcs.AttackOfTheOrcs.setup_game_scenario`
    """

    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """Update the occupant of this hut"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("GOOD JOB! Hut %d acquired" % self.number)

    def get_occupant_type(self):
        """Return a string giving info on the hut occupant"""
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type
