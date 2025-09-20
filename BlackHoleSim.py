import pygame 
import math

pygame.init()
running = True
display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

class lightray:
    def __init__(self, speed = 1, xpos = 10, ypos = 360):
        self.speed = speed
        self.xpos = xpos
        self.ypos = ypos
        self.ray_velocity_x = speed  
        self.ray_velocity_y = 0      
    def move(self, distance, bend):
        vector_to_blackhole_x = 640 - self.xpos
        vector_to_blackhole_y = 360 - self.ypos
        unit_vector_to_blackhole_x = vector_to_blackhole_x / distance + 0.00000001
        unit_vector_to_blackhole_y = vector_to_blackhole_y / distance + 0.00000001
        self.ray_velocity_x += unit_vector_to_blackhole_x * bend
        self.ray_velocity_y += unit_vector_to_blackhole_y * bend
        velocity_magnitude = math.sqrt(self.ray_velocity_x**2 + self.ray_velocity_y**2)
        self.ray_velocity_x = (self.ray_velocity_x / velocity_magnitude) * self.speed
        self.ray_velocity_y = (self.ray_velocity_y / velocity_magnitude) * self.speed
        self.xpos += self.ray_velocity_x
        self.ypos += self.ray_velocity_y
    def distance(self) -> float:
        vector_to_blackhole_x = 640 - self.xpos
        vector_to_blackhole_y = 360 - self.ypos
        distance = math.sqrt(vector_to_blackhole_x**2 + vector_to_blackhole_y**2)
        return distance
    def bend(self, distance , speedoflight, massofblackhole, gc) -> float:
        bend = (4*gc*massofblackhole) / ((speedoflight**2) * (distance+1e-9)) / 1e10
        return bend

c = 29972458
mass = 8.54e33
gc = 6.674e-11

rays = [lightray(1, 20, y) for y in range(200, 521, 40)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    blackHole = pygame.draw.circle(display, (0,0,255), (640,360), 50)

    for ray in rays:
        pygame.draw.circle(display, (255,255,255), (ray.xpos,ray.ypos), 1)
        ray.move(ray.distance(), ray.bend(ray.distance(), c, mass , gc))
    
    fade_surface = pygame.Surface((1280, 720))
    fade_surface.set_alpha(50) 
    fade_surface.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)
