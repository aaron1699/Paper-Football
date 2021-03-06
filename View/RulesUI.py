import sys
import pygame
import Colours
from pygame import mixer
import Settings
import View.MenuUI
# import tkinter as tk  # tkinter is used for GUI. Probably will have to use it at some point for any input

pygame.init()


class RulesUI:
    """
    Class representing Rules view
    """

    # Art
    title = pygame.font.SysFont('comicsansms', 50)
    font = pygame.font.SysFont('comicsansms', 18)
    exit_icon = pygame.image.load("Art/exit2.png")
    rules = pygame.image.load("Art/game_rules.png")

    def __init__(self, controller):
        # State
        self.is_running = False

        # Context
        self.screen = controller.screen
        self.controller = controller
        self.rules_icon_rect = self.exit_icon.get_rect()
        self.rules_rect = self.rules.get_rect()

    def main(self):
        self.event_handler()
        # Ticking
        self.controller.delta_time += self.controller.clock.tick() / 1000.0
        while self.controller.delta_time > 1 / Settings.max_tps:
            self.controller.delta_time -= 1 / Settings.max_tps
            self.update()
            self.render()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.close_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.controller.change_view(self.controller.gameUI)
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.rules_icon_rect.collidepoint(pygame.mouse.get_pos()):
                    self.controller.change_view(self.controller.gameUI)

    def update(self):
        # Layout helper variables
        sw = self.screen.get_width()
        sh = self.screen.get_height()

        self.rules_icon_rect.bottomright = (sw - 20, sh - 20)
        self.rules_rect.center = (sw/2, sh/2)

    def render(self):
        # Clear screen
        self.screen.fill((0, 0, 0))

        # Background
        self.screen.blit(self.rules, self.rules_rect)

        # Button
        self.screen.blit(self.exit_icon, self.rules_icon_rect)

        # Show new frame
        pygame.display.flip()

