from abc import ABC


class Furniture(ABC):

    def use(self):
        pass


class Chair(Furniture):

    def use(self):
        print("Sit on")


class Bed(Furniture):

    def use(self):
        print("Sleep on")


class Table(Furniture):

    def use(self):
        print("Place stuff on")


class Draws(Furniture):

    def use(self):
        print("Put stuff away")


# run the code
C = Chair()
C.use()

B = Bed()
B.use()

T = Table()
T.use()

D = Draws()
D.use()
