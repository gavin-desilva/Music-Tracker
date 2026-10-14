## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._
```python
# EXAMPLE

class MusicTracker:

    def __init__(self):
        self.tracklist = []
        # Parameters:
        #   none
        # Side effects:
        pass#   Creates an empty list for song names
      
    def add(self, track):
        # Parameters:
        #   track: string representing a single song
        # Returns:
        #   Nothing
        # Side-effects
        #   Appends track to tracklist
        pass # No code here yet

    def view_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   Tracklist as a list
        # Side-effects
        #   None
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE
"""
Initialising class and calling view_tracks function returns a blank tracklist list. 
"""
tracker = MusicTracker()
assert tracker.view_tracks() == []

"""
Given an invalid string input, where there is no "-" to separate the artist and track name, an exception is raised
"""
tracker = MusicTracker()
tracker.add("Hello Adele") # raises an error with the message "Input is not in valid track format"

"""
Given an empty track, an exception is raised
"""
tracker = MusicTracker()
tracker.add("") # raises an error with the message "No track given"    

"""
Given a non-string input, an exception is raised
"""
tracker = MusicTracker()
tracker.add(400) # raises an error with the message "Input is not a string"

"""
Given a valid single string input, the add function adds the string to the tracklist list
"""
tracker = MusicTracker()
tracker.add("Baby - Justin Bieber")
assert tracker.view_tracks() == ["Baby - Justin Bieber"]

"""

"""
"""
Adding multiple valid strings then calling the view_tracks function, it returns the tracklist list in the order the tracks were added
"""
tracker = MusicTracker()
tracker.add("Baby - Justin Bieber")
tracker.add("Call Me Maybe - Carly Rae Jepsen")
tracker.add("Gangnam Style - PSY")
assert tracker.view_tracks() == [
    "Baby - Justin Bieber",
    "Call Me Maybe - Carly Rae Jepsen",
    "Gangnam Style - PSY"
]

#_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
