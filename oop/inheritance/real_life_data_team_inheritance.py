class DataProfessional:
    def __init__(self, name):
        self.name = name

    def analyze(self):
        print(f"{self.name} is analyzing data.")

class Analyst(DataProfessional):
    def create_report(self):
        print(f"{self.name} is creating a business report.")

class DataEngineer(DataProfessional):
    def build_pipeline(self):
        print(f"{self.name} is building a data pipeline.")

    def analyze(self):
        print(f"{self.name} is analyzing data quality and performance.")

class DataScientist(DataProfessional):
    def build_model(self):
        print(f"{self.name} is building a machine learning model.")

    def analyze(self):
        print(f"{self.name} is analyzing data for patterns and insights.")

# Usage example
if __name__ == "__main__":
    alice = Analyst("Alice")
    bob = DataEngineer("Bob")
    carol = DataScientist("Carol")

    alice.analyze()
    alice.create_report()

    bob.analyze()
    bob.build_pipeline()

    carol.analyze()
    carol.build_model()
