# Heading 1
## Heading 2
Some content?
## Another heading 2
Some more content

```python
def some_function():
  return "wow!"
```

```javascript
  const someFunction = () => {
    return "hello";
  }
```


```mermaid
classDiagram
        class `Class` {
          - str location
          - str name
          + get_location()
          + get_name()
        }
        class Student {
            - str name
            - str number
            - str email
            + attend_class()
        }
        `Class` o-- "*..*" Student : has_and_belongs_to_many
```

```mermaid
classDiagram
        class Animal {
            - int age
            
            + eat()
            + move()
        }


```

```mermaid

classDiagram

   class Bookstore {

       + str name

       + str address

       + dict[str, str] inventory
       + List[str] staff
       + shelfs
       - addBook()
       - removeBook()
       - sellBook()
       - checkInventory()
   }

    class Books {
       + str title
       + str author
       + str number
       + str genre
       + float price 
       + int stock
       + getDetails()
       + updateStock()
   }

   class employees {
       + str name
       + str number
       + str email
       + str jobTitle
       + float salary

       - did_shift()
       + clockIn()
       + clockOut()
       + sellBook()
       + assistCustomer()
   }



   Bookstore "1" -- "*" Books : has
   Bookstore "1" -- "*" employees : employs
   Bookstore "1" -- "*" shelfs : has
   employees "1" -- "*" Books : sells


```


```mermaid
classDiagram
    class Movie {
        - str name
        - float length
        + get_name()
        + get_actors()
    }

    class Actors {
        - str name
        - int age
        + get_actor_movies()
    }

    class Directors {
        - str name
        - int age
        + get_director_movies()
    }

    Movie "*" -- "*" Actors : belongs_to_and_has_many
    Movie "*" -- "1" Directors : has_one
    Actors "1" -- "1" Directors : can_be
```