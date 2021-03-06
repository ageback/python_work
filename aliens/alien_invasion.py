import sys
import pygame
import os.path
from time import sleep

from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """
    管理游戏资源和行为的类。
    """

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.set_screen_mode()
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例。
        #   并创建记分牌。
        self.stats = GameStats(self)
        self.read_highscore()
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")

    def read_highscore(self):
        highscore_file = 'high_score.txt'
        if os.path.exists(highscore_file):
            with open(highscore_file) as file_obj:
                self.stats.high_score = int(file_obj.read())

    def set_screen_mode(self):
        if not self.settings.full_screen_mode:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        else:
            # 全屏模式运行
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed and self.stats.game_active:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人。
        #  如果是，就删除相应的子弹和外星人。
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.aliens:
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            # 消灭所有外星人后提高游戏速度
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 显示得分
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_key_up_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_key_down_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.exit_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            self._start_game()

    def exit_game(self):
        highscore_file = 'high_score.txt'
        with open(highscore_file, 'w') as file_obj:
            file_obj.write(str(self.stats.high_score))
        sys.exit()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """
        响应飞船被外星人撞到。
        """
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.stats.reset_stats()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """
        检查是否有外星人到达了屏幕底端
        :return:
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 游戏开始时重置初始值。
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        # 隐藏鼠标光标
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
