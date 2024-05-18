from pygame import *
import sys
font.init()

window = display.set_mode((800, 600))
display.set_caption('Menu')
clock = time.Clock()

menu_options = ['Start', 'Settings', 'Exit']
selected_option = 0
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

class Button():
    def __init__(self, text, x, y, h, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.hover_color = hover_color
    def draw(self, screen):
        x, y = mouse.get_pos()
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            draw.rect(screen, self.hover_color, (self.x, self.y, self.w, self.h))
        else:
            draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        text = font.SysFont('Arial', 36).render(self.text, True, WHITE)
        text_rect = text.get_rect(center = (self.x + self.w / 2, self.y + self.h / 2))
        screen.blit(text, text_rect)

buttons = []
for i,option in enumerate(menu_options):
    button = Button(option, 400-100, 200 + i * 50, 200, 50, BLACK, RED)
    buttons.append(button)

run = True
game_state = 'menu'
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(BLACK)
    if game_state == 'menu':
        for i, button in enemirate(buttons):
            if i == selected_option:
                button.color = GREEN
            else:
                button.color = BLACK
            button.draw(window)
    display.update()
    clock.tick(FPS)