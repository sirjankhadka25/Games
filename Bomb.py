import time
import pygame

def timebomb():
    time_str = "00:00:05"  # 5 seconds
    h, m, s = map(int, time_str.split(":"))
    total_seconds = h * 3600 + m * 60 + s

    pygame.mixer.init()
    explosion_sound = pygame.mixer.Sound("explosion.mp3")

    while total_seconds > 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        print(f"{h:02d}:{m:02d}:{s:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("💥 BOOM!")
    explosion_sound.play()
    time.sleep(3)  # wait so sound can finish

timebomb()
