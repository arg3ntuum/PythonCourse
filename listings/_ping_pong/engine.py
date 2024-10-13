class Engine:
    def __init__(self):
        pass

    @staticmethod
    def bounce(ball, screen_height) -> bool:
        if ball.rect.top <= 0 or ball.rect.bottom >= screen_height:
            ball.dy = -ball.dy
            return True
        return False

    @staticmethod
    def collide(ball, platform) -> bool:
        if ball.rect.colliderect(platform.rect):
            ball.dx = -ball.dx
            return True
        return False
