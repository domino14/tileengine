# A tile engine for Pygame.
import pygame
import json
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)


class TileEngine(object):
    """
    A tile engine that can be embedded into a world map creator or
    a game map.

    """
    # A 2-D array, initialize to empty.
    BASE_TILE_SIZE = 60  # Pixels.
    world_map = []
    dim_x = 0
    dim_y = 0
    # A dict of tile number to texture image file.
    tile_map = {}

    # def __init__(self, x, y):
    #     """
    #     Initialize the world map to have dimensions x by y.
    #     """
    #     self.dim_x = x
    #     self.dim_y = y
    #     for j in range(y):
    #         self.world_map.append([0] * x)

    #     print self.world_map

    def __init__(self, viewport_dims):
        self.load_tile_map('data/tile_mapping.json')
        self.load_world_map('data/world_map.json')
        # Pixel coordinates of top left.
        self.viewport_topleft = (0, 0)
        self.viewport_dims = viewport_dims

    def load_tile_map(self, filename):
        """
        Loads a JSON file that contains a map of tile number to filename.
        Also load images.

        """
        f = open(filename)
        tiles = json.loads(f.read())
        f.close()
        for tile, filename in tiles.iteritems():
            self.tile_map[tile] = pygame.image.load(filename)
        logging.debug('Done loading tile map.')

    def load_world_map(self, filename):
        """
        Loads a JSON 2-D array with the world map.
        """
        f = open(filename)
        self.world_map = json.loads(f.read())
        f.close()
        self.dim_x = len(self.world_map[0])
        self.dim_y = len(self.world_map)

    def set_viewport_topleft(self, topleft):
        """
        Sets the x, y pixel coordinates of the top left.
        It starts at 0, 0.
        """
        self.viewport_topleft = topleft

    def blit_map(self, background):
        """
        Blits the map.
        :param background - A Pygame surface.

        """
        # Find the X, Y tile coordinate of the top left tile (even if
        # it's partially obscured). These coords are u, v
        u = self.viewport_topleft[0] / self.BASE_TILE_SIZE
        v = self.viewport_topleft[1] / self.BASE_TILE_SIZE
        # Set counters and loop through tiles.
        x = -(self.viewport_topleft[0] % self.BASE_TILE_SIZE)
        i = u
        while x < self.viewport_dims[0]:
            y = -(self.viewport_topleft[1] % self.BASE_TILE_SIZE)
            j = v
            while y < self.viewport_dims[1]:
                # j is the row (y), i is the col (x)
                try:
                    tile = self.world_map[j][i]
                except IndexError:
                    break
                background.blit(self.tile_map[str(tile)], (x, y))
                y += self.BASE_TILE_SIZE
                j += 1
            x += self.BASE_TILE_SIZE
            i += 1



