# Composition

A composition relationship is a type of aggregation where the contained object cannot exist independently of the containing object. In other words, the contained object is dependent on the containing object and will be destroyed when the containing object is destroyed.

In UML, a composition relationship is represented by a filled diamond shape pointing to the containing object.

## UML Example

```mermaid
classDiagram
    class House {
        +String address
        +addRoom(Room)
    }
    class Room {
        +String name
        +double area
    }
    House *-- "1..*" Room : consists of

```

## Python Implementation

```python
# room.py
...
# house.py
...

# main.py
from house import House
...
```
