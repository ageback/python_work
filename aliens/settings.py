class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 650

        # 飞船设置
        self.ship_speed = 1.5
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移。
        self.fleet_direction = 1
