"""
Data Structures & Algorithms

Lab 5: Hash Maps

Entity-Component-System Exercise
"""

from abc import abstractmethod
from collections.abc import Iterator
from time import perf_counter
from typing import TypeAlias
import sys

import pygame

from lib.base import Base

from lab3.core.dynamic_array_list import DynamicArrayList as List
from lab5.core.chaining_hash_map import ChainingHashMap as Map


Entity: TypeAlias = int


class Component(Base):
    pass


class System(Base):
    @abstractmethod
    def process(self, ecs: "ECS", **extra_args) -> None: ...


class ECS(Base):
    _next_entity: Entity
    _entities: List[Entity]
    _components: Map[type[Component], Map[Entity, Component]]
    _systems: List[System]

    def __init__(self) -> None:
        self._next_entity = 0
        self._entities = List()
        self._components = Map()
        self._systems = List()

    def add_new_entity(self) -> Entity:
        entity = self._next_entity
        self._next_entity += 1
        self._entities.insert_last(entity)
        return entity

    def get_entity_count(self) -> int:
        return self._entities.get_length()

    def get_entities(self) -> Iterator[Entity]:
        for entity in self._entities.iterator():
            yield entity

    def get_entities_with_component(self, component_type: type[Component]) -> Iterator[Entity]:
        for entity in self.get_entities():
            if self.has_component(entity, component_type):
                yield entity

    def get_entities_with_components(self, component_types: tuple[type[Component]]) -> Iterator[Entity]:
        for entity in self.get_entities():
            if self.has_components(entity, component_types):
                yield entity

    def _get_entity_index(self, entity: Entity, lower: int, upper: int) -> int:
        if lower > upper:
            raise ValueError
        index = (lower + upper) // 2
        entity_at_index = self._entities.get_at(index)
        if entity < entity_at_index:
            return self._get_entity_index(entity, lower, index - 1)
        if entity > entity_at_index:
            return self._get_entity_index(entity, index + 1, upper)
        return index

    def remove_entity(self, entity: Entity) -> None:
        index = self._get_entity_index(entity, 0, self._entities.get_length() - 1)
        self._entities.remove_at(index)
        for component_map in self._components.values_iterator():
            if component_map.contains(entity):
                component_map.remove(entity)

    def add_component(self, entity: Entity, component: Component) -> None:
        component_type = type(component)
        if self._components.contains(component_type):
            component_map = self._components.get(component_type)
            if component_map.contains(entity):
                raise ValueError
        else:
            component_map = Map()
            self._components.insert(component_type, component_map)
        component_map.insert(entity, component)

    def has_component(self, entity: Entity, component_type: type[Component]) -> None:
        if not self._components.contains(component_type):
            return False
        return self._components.get(component_type).contains(entity)

    def has_components(self, entity: Entity, component_types: tuple[type[Component]]) -> None:
        for component_type in component_types:
            if not self.has_component(entity, component_type):
                return False
        return True

    def get_component(self, entity: Entity, component_type: type[Component]) -> Component:
        if not self._components.contains(component_type):
            raise KeyError
        return self._components.get(component_type).get(entity)

    def get_components(self, component_type: type[Component]) -> Iterator[tuple[Entity, Component]]:
        if self._components.contains(component_type):
            yield from self._components.get(component_type).iterator()

    def remove_component(self, entity: Entity, component_type: type[Component]) -> Component:
        if not self._components.contains(component_type):
            raise KeyError
        return self._components.get(component_type).remove(entity)

    def add_system(self, system: System) -> None:
        self._systems.insert_last(system)

    def get_systems(self) -> List[System]:
        return self._systems

    def process(self, **extra_args) -> None:
        for system in self._systems.iterator():
            system.process(self, **extra_args)


class Game(Base):
    _previous_time: float
    _surface: pygame.Surface
    _ecs: ECS

    def __init__(self, width: int, height: int) -> None:
        self._surface = pygame.display.set_mode(size=(width, height))
        self._ecs = ECS()

    def run(self) -> None:
        surface = self._surface
        self._previous_time = perf_counter()
        while True:
            time = perf_counter()
            delta_time = time - self._previous_time
            events = List.build(pygame.event.get())
            width = surface.get_width()
            height = surface.get_height()
            self._ecs.process(
                delta_time=delta_time,
                events=events,
                surface=self._surface,
                width=width,
                height=height,
            )
            pygame.display.flip()
            self._previous_time = time


class Size(Component):
    _width: float
    _height: float

    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height


class Position(Component):
    _x: float
    _y: float

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y


class Velocity(Component):
    _x: float
    _y: float

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y


class Ball(Component):
    pass


class Paddle(Component):
    pass


class SideWall(Component):
    pass


KeyCode: TypeAlias = int


class Controls(Component):
    _up: KeyCode
    _down: KeyCode

    def __init__(self, up: KeyCode, down: KeyCode) -> None:
        self._up = up
        self._down = down

    def get_up(self) -> KeyCode:
        return self._up

    def get_down(self) -> KeyCode:
        return self._down


class Quitting(System):
    def process(self, ecs: ECS, events: List[pygame.event.Event], **extra_args) -> None:
        for event in events.iterator():
            if event.type == pygame.QUIT:
                sys.exit()


class Clearing(System):
    def process(self, ecs: ECS, surface: pygame.Surface, **extra_args) -> None:
        surface.fill((0, 0, 0))


class Moving(System):
    def process(self, ecs: ECS, delta_time: float, **extra_args) -> None:
        for entity in ecs.get_entities_with_components((Position, Velocity)):
            position = ecs.get_component(entity, Position)
            velocity = ecs.get_component(entity, Velocity)
            position.set_x(position.get_x() + velocity.get_x() * delta_time)
            position.set_y(position.get_y() + velocity.get_y() * delta_time)


class Bouncing(System):
    def process(self, ecs: ECS, **extra_args) -> None:
        for ball in ecs.get_entities_with_component(Ball):
            ball_position = ecs.get_component(ball, Position)
            ball_velocity = ecs.get_component(ball, Velocity)
            ball_size = ecs.get_component(ball, Size)
            ball_x = ball_position.get_x()
            ball_y = ball_position.get_y()
            ball_w = ball_size.get_width()
            ball_h = ball_size.get_height()
            ball_w2 = ball_w / 2
            ball_h2 = ball_h / 2
            ball_l = ball_x - ball_w2
            ball_r = ball_x + ball_w2
            ball_t = ball_y - ball_h2
            ball_b = ball_y + ball_h2
            for paddle in ecs.get_entities_with_component(Paddle):
                paddle_position = ecs.get_component(paddle, Position)
                paddle_size = ecs.get_component(paddle, Size)
                paddle_x = paddle_position.get_x()
                paddle_y = paddle_position.get_y()
                paddle_w = paddle_size.get_width()
                paddle_h = paddle_size.get_height()
                paddle_w2 = paddle_w / 2
                paddle_h2 = paddle_h / 2
                paddle_l = paddle_x - paddle_w2
                paddle_r = paddle_x + paddle_w2
                paddle_t = paddle_y - paddle_h2
                paddle_b = paddle_y + paddle_h2
                if ball_r < paddle_l or ball_l > paddle_r:
                    continue
                if ball_b < paddle_t or ball_t > paddle_b:
                    continue
                ball_velocity.set_x(-ball_velocity.get_x())
            for wall in ecs.get_entities_with_component(SideWall):
                wall_position = ecs.get_component(wall, Position)
                wall_size = ecs.get_component(wall, Size)
                wall_y = wall_position.get_y()
                wall_h = wall_size.get_height()
                wall_h2 = wall_h / 2
                wall_t = wall_y - wall_h2
                wall_b = wall_y + wall_h2
                if ball_b < wall_t or ball_t > wall_b:
                    continue
                ball_velocity.set_y(-ball_velocity.get_y())


class Controlling(System):
    def process(self, ecs: ECS, **extra_args) -> None:
        pressed = pygame.key.get_pressed()
        speed = 240
        for entity in ecs.get_entities_with_component(Controls):
            controls = ecs.get_component(entity, Controls)
            velocity = ecs.get_component(entity, Velocity)
            up = controls.get_up()
            down = controls.get_down()
            dy = 0
            if pressed[up]:
                dy -= speed
            if pressed[down]:
                dy += speed
            velocity.set_y(dy)


class Resetting(System):
    def process(self, ecs: ECS, width: int, height: int, **extra_args) -> None:
        for ball in ecs.get_entities_with_component(Ball):
            ball_position = ecs.get_component(ball, Position)
            ball_size = ecs.get_component(ball, Size)
            ball_x = ball_position.get_x()
            ball_w = ball_size.get_width()
            ball_w2 = ball_w / 2
            ball_l = ball_x - ball_w2
            ball_r = ball_x + ball_w2
            if ball_r < 0 or ball_l > width:
                ball_position.set_x(width / 2)
                ball_position.set_y(height / 2)


class Clamping(System):
    def process(self, ecs: ECS, height: int, **extra_args) -> None:
        for paddle in ecs.get_entities_with_component(Paddle):
            paddle_position = ecs.get_component(paddle, Position)
            paddle_size = ecs.get_component(paddle, Size)
            paddle_y = paddle_position.get_y()
            paddle_h = paddle_size.get_height()
            paddle_h2 = paddle_h / 2
            paddle_t = paddle_y - paddle_h2
            paddle_b = paddle_y + paddle_h2
            for wall in ecs.get_entities_with_component(SideWall):
                wall_position = ecs.get_component(wall, Position)
                wall_size = ecs.get_component(wall, Size)
                wall_y = wall_position.get_y()
                wall_h = wall_size.get_height()
                wall_h2 = wall_h / 2
                wall_t = wall_y - wall_h2
                wall_b = wall_y + wall_h2
                if wall_y < height / 2:
                    if paddle_t < wall_b:
                        paddle_position.set_y(wall_b + paddle_h2)
                else:
                    if paddle_b > wall_t:
                        paddle_position.set_y(wall_t - paddle_h2)


class Rendering(System):
    def process(self, ecs: ECS, surface: pygame.Surface, **extra_args) -> None:
        for entity in ecs.get_entities_with_components((Position, Size)):
            position = ecs.get_component(entity, Position)
            size = ecs.get_component(entity, Size)
            w = size.get_width()
            h = size.get_height()
            l = position.get_x() - w / 2
            t = position.get_y() - h / 2
            pygame.draw.rect(surface, (255, 255, 255), (l, t, w, h))


class Pong(Game):
    def __init__(self):
        width = 640
        height = 480
        super().__init__(width, height)
        wall_thickness = 30
        top_wall = self._ecs.add_new_entity()
        self._ecs.add_component(top_wall, Size(width, wall_thickness))
        self._ecs.add_component(top_wall, Position(width / 2, wall_thickness / 2))
        self._ecs.add_component(top_wall, SideWall())
        bottom_wall = self._ecs.add_new_entity()
        self._ecs.add_component(bottom_wall, Size(width, wall_thickness))
        self._ecs.add_component(bottom_wall, Position(width / 2, height - wall_thickness / 2))
        self._ecs.add_component(bottom_wall, SideWall())
        paddle_width = 20
        paddle_height = 80
        paddle_offset = 40
        left_paddle = self._ecs.add_new_entity()
        self._ecs.add_component(left_paddle, Size(paddle_width, paddle_height))
        self._ecs.add_component(left_paddle, Position(paddle_offset, height / 2))
        self._ecs.add_component(left_paddle, Velocity(0, 0))
        self._ecs.add_component(left_paddle, Paddle())
        # self._ecs.add_component(left_paddle, Controls(pygame.K_COMMA, pygame.K_o))  # dvorak
        self._ecs.add_component(left_paddle, Controls(pygame.K_w, pygame.K_s))  # qwerty
        right_paddle = self._ecs.add_new_entity()
        self._ecs.add_component(right_paddle, Size(paddle_width, paddle_height))
        self._ecs.add_component(right_paddle, Position(width - paddle_offset, height / 2))
        self._ecs.add_component(right_paddle, Velocity(0, 0))
        self._ecs.add_component(right_paddle, Paddle())
        self._ecs.add_component(right_paddle, Controls(pygame.K_UP, pygame.K_DOWN))
        ball_size = 20
        ball = self._ecs.add_new_entity()
        self._ecs.add_component(ball, Size(ball_size, ball_size))
        self._ecs.add_component(ball, Position(width / 2, height / 2))
        self._ecs.add_component(ball, Velocity(140, 120))
        self._ecs.add_component(ball, Ball())
        self._ecs.add_system(Quitting())
        self._ecs.add_system(Clearing())
        self._ecs.add_system(Moving())
        self._ecs.add_system(Bouncing())
        self._ecs.add_system(Controlling())
        self._ecs.add_system(Resetting())
        self._ecs.add_system(Clamping())
        self._ecs.add_system(Rendering())
