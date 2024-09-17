# Remote Piano Teacher

This project is a comprehensive software system designed to facilitate real-time remote piano teaching and learning through the use of MIDI-connected keyboards and programmable LED strips.

## Features

- Real-time MIDI note transmission between teacher and student
- LED strip integration for visual key highlighting
- Teaching mode: Teacher's played notes are visualized on student's LED strip
- Learning mode: Load MIDI files or custom note sequences for practice
- Adjustable tempo and looping sections
- Bidirectional note visualization
- Low-latency communication for smooth learning experience

## System Requirements

- MIDI-compatible keyboard
- Programmable LED strip (compatible with rpi_ws281x library)
- Python 3.7+
- Raspberry Pi (for LED strip control)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/RemotePianoTeacher.git
   cd RemotePianoTeacher
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the settings in `config.py` to match your MIDI devices and LED strip setup.

## Usage

1. Ensure your MIDI keyboard is connected and the LED strip is properly set up.

2. Run the main script:
   ```
   python main.py
   ```

3. Choose the mode:
   - Enter 'teach' for teaching mode
   - Enter 'learn' for learning mode

4. Follow the on-screen instructions for each mode.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.