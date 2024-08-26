from magic import magical_contact
class magical_creature(magical_contact):
    def status(self,species,tame):
        self.__species=species
        self.__tame=True

    def get_species(self,species):
        return self.__species
    
    def get_tame(self ,tame):
        return self.__tame
    
    def describe_creature(self):
        return f" species : {self.get_species()},tame: {self.get_tame()}"