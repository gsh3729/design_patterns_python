'''
provides a simplified interface to a complex subsystem
It hides the complexity of the system and provides a unified interface to the client
'''
# Subsystem classes

class DVDPlayer:
    def on(self):
        print("DVD Player ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def off(self):
        print("DVD Player OFF")


class Projector:
    def on(self):
        print("Projector ON")

    def wide_screen_mode(self):
        print("Projector in widescreen mode")

    def off(self):
        print("Projector OFF")


class Lights:
    def dim(self):
        print("Lights dimmed")

    def on(self):
        print("Lights ON")


class Amplifier:
    def on(self):
        print("Amplifier ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")

    def off(self):
        print("Amplifier OFF")


# Facade class

class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, lights: Lights, amp: Amplifier):
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.amp = amp

    def watch_movie(self, movie):
        print("\nGet ready to watch a movie...")
        self.lights.dim()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("\nShutting movie theater down...")
        self.dvd.off()
        self.amp.off()
        self.projector.off()
        self.lights.on()


# Client code

dvd = DVDPlayer()
projector = Projector()
lights = Lights()
amp = Amplifier()

home_theater = HomeTheaterFacade(dvd, projector, lights, amp)
home_theater.watch_movie("Inception")
home_theater.end_movie()
