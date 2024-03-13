import pygame, sys

class ParticlePrinciple:
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            for particle in self.particles:
                particle[0][1] += particle[2]
                particle[1] -= 0.2
                pygame.draw.circle(screen, pygame.Color('white'))

    def add_particles(self):
        pos_x = 250
        pos_y = 250
        radius = 10
        direction = -1
        particle_circle = [[pos_x, pos_y], radius, direction]
        self.particles.append(particle_circle)

    def delete_particles(self):
        pass # deletes particles after a certain time



pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()

    screen.fill((30, 30, 30))
    particle1.emit()
    pygame.display.update()
    clock.tick(120)