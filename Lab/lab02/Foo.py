class Foo:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def speak(self):
       return f"{self.name} says hello!"

    def __repr__(self):
        return f"Foo({self.name}, {self.profession})"
