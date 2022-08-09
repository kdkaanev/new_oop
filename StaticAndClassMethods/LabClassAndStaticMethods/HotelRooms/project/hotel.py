from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        pass

    def add_room(self, room: Room):
        pass

    def take_room(self, room_number, people):
        pass

    def free_room(self, room_number):
        pass

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
            f"Free rooms: {}\n"\
             f"   Taken rooms: {}"
