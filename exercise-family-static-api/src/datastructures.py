
from random import randint

starting_family = [
    {
        "first_name": "John",
        "age": 33,
        "lucky_numbers": [1, 4, 5]
    },
    {
        "first_name": "jane",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },
    {
        "first_name": "John",
        "age": 5,
        "lucky_numbers": [1]
    },
]

class FamilyStructure:
    def __init__(self, last_name):
        self._members = starting_family
        self.last_name = last_name

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generateId()
        self._members.append(member)
        return None

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return None
        

    def get_member(self, id):
        # fill this method and update the return
        for m in self._members:
            if m["id"] == int(id):
                return m

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members