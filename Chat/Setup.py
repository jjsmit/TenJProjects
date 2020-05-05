class DiffEnt():
    PublicBase = 5
    PublicMod = 23

    def __init__(self, PickedNumber):
        self.PickedNumber = PickedNumber
        self.N = DiffEnt.PublicBase**self.PickedNumber%DiffEnt.PublicMod

    def ComputeKey(self, OutN):
        self.OutN = OutN
        self.Secret = self.OutN**self.PickedNumber%DiffEnt.PublicMod
        return self.Secret
