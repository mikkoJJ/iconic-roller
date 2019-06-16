""" Functions for randomly rolling the relationships.
"""
from .defaults import ICONS, RELATIONSHIP_TYPES
from .icon_relationships import IconRelationship

import random
from typing import List


def roll_relationships(relationship_points: int, min_icons: int) -> List[IconRelationship]:
    """

    :param relationship_points:
        How many points are spent to relationship.
    :param min_icons:
        Minimum number of different icons to have a relationship to.
    :return:
        A list of icon relationship objects representing the rolled relationships.
    """
    relationships = []

    for i in range(0, relationship_points):
        if len(relationships) < min_icons or random.randint(0, 1) == 0:
            relationships.append(roll_new_icon())
        else:
            add_to_relationships(relationships)

    return relationships


def roll_new_icon() -> IconRelationship:
    icon = random.choice(ICONS)
    ICONS.remove(icon)

    relation_type = random.choice(RELATIONSHIP_TYPES)

    relationship = IconRelationship(icon, relation_type)

    return relationship


def add_to_relationships(relationships: list):
    random.choice(relationships).points += 1
