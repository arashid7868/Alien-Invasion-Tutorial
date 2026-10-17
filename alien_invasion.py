"""Run the Alien Invasion game using Pygame."""

import sys
from pathlib import Path

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage the game resources and behavior."""

    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()

        self.settings = Settings()
        self.base_path = Path(__file__).resolve().parent

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height,
            )
        )

        pygame.display.set_caption("Alien Invasion - Part 1")

        background_path = (
            self.base_path
            / "Assets"
            / "images"
            / "Starbasesnow.png"
        )

        self.background = pygame.image.load(
            str(background_path)
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (
                self.settings.screen_width,
                self.settings.screen_height,
            ),
        )

        self.ship = Ship(self)
        self.clock = pygame.time.Clock()

        print("Game initialized successfully.")
        print(f"Display size: {self.screen.get_size()}")
        print("Use LEFT and RIGHT arrow keys to move.")
        print("Press Q or close the window to exit.")

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.frame_rate)

    def _check_events(self):
        """Respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    self._quit_game()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Draw the background and ship on the screen."""
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        pygame.display.flip()

    @staticmethod
    def _quit_game():
        """Shut down Pygame and exit."""
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()