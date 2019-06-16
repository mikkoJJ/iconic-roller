""" "Data objects" for the Iconic Roller
"""


class IconRelationship(object):
    """ Object representing a relationship to a single icon.
    """

    def __init__(self, icon: str, type: str):
        """ Initialise a new relationship to the given value.

        :param icon:
            Icon that is the "target" of the relationship
        :param type:
            Type of the relationship
        """
        self.icon = icon
        self.type = type
        self.points = 1

    def __str__(self):
        """
        :return:
            String representation of this relationship. Eg::
                "2 point positive relationship with The Archmage"
        """
        return f"{self.points} point {self.type} relationship with {self.icon}"
