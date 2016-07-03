from solder import Solder


class SolderFactory:
    @classmethod
    def create(cls):
        solder = Solder()
        return solder
