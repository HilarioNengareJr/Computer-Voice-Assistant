import pygame
import subprocess


class FileManager:
    
    def open_folder(self, path):
        subprocess.Popen(['xdg_open', path]) # Opens folder or file with the default application
    
    
    def play_music(self, path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
    def stop_music(self):
        pygame.mixer.music.stop()
        
    