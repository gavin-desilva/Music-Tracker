class MusicTracker:
    def __init__(self):
        self.tracklist = []

    def view_tracks(self):
        return self.tracklist

    def add(self, track):
        if track == "" or track == None:
            raise Exception("No track given")
        if " - " not in track:
            raise Exception("Input is not in valid track format")
        self.tracklist.append(track)