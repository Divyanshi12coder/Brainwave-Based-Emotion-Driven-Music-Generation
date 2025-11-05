# src/music_gen/music_generator.py
from midiutil import MIDIFile

def generate_music(emotion):
    tempo_map = {"happy": 140, "sad": 60, "calm": 90, "angry": 150}
    key_map = {"happy": 60, "sad": 48, "calm": 55, "angry": 50}

    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo_map.get(emotion, 100))

    for i in range(8):
        midi.addNote(0, 0, key_map.get(emotion, 60), i, 1, 100)

    with open(f"music/{emotion}_track.mid", "wb") as f:
        midi.writeFile(f)
    return f"music/{emotion}_track.mid"