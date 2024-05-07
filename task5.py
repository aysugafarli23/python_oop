#Python OOP Examples in mixed languages

class languages():
    sinif =  "dil"
    
    
    def __init__(self, id, name, country, learning_level, interest_level):
        self.id = id
        self.name = name
        self.country = country
        self.learning_level = learning_level
        self.interest_level = interest_level
        
    def simvollariVar(self, simvollariVar = True):
        if simvollariVar == False:
            return f"{self.name}nin simvollari yoxdur"
        else:
            return f"{self.name}nin simvollari vardir"
        
    def olkemizdeTedrisi(self, olkemizdeTedrisi = False):
        if olkemizdeTedrisi == True:
            return f"{self.name}nin ölkəmizdə tədrisi mövcuddur"
        else:
            return f"{self.name}nin ölkəmizdə tədrisi mövcud deyil"
        
    def teqaudluTehsili(self, teqaudluTehsili = True):
        if teqaudluTehsili == False:
            return f"{self.name}nin təqaüdlü təhsili mövcud deyil"
        else:
            return f"{self.name}nin təqaüdlü təhsili mövcuddur"
        
Koreya_dili = languages(1, "Koreya dili", "Koreya", "orta", "yüksək")
Çin_dili = languages(2,"Çin dili","Çin","çətin","orta")
Alman_dili = languages(3, "Alman dili", "Almaniya", "orta", "az")
İngilis_dili = languages(4, "İngilis dili", "İngilitərə və bir çox ölkə", "orta", "yüksək")

print(f"#{Koreya_dili.id} {Koreya_dili.name} {Koreya_dili.country}nın rəsmi dilidir.Eyni zamanda {Koreya_dili.learning_level} çətinlikli bu dil bir çox dünya xalqları tərəfindən {Koreya_dili.interest_level} maraqla qarşılanır.")
print(f"#{Çin_dili.id} {Çin_dili.name} {Çin_dili.country}in rəsmi dilidir.Eyni zamanda {Çin_dili.learning_level} çətinlikli bu dil bir çox dünya xalqları tərəfindən {Çin_dili.interest_level} maraqla qarşılanır.")
    
     
print(f"{Koreya_dili.simvollariVar()} ve {Koreya_dili.olkemizdeTedrisi(True)} {Koreya_dili.teqaudluTehsili()}")
print(Çin_dili.simvollariVar(), Çin_dili.olkemizdeTedrisi(True), Çin_dili.teqaudluTehsili())
print(Alman_dili.simvollariVar(False), Alman_dili.olkemizdeTedrisi())
print(İngilis_dili.simvollariVar(simvollariVar = False))

    
