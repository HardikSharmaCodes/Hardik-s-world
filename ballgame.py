import pygame
import math

def add_side(polygon, center):
    """Add one more side while keeping all vertices equidistant from the center."""
    cx, cy = center
    n = len(polygon) 
    r = math.dist(center, polygon[0])  # distance from center to a vertex

    new_n = n + 1
    new_polygon = []
    for i in range(new_n):
        angle = 2 * math.pi * i / new_n 
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        new_polygon.append((x, y))

    return new_polygon

def closest_point_on_segment(px, py, x1, y1, x2, y2):
    """Return closest point on segment (x1,y1)-(x2,y2) to point (px,py)."""
    dx, dy = x2 - x1, y2 - y1
    if dx == dy == 0:
        return (x1, y1)
    t = ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)
    t = max(0, min(1, t))  # clamp to segment
    return (x1 + t * dx, y1 + t * dy)

def reflect_velocity(vx, vy, nx, ny):
    """Reflect velocity (vx,vy) across normal (nx,ny)."""
    length = math.hypot(nx, ny)
    nx, ny = nx / length, ny / length
    dot = vx * nx + vy * ny
    rvx = vx - 2 * dot * nx
    rvy = vy - 2 * dot * ny
    return rvx, rvy

pygame.init()
display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

running = True
center = (640, 360)
circle_radius = 15

# start with a square
pollist = [
    (center[0] + 200, center[1] + 200),
    (center[0] - 200, center[1] + 200),
    (center[0] - 200, center[1] - 200),
    (center[0] + 200, center[1] - 200)
]

# ball starts inside
circlex, circley = 640, 360
vx, vy = 4, 3  # initial velocity

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill("black")

    # move ball
    circlex += vx
    circley += vy

    # check collisions with polygon edges
    for i in range(len(pollist)):
        x1, y1 = pollist[i]
        x2, y2 = pollist[(i+1) % len(pollist)]

        cx, cy = closest_point_on_segment(circlex, circley, x1, y1, x2, y2)
        dist = math.hypot(circlex - cx, circley - cy)

        if dist < circle_radius:  # collision!
            circle_radius += 1
            # inward normal of edge (pointing toward polygon center)
            ex, ey = x2 - x1, y2 - y1
            nx, ny = -ey, ex
            if (center[0] - circlex) * nx + (center[1] - circley) * ny < 0:
                nx, ny = -nx, -ny  # flip to point inward

            # push ball back inside
            overlap = circle_radius - dist
            circlex += nx / math.hypot(nx, ny) * overlap
            circley += ny / math.hypot(nx, ny) * overlap

            # bounce
            vx, vy = reflect_velocity(vx, vy, nx, ny)

            # add side to polygon
            pollist = add_side(pollist, center)
            break  # handle one collision per frame

    # draw polygon and ball
    pygame.draw.polygon(display, (0,255,0), pollist, 2)
    pygame.draw.circle(display, (0,0,255), (int(circlex), int(circley)), circle_radius)

    pygame.display.flip()
    clock.tick(60)
