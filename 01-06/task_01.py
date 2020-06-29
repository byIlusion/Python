import pygame
from itertools import cycle


class TrafficLight:
    __color = 'off'
    __colors = [(50, 50, 50), (255, 0, 0), (255, 255, 0), (0, 230, 0)]
    __radius = 40
    __margin = 10
    __positions = []
    __state = 0
    # На 4 итерации не перепутано, а так задумано ------------------\ /
    __states = [((1, 0, 0), 7), ((0, 1, 0), 2), ((0, 0, 1), 5), ((0, 1, 1), 2)]

    def __init__(self):
        self.__sc = pygame.display.set_mode(
            (self.__radius * 2 + self.__margin * 2, self.__radius * 6 + self.__margin * 4))
        self.__positions = [
            (self.__radius + self.__margin, self.__radius + self.__margin + i * (self.__radius * 2 + self.__margin)) for
            i in range(3)]
        self.checkout_state([0, 0, 0])
        pygame.time.delay(1000)

    def run(self):
        for s in cycle(self.__states):
            if s[0][0] == 1:
                self.__color = "Красный"
                print(f"{self.__color}! СТОП!")
            elif s[0][1] == 1:
                self.__color = "Желтый"
                print(f"{self.__color}. Внимание")
            else:
                self.__color = "Зеленый"
                print(f"{self.__color}. Поехали!")
            self.checkout_state(s[0])
            self.delay(s[1], True if s[0][1] == 0 else False)

    def delay(self, delay, show_timer=True):
        f1 = pygame.font.Font(None, 42)
        while delay > 0:
            if show_timer:
                self.__light(1, 0)
                text1 = f1.render(f"{delay:02d}", 1, (255, 255, 255))
                self.__sc.blit(text1, (int(self.__positions[1][0] - self.__radius / 2), int(self.__positions[1][1] - self.__radius / 2)))
                pygame.display.update()
            pygame.time.delay(1000)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            delay -= 1

    def checkout_state(self, states):
        [self.__light(i, i + 1 if s else 0) for i, s in enumerate(states)]

    def __light(self, *state):
        pygame.draw.circle(self.__sc, self.__colors[state[1]], self.__positions[state[0]], self.__radius)
        pygame.display.update()


pygame.init()

tl = TrafficLight()
tl.run()
