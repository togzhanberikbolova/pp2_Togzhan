import pygame
pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
songs = ['download/music.mp3', 'download/music1.mp3', 'download/music2.mp3']


pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

current_song_index = 0
done=False
pause=False
vol=1.0
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done=True
         pygame.quit()
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            pause=not pause
            if pause:
               pygame.mixer.music.pause()
            else:
               pygame.mixer.music.unpause()
         elif event.key == pygame.K_UP:
            vol+=1
            pygame.mixer.music.set_volume(vol)
         elif event.key == pygame.K_DOWN:
            vol-=1
            pygame.mixer.music.set_volume(vol)
         elif event.key == pygame.K_RIGHT:
            current_song_index+=1
            if current_song_index > len(songs)-1:
               current_song_index = 0 
            pygame.mixer.music.load(songs[current_song_index])
            pygame.mixer.music.play()
         elif event.key == pygame.K_LEFT:
            current_song_index-=1
            if current_song_index<0:
               current_song_index=len(songs)-1
            pygame.mixer.music.load(songs[current_song_index])
            pygame.mixer.music.play()
   clock.tick(60)
   pygame.display.update()
        
