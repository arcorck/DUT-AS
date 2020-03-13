class Box:
    def __init__(self):
        self._contents = []
        self.ouvert = False
    
    

    def add(self,truc):
        self._contents.append(truc)

 
    def __contains__(self,machin):
        return machin in self._contents

    def remove(self,machin):
        self._contents.remove(machin)
    
    def action_look(self):
        if not self.is_open():
            return "la boite est fermée !"
        else:
            return "la boite contient: "+', '.join(self._contents)

    def is_open(self):
        return self.ouvert

    def open(self):
        self.ouvert = True

    def close(self):
        self.ouvert = False

    
class Thing:
    def __init__(self,volume, name=None):
        self._volume = volume
        self._name = name

    def volume(self):
        return self._volume

    def name(self):
        return self._name

