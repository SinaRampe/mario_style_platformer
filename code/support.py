from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for img_file in img_files:
            img_surf = pygame.image.load(f"graphics/player/{img_file}").convert_alpha()
            surface_list.append(img_surf)

    return surface_list