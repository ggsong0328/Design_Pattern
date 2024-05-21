import pygame
import os
import random
from abc import ABC, abstractmethod

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "boo_1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "boo_2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "boo_3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "boo_1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "boo_2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "boo_3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

class GameState:
    _instance = None

    @staticmethod
    def get_instance():
        if GameState._instance is None:
            GameState()
        return GameState._instance

    def __init__(self):
        if GameState._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GameState._instance = self
            self.game_speed = 10
            self.points = 0

    def increase_speed(self):
        self.game_speed += 0

    def add_points(self, amount):
        self.points += amount

class State(ABC):
    @abstractmethod
    def handle_input(self, dinosaur, input):
        pass

    @abstractmethod
    def update(self, dinosaur):
        pass

class RunningState(State):
    def handle_input(self, dinosaur, input):
        if input[pygame.K_UP]:
            dinosaur.set_state(JumpingState())
        elif input[pygame.K_DOWN]:
            dinosaur.set_state(DuckingState())

    def update(self, dinosaur):
        dinosaur.image = dinosaur.run_img[dinosaur.step_index // 5]
        dinosaur.dino_rect.y = dinosaur.Y_POS
        dinosaur.step_index = (dinosaur.step_index + 1) % 10

class JumpingState(State):
    def handle_input(self, dinosaur, input):
        pass  # Jumping is handled by the state itself

    def update(self, dinosaur):
        dinosaur.image = dinosaur.jump_img
        dinosaur.dino_rect.y -= dinosaur.jump_vel * 4
        dinosaur.jump_vel -= 0.8
        if dinosaur.jump_vel < -dinosaur.JUMP_VEL:
            dinosaur.set_state(RunningState())
            dinosaur.jump_vel = dinosaur.JUMP_VEL

class DuckingState(State):
    def handle_input(self, dinosaur, input):
        if not input[pygame.K_DOWN]:
            dinosaur.set_state(RunningState())

    def update(self, dinosaur):
        dinosaur.image = dinosaur.duck_img[dinosaur.step_index // 5]
        dinosaur.dino_rect.y = dinosaur.Y_POS_DUCK
        dinosaur.step_index = (dinosaur.step_index + 1) % 10

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.state = RunningState()

    def set_state(self, state):
        self.state = state

    def update(self, userInput):
        self.state.handle_input(self, userInput)
        self.state.update(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        game_state = GameState.get_instance()
        self.x -= game_state.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        game_state = GameState.get_instance()
        self.rect.x -= game_state.game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class ObstacleFactory:
    @staticmethod
    def create_obstacle(obstacle_type):
        if obstacle_type == 'small_cactus':
            return SmallCactus(SMALL_CACTUS)
        elif obstacle_type == 'large_cactus':
            return LargeCactus(LARGE_CACTUS)
        elif obstacle_type == 'bird':
            return Bird(BIRD)

def main():
    global x_pos_bg, y_pos_bg, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_state = GameState.get_instance()
    x_pos_bg = 0
    y_pos_bg = 380
    obstacles = []
    death_count = 0
    font = pygame.font.Font('freesansbold.ttf', 20)

    def score():
        game_state.add_points(1)
        if game_state.points % 100 == 0:
            game_state.increase_speed()

        text = font.render("Points: " + str(game_state.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_state.game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            obstacle_type = random.choice(['small_cactus', 'large_cactus', 'bird'])
            obstacles.append(ObstacleFactory.create_obstacle(obstacle_type))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(25)
        pygame.display.update()

def menu(death_count):
    run = True
    game_state = GameState.get_instance()
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        else:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score_text = font.render("Your Score: " + str(game_state.points), True, (0, 0, 0))
            scoreRect = score_text.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score_text, scoreRect)
            if death_count >= 1:
                game_state.points = 0

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
