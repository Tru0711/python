class Mother:
    def motherly_love(self):
        return "Mother's love"

class Father:
    def fatherly_advice(self):
        return "Father's advice"

class ChildWithParents(Mother, Father):
    def both_love(self):
        return "Both parents' love"


mp = ChildWithParents()
print(mp.motherly_love())
print(mp.fatherly_advice())
print(mp.both_love())