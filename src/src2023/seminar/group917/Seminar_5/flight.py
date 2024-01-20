class Flight:
    def __init__(self, oras_plecare, oras_destinatie, ora_plecare, ora_sosire):
        self.__oras_plecare = oras_plecare
        self.__oras_destinatie = oras_destinatie
        self.__ora_plecare = ora_plecare
        self.__ora_sosire = ora_sosire

    @property
    def oras_plecare(self):
        return self.__oras_plecare

    @property
    def oras_destinatie(self):
        return self.__oras_destinatie

    @property
    def ora_plecare(self):
        return self.__ora_plecare

    @property
    def ora_sosire(self):
        return self.__ora_sosire

    def __str__(self):
        return "Flight: [Oras plecare:{} | Oras sosire: {} | Ora plecare: {} | Ora sosire: {}]".format(
            self.__oras_plecare, self.oras_destinatie, str(self.ora_plecare), str(self.__ora_sosire))