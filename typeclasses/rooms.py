"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia.objects.objects import DefaultRoom

from .objects import ObjectParent


class Room(ObjectParent, DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """




    # TODO: Refactor at_object_receive and at_objecte leave
    def at_object_receive(self, moved_obj, source_location, move_type="move", **kwargs):
        characters = [character for character in self.contents if character.typename == "Character"]

        if len(characters) > 0:
            room = self
            room_data = {
                "dbref": room.id,
                "name": room.name,
                "desc": room.db.desc,
                "contents":  list(set(room.contents) - set(room.exits) - set(room.contents_get(content_type="character"))),
                "characters": list(set(room.contents_get(content_type="character"))),
                "exits": room.exits,
            }

            for char in characters:
                char.msg(room_data=room_data)
    pass

    def at_object_leave(self, moved_obj, source_location, move_type="move", **kwargs):
        characters = [character for character in self.contents if character.typename == "Character"]
        print(moved_obj)
        if len(characters) > 0:
            room = self
            room_data = {
                "dbref": room.id,
                "name": room.name,
                "desc": room.db.desc,
                "contents":  list(set(room.contents) - set([moved_obj]) - set(room.exits) - set(room.contents_get(content_type="character"))),
                "characters": list(set(room.contents_get(content_type="character")) - set([moved_obj])),
                "exits": room.exits,
            }

            for char in characters:
                char.msg(room_data=room_data)
    pass
