## 크롬 공룡 게임 리팩토링
#### 202001818 송강규
#### test.py가 리팩토링한 코드

## 사용한 패턴
#### 1. Singleton Pattern
사용한 부분: 'GameState 클래스'

이유: GameState 클래스는 게임의 상태를 관리하는 클래스이다. 게임 속도와 점수 같은 전역적으로 접근할 수 있는 상태를 유지하기 위해 싱글턴 패턴을 사용. 싱글턴 패턴은 클래스의 인스턴스를 하나만 생성하여 전역적으로 접근할 수 있도록 보장. 이를 통해 여러 객체가 동일한 게임 상태를 공유할 수 있다.

```python
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
```

#### 2. State Pattern
사용한 부분: 'State', 'RunningState', 'JumpingState', 'DuckingState' 클래스

이유: 공룡의 상태(달리기, 점프, 웅크리기)를 관리하기 위해 상태 패턴을 사용. 상태 패턴을 사용하면 객체의 상태에 따라 행동을 변경할 수 있다. 이는 공룡의 상태가 변경될 때마다 상태별 행동(입력 처리 및 업데이트 로직)이 달라지는 것을 쉽게 관리할 수 있도록 한다.

```python
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
```

#### 3.Factory Pattern
사용한 부분: 'ObstacleFactory' 클래스

이유: 장애물 객체를 생성할 때 팩토리 패턴을 사용. 팩토리 패턴은 객체 생성 로직을 캡슐화하여 클라이언트 코드와 객체 생성 코드를 분리한다. 이를 통해 장애물의 종류가 추가되거나 변경될 때 클라이언트 코드를 수정하지 않고도 쉽게 확장할 수 있다.

```python
class ObstacleFactory:
    @staticmethod
    def create_obstacle(obstacle_type):
        if obstacle_type == 'small_cactus':
            return SmallCactus(SMALL_CACTUS)
        elif obstacle_type == 'large_cactus':
            return LargeCactus(LARGE_CACTUS)
        elif obstacle_type == 'bird':
            return Bird(BIRD)
```

#### 오류 사항
현재 게임이 끝났을 때 화면에 띄어지는 Your Score 부분이 계속 0으로 고정이 되는 문제가 있다. [수정 완료]