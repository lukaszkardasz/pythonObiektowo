class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        return f"Jestem {self.marka} {self.model}"

# Tworzymy obiekt
auto = Samochod("Toyota", "Corolla")
print(auto.przedstaw_sie())