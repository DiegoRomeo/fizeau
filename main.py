import sys
from time import time

import asyncio

import pygame
from pygame.locals import *

from gear import Gear
from light_sensor import LightSensor
from light_source import LightSource
from mirror import Mirror, RotatedMirror
from text import Font
from slider import Slider
from fire import Flame
from button import SwitchButton
from message_box import MessageBox
from graph import Graph


pygame.init()
pygame.display.set_caption("Fizeau")

icon = pygame.image.load("./assets/fizeau.png")
bg = pygame.transform.scale_by(pygame.image.load("./assets/bg.png"), 1.5)
bg.set_alpha(50)

pygame.display.set_icon(icon)

fps = 60
clock = pygame.time.Clock()
 
width, height = 1280, 720
screen = pygame.display.set_mode((width, height), RESIZABLE)

def rgb(hexa):
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))



lightsource = LightSource(180, 500)
rotated_mirror = RotatedMirror(lightsource.x, lightsource.y - 200)
mirror = Mirror(1200, rotated_mirror.y)
gear = Gear(rotated_mirror.x + 100, rotated_mirror.y, 8, 1)
lightsensor = LightSensor(20, rotated_mirror.y)
flame = Flame(lightsource.x + lightsource.image.get_width() // 2, lightsource.y)

# Controllers
slider = Slider(80, 700, 140, 20, 0, 30, 0.1, "Angular Velocity")
switch = SwitchButton(250, 688, "Torch")


graph = Graph(850, 500)

particles = []

# FONTS
my_font = Font("./assets/large_font.png")

counter = 0
bar_height = 100

display = pygame.Surface((300, 200))
main_display = display.copy()
main_display.set_colorkey((0,0,0))
background_timer = 0

game_speed = 3
background_color = rgb("352b40")

info = MessageBox(20, 20, "Fizeau's experiment")

def dtf(dt):
    return dt / 1000 * 60

async def main():
    global counter
    # Game loop.

    while True:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        dt = clock.tick()
        mouse_position = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if switch.rectangle.collidepoint(mouse_position):
                    switch.pressed = not switch.pressed
        # Check collisions

        for particle in particles:
            if particle.mask.overlap(rotated_mirror.mask, (rotated_mirror.x - particle.x, rotated_mirror.y - particle.y)) and not particle.reflected:
                rotated_mirror.reflect(particle)
                particle.reflected = True

            elif particle.mask.overlap(mirror.mask, (mirror.x - particle.x, mirror.y - particle.y)):
                mirror.reflect(particle)

            elif gear.check_collision(particle):
                particles.remove(particle)
                del particle

            elif particle.mask.overlap(lightsensor.mask, (lightsensor.x - particle.x, lightsensor.y - particle.y)):
                graph.data.append([graph.width, 20])
                particles.remove(particle)
                del particle

            else:
                graph.data.append([graph.width, 0])

        if slider.container_rect.collidepoint(mouse_position) and mouse_pressed[0]:
            slider.move_slider(mouse_position)

        # Update
        counter += 0.5
        if counter > 10:
            counter = 1

        if counter % 2 and switch.pressed:
            particles.append(lightsource.generate_particle())

        for particle in particles:
            particle.update(1/fps)

        angular_velocity = int(slider.get_value())
        slider.text = f"Angular Velocity: {angular_velocity}"
        gear.angular_velocity = angular_velocity

        # Draw
        if switch.pressed:
            flame.draw(screen)
        else:
            graph.data.append([graph.width, 0])


        lightsource.draw(screen)
        gear.draw(screen)

        for particle in particles:
            particle.draw(screen)

        lightsensor.draw(screen)

        slider.render(screen)
        switch.draw(screen)
        rotated_mirror.draw(screen)
        mirror.draw(screen)

        info.render(screen)
        graph.render(screen, dt)
        my_font.render(screen, "Light received", graph.x + 20, graph.y + 20, "white", 1)

        pygame.display.flip()
        clock.tick(fps)

        await asyncio.sleep(0)

asyncio.run(main())
