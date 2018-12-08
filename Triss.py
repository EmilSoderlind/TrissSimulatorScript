
class Triss(object):
    prize = -1

    def __init__(self, newPrize):
        self.prize = newPrize

    def __init__(self):
        self.prize = -1

    def setPrize(self,newPrize):
        self.prize = newPrize

    def getPrize(self):
        return self.prize

    def __str__(self):
        return str("<Triss: prize: {}>".format(str(self.prize)))
