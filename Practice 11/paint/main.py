import pygame
import sys
import math  # needed for triangle calculations

pygame.init()

# Window setup
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = [BLACK, RED, GREEN, BLUE, YELLOW]
current_color = BLACK

# Brush sizes
brush_sizes = [4, 8, 16]
current_size = brush_sizes[0]

# Tool states
eraser = False
mode = "brush"  # brush, rect, circle, square, rtriangle, etriangle, rhombus

# Drawing states
drawing = False
last_pos = None
start_pos = None

# Canvas (separate surface to keep drawings)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Font for UI
font = pygame.font.SysFont(None, 24)

def draw_ui():
    """Draw all UI buttons"""

    # Color buttons
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*50, 10, 40, 40))
    
    # Brush size buttons
    for i, size in enumerate(brush_sizes):
        pygame.draw.rect(screen, BLACK, (10 + i*50, 60, 40, 40), 2)
        pygame.draw.circle(screen, BLACK, (30 + i*50, 80), size)
    
    # Eraser button
    pygame.draw.rect(screen, (200, 200, 200), (10, 110, 100, 40))
    screen.blit(font.render("Eraser", True, BLACK), (20, 120))

    # Clear button
    pygame.draw.rect(screen, (220, 220, 220), (10, 160, 100, 40))
    screen.blit(font.render("Clear", True, BLACK), (25, 170))

    # Shape buttons
    buttons = [
        ("Rect", 210),
        ("Circle", 260),
        ("Square", 310),
        ("R-Tri", 360),
        ("E-Tri", 410),
        ("Rhomb", 460),
    ]

    for text, y in buttons:
        pygame.draw.rect(screen, (200, 200, 255), (10, y, 100, 40))
        screen.blit(font.render(text, True, BLACK), (20, y + 10))


def draw_shape(surface, mode, start, end, color, width):
    """Draw different shapes based on mode"""

    x1, y1 = start
    x2, y2 = end

    if mode == "rect":
        rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        pygame.draw.rect(surface, color, rect, width)

    elif mode == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, side, side)
        pygame.draw.rect(surface, color, rect, width)

    elif mode == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, radius, width)

    elif mode == "rtriangle":
        # Right triangle (90° angle)
        points = [start, (x2, y1), end]
        pygame.draw.polygon(surface, color, points, width)

    elif mode == "etriangle":
        # Equilateral triangle
        side = math.hypot(x2 - x1, y2 - y1)
        height = (math.sqrt(3) / 2) * side

        p1 = start
        p2 = (x1 + side, y1)
        p3 = (x1 + side / 2, y1 - height)

        pygame.draw.polygon(surface, color, [p1, p2, p3], width)

    elif mode == "rhombus":
        # Rhombus (diamond shape)
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        points = [
            (cx, y1),
            (x2, cy),
            (cx, y2),
            (x1, cy)
        ]
        pygame.draw.polygon(surface, color, points, width)


running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_ui()

    # Preview shape while dragging mouse
    if drawing and start_pos and mode != "brush":
        current_pos = pygame.mouse.get_pos()
        color = WHITE if eraser else current_color
        draw_shape(screen, mode, start_pos, current_pos, color, current_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Hotkeys for tools
            if event.key == pygame.K_e:
                eraser = not eraser
                mode = "brush"

            if event.key == pygame.K_z:
                mode = "brush"
                eraser = False

            if event.key == pygame.K_SPACE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Color selection
            for i, color in enumerate(colors):
                if pygame.Rect(10 + i*50, 10, 40, 40).collidepoint(x, y):
                    current_color = color
                    eraser = False
                    mode = "brush"

            # Brush size selection
            for i, size in enumerate(brush_sizes):
                if pygame.Rect(10 + i*50, 60, 40, 40).collidepoint(x, y):
                    current_size = size

            # UI buttons
            if pygame.Rect(10, 110, 100, 40).collidepoint(x, y):
                eraser = True
                mode = "brush"

            if pygame.Rect(10, 160, 100, 40).collidepoint(x, y):
                canvas.fill(WHITE)

            # Shape buttons
            shape_map = {
                210: "rect",
                260: "circle",
                310: "square",
                360: "rtriangle",
                410: "etriangle",
                460: "rhombus"
            }

            for y_pos, shape in shape_map.items():
                if pygame.Rect(10, y_pos, 100, 40).collidepoint(x, y):
                    mode = shape
                    eraser = False

            drawing = True
            last_pos = event.pos
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos
                color = WHITE if eraser else current_color

                if mode == "brush":
                    pass
                else:
                    draw_shape(canvas, mode, start_pos, end_pos, color, current_size)

            drawing = False
            last_pos = None
            start_pos = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            # Free drawing (brush)
            if mode == "brush":
                if last_pos:
                    color = WHITE if eraser else current_color
                    pygame.draw.line(canvas, color, last_pos, event.pos, current_size)
                last_pos = event.pos

    pygame.display.flip()

pygame.quit()
sys.exit()