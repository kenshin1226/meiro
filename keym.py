import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
pvx = 0  # 横方向の速度を初期化
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_LEFT:
                if mods & pygame.KMOD_CTRL:  # Ctrlキーが押されているかチェック
                    print("Ctrl + Left Arrow")
                elif mods & pygame.KMOD_SHIFT:  # Ctrlキーが押されているかチェック
                    print("SHIFT + Left Arrow")
                else:
                    print("Left Arrow")
            elif event.key == pygame.K_RIGHT:
                if mods & pygame.KMOD_CTRL:  # Ctrlキーが押されているかチェック
                    print("Ctrl + Right Arrow")
                elif mods & pygame.KMOD_SHIFT:  # Ctrlキーが押されているかチェック
                    print("SHIFT + Right Arrow")
                else:
                    print("Right Arrow")
    # ここでpvxを使って何かしらの処理を行う
    # 例: オブジェクトの位置を更新する
    pygame.display.flip()
pygame.quit()