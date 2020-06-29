import pygame
from itertools import cycle


class TrafficLight:

    # __color = 'black'
    __colors = [(50, 50, 50), (255, 0, 0), (255, 255, 0), (0, 230, 0)]
    # __colors_names = ["off", "red", "yellow", "green"]
    __radius = 40
    __margin = 10
    __positions = []
    __state = 0
    __states = [((1, 0, 0), 7), ((1, 1, 0) ,2), ((0, 0, 1) ,5), ((0, 1, 0) ,2)]

    def __init__(self):
        self.__sc = pygame.display.set_mode((self.__radius * 2 + self.__margin * 2, self.__radius * 6 + self.__margin * 4))
        self.__positions = [(self.__radius + self.__margin, self.__radius + self.__margin + i * (self.__radius * 2 + self.__margin)) for i in range(3)]
        self.checkout_state([0, 0, 0])
        pygame.time.delay(1000)

    def run(self, color):
        self.__color = color

        for s in cycle(self.__states):
            self.checkout_state(s[0])
            self.delay(s[1])

    def delay(self, delay):
        while delay > 0:
            pygame.time.delay(500)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            delay -= 0.5


    def checkout_state(self, states):
        [self.__light(i, i + 1 if s else 0) for i, s in enumerate(states)]

    def __light(self, *state):
        pygame.draw.circle(self.__sc, self.__colors[state[1]], self.__positions[state[0]], self.__radius)
        pygame.display.update()


pygame.init()
# states = [7, 2, 3, 2]

tl = TrafficLight()
tl.run("red")
