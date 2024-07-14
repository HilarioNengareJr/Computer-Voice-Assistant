import pygame
import subprocess
import shutil


class FileManager:
    
    def open_folder(self, path):
        subprocess.Popen(['xdg_open', path]) # Opens folder or file with the default application
    
    def open_application(self, app_name):
        
        app_path = shutil.which(app_name)
        
        if app_path:
            subprocess.Popen([app_path])
        
        else:
            print(f"{app_name} Not Found")
            
        
class MusicPlayer: 
    def play_music(self, path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
    def stop_music(self):
        pygame.mixer.music.stop()
        
    