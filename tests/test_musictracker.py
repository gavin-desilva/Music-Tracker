import pytest
from lib.musictracker import *

def test_intialising_musictracker_creates_empty_list():
    tracker = MusicTracker()
    assert tracker.view_tracks() == []

def test_invalid_string_format():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add("Hello Adele")
    error_message = str(e.value)
    assert error_message == "Input is not in valid track format"

def test_single_valid_string_input():
    tracker = MusicTracker()
    tracker.add("Baby - Justin Bieber")
    assert tracker.view_tracks() == ["Baby - Justin Bieber"]

def test_empty_string():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add("")
    error_message = str(e.value)
    assert error_message == "No track given"

def test_multiple_valid_strings_input():
    tracker = MusicTracker()
    tracker.add("Baby - Justin Bieber")
    tracker.add("Call Me Maybe - Carly Rae Jepsen")
    tracker.add("Gangnam Style - PSY")
    assert tracker.view_tracks() == [
        "Baby - Justin Bieber",
        "Call Me Maybe - Carly Rae Jepsen",
        "Gangnam Style - PSY"
    ]