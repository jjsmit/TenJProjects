class DiffEnt():
    PublicMod = 23
    PublicBase = 5

    def __init__(self, PickedNumber, otherDiffEnt = None):
        self.PickedNumber = PickedNumber
        self.publicKey = self.PublicBase**self.PickedNumber % self.PublicMod
        if otherDiffEnt != None:
            self.ComputeKey(otherDiffEnt.publicKey)
            otherDiffEnt.ComputeKey(self.publicKey)

    def ComputeKey(self, PublicKey):
        self.SecretKey= PublicKey**self.PickedNumber % DiffEnt.PublicMod
