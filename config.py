# Configuration settings for RemotePianoTeacher

# MIDI settings
MIDI_INPUT_DEVICE = "Your MIDI Input Device Name"
MIDI_OUTPUT_DEVICE = "Your MIDI Output Device Name"

# LED strip settings
LED_COUNT = 88  # Number of LEDs in the strip (88 for a full-size piano)
LED_PIN = 18    # GPIO pin connected to the LED strip
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest

# Networking settings
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5000

# Color settings
NOTE_COLORS = {
    'C': (255, 0, 0),    # Red
    'D': (255, 127, 0),  # Orange
    'E': (255, 255, 0),  # Yellow
    'F': (0, 255, 0),    # Green
    'G': (0, 0, 255),    # Blue
    'A': (75, 0, 130),   # Indigo
    'B': (143, 0, 255)   # Violet
}

# Learning mode settings
DEFAULT_TEMPO = 120  # Default tempo in BPM
MAX_TEMPO = 240      # Maximum allowed tempo
MIN_TEMPO = 40       # Minimum allowed tempo

# Visualization settings
NOTE_FADE_DURATION = 0.5  # Duration of note fade effect in seconds