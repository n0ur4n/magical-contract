from magic import magical_contact
class witchorwizard(magical_contact):
    def wand_choice(self,wand,house):
        self.__wand={"Gryffindor":"Phoenix Feather",
"Slytherin":"Dragon heartstring",
"Ravenclaw":"unicorn hair",
"Hufflepuff":"Phoenix Feather"
    }
        self.__house={
        "Brave":"Gryffindor",
        "Sly":"Slytherin",
        "Smart":"Ravenclaw",
        "Loyal":"Huffle puff",
        "Nothing":"Invalid House"
    }
    def get_wand(self,wand):
        return (self.__wand)
    
    def get_house(self,house):
        return (self.__house)
    
    def describe_wizardorwitch(self):
        return f" wand : {self.get_wand()}, house: {self.get_house()}"