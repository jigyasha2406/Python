class sound():
    def make_sound(self):
        print("diffrent animal make different sound")
class dog(sound):
    def make_sound(self):
        print("Barks")
class cat(sound):
    def make_sound(self):
        print("meow")
class cow(sound):
    def make_sound(self):
        print("woo")
dog=dog()
cat=cat()
cow=cow()
cow.make_sound()
cat.make_sound()
dog.make_sound()
