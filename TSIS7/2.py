import pygame
import time
import logging
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s')

pygame.init()
W,H=600,600
screen = pygame.display.set_mode((W,H))

songs = ['download/music.mp3', 'download/music1.mp3', 'download/music2.mp3']
pygame.mixer.music.load(songs[0])
current_song_index = 0
pygame.mixer.music.play()
done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
            pygame.quit()
    user_input = input("press 'p' to play/stop, 'n' to play next song, 'b' to play the previous song, 'q' to quit")
    if user_input == 'p':
        if pygame.mixer.music.get_busy:
            pygame.mixer.music.pause()
            logging.info("Music paused")
        else:
            pygame.mixer.music.unpause()
            logging.info("Music resumed")
    
    elif user_input == 'n':
        current_song_index+=1
        if current_song_index > len(songs)-1:
            current_song_index = 0
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
    
    elif user_input == 'b':
        current_song_index-=1
        if current_song_index < 0:
            current_song_index = len(songs)-1
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
    
    elif user_input == 'q':
        pygame.mixer.music.stop()
        break
    
    time.sleep(1)
    pygame.display.update()
        
