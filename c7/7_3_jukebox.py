import pytest
from queue import Queue, Empty
import threading
import time


class Song:
    def __init__(self, title):
        self.title = title

    def play(self):
        return "Playing {}".format(self.title)


class Jukebox(threading.Thread):
    def __init__(self):
        super().__init__()
        self.playlist = Queue()
        self.songs = {
            'A': Song('A'),
            'B': Song('B'),
            'C': Song('C')
        }
        self.credit_lock = threading.Lock()
        self.credit = 0
        self.output_lock = threading.Lock()
        self.output = []
        self.running = False

    def _write_output(self, s):
        with self.output_lock:
            self.output.append(s)

    def run(self):
        self.running = True
        while self.running:
            try:
                song = self.playlist.get(block=True, timeout=0.2)
                self._write_output(song.play())
            except Empty:
                pass

    def stop(self):
        self.running = False

    def insert_coin(self):
        with self.credit_lock:
            self.credit += 1

    def get_songs(self):
        return list(self.songs.keys())

    def play_song(self, title):
        with self.credit_lock:
            if self.credit > 0:
                self.playlist.put(self.songs[title])
                self.credit -= 1
                return True
            else:
                return False


def test_solution():
    jb = Jukebox()
    jb.start()

    songs = jb.get_songs()
    assert not jb.play_song(songs[0])
    jb.insert_coin()
    jb.insert_coin()
    jb.insert_coin()
    assert jb.play_song(songs[2])
    assert jb.play_song(songs[1])
    assert jb.play_song(songs[0])
    assert not jb.play_song(songs[1])

    # wait for songs to finish
    time.sleep(0.1)
    jb.stop()

    print(jb.output)
    assert jb.output == [
        "Playing C",
        "Playing B",
        "Playing A",
    ]




if __name__ == '__main__':
    pytest.main(args=[__file__])
