
# import pygame
# import sys

# # Inisialisasi Pygame
# pygame.init()

# # Ukuran layar
# screen_width = 800
# screen_height = 600

# # Warna
# white = (255, 255, 255)

# # Inisialisasi layar
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Permainan Pygame Sederhana")

# # Inisialisasi posisi objek
# x = screen_width // 2
# y = screen_height // 2

# # Kecepatan pergerakan objek
# speed = 5

# # Loop utama
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= speed
#     if keys[pygame.K_RIGHT]:
#         x += speed
#     if keys[pygame.K_UP]:
#         y -= speed
#     if keys[pygame.K_DOWN]:
#         y += speed

#     # Bersihkan layar
#     screen.fill(white)

#     # Gambar objek
#     pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))

#     # Update tampilan
#     pygame.display.update()

# # Keluar dari Pygame
# pygame.quit()
# sys.exit()

