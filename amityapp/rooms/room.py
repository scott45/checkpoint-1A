__author__ = 'scotty'


# room class models the rooms in amity and is to be inherited by class office and livingspace

class Room(object):
    def __init__(self, room_name, room_type, capacity):
        self.room_name = room_name.title()
        self.room_type = room_type.strip().title()
        self.capacity = capacity
        self.occupants = []

    # functionality for adding a person to a room
    def add_person(self, person):
        self.occupants.append(person)
        self.capacity -= 1
        return self.capacity


class LivingSpace(Room):
    # Ls class method from the Room class and overrides some properties using the super function call.

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(
            room_name, room_type='Living Space', capacity=4
        )


class Office(Room):
    # office class method from the Room class and overrides some properties using the super function call.

    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type='Office', capacity=6
        )
