# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/README.md))

### [Entity-Component-System](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/ecs/README.md)
```shell
pip install pygame
python labs ecs
```

Games are often programmed in a style known as ECS, short for Entity-Component-System.

Essentially, ECS is an alternative to e.g. OOP (Object-Oriented Programming), and though it's a concept/approach that
could be used more generally, the vast majority of ECS's use is in game development.

ECS, as you might guess, involves three main things: entities, components, and systems.

An "entity" identifies a particular _thing_, such as a player, an enemy, or a tree. (Or other, less visible / more
abstract things too, but we're not going to discuss them - or various other points - as we're only explaining just
enough of these topics to help you make sense of the examples, and perhaps to whet your appetite enough that you go off
and learn about them properly.)

A "component" is an aspect of a thing, such as its position or velocity.

A "system" is a behaviour that things with certain aspects have - for example, how things with both a position and a
velocity change their position based on that velocity.

Put another way: entities are identifiers, components are data, systems are code.

In this example, we've implemented a very simple Pong clone using ECS. The important thing is to see how the basic ECS
framework works - particularly, how it stores entities' components. You'll notice that it's a map of maps,
`Map[type[Component], Map[Entity, Component]]`: For a given component type (the syntax `type[Component]` just means a
type that extends `Component`), it stores a map that associates entities and their components of that type. If the
component type is `Position`, then the `Map[Entity, Component]` will more specifically be a `Map[Entity, Position]`
(effectively - though we can't properly express this in the type system, as Python doesn't have "dependent types"...
though nor, for that matter, do many languages), and will tell us both which entities have positions (by which entities
are keys in the map), and what those positions are (by what values those keys map to).

It's not important for understanding its use of maps, but you may want to _run_ this example - to do that, first run
```shell
pip install pygame
```
then just run
```shell
python labs ecs
```

The controls are `W` & `A` and `Up` & `Down`.

Note that this is a very basic, even slightly buggy clone, as it's just supposed to be a very minimal example to help
illustrate what entities, components and systems are. Admittedly though, ECS really comes into its own for larger
projects, so if you think this all seems a little overcomplicated, you're probably right that it's over-the-top for a
simple Pong clone, but don't dismiss it based on that! Another thing to note, if you get into ECS, is that not everyone
implements it in exactly the same way, and you will likely encounter different ECS frameworks that do it somewhat
differently - the basic idea, though, remains largely the same.

---

Next:
- [Linkers](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/linker/README.md)
