"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_post_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_look(self, target, **kwargs):
        """
        Called when this object performs a look. It allows to
        customize just what this means. It will not itself
        send any data.

        Args:
            target (Object): The target being looked at. This is
                commonly an object or the current location. It will
                be checked for the "view" type access.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call. This will be passed into
                return_appearance, get_display_name and at_desc but is not used
                by default.

        Returns:
            lookstring (str): A ready-processed look string
                potentially ready to return to the looker.

        """
        if not target.access(self, "view"):
            try:
                return "Could not view '%s'." % target.get_display_name(self, **kwargs)
            except AttributeError:
                return "Could not view '%s'." % target.key

        description = target.return_appearance(self, **kwargs)

        # the target's at_desc() method.
        # this must be the last reference to target so it may delete itself when acted on.
        target.at_desc(looker=self, **kwargs)

        if target.typename is 'Room':
            self.msg('looked AT ROOM!!!!!!')
            if self.location:
                room = self.location
                room_data = {
                    "dbref": room.id,
                    "name": room.name,
                    "desc": room.db.desc,
                    "contents":  list(set(room.contents) - set(room.exits) - set([self])),
                    "exits": room.exits,
                }
                self.msg(room_data = room_data)


        return description

    pass
