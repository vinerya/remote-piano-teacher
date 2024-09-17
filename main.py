import asyncio
import midi_handler
import led_controller
import network_sync
import config

class RemotePianoTeacher:
    def __init__(self):
        self.midi_handler = midi_handler.MIDIHandler()
        self.led_controller = led_controller.LEDController()
        self.network_sync = network_sync.NetworkSync()

    async def run_teaching_mode(self):
        print("Running in teaching mode...")
        await self.network_sync.start_server(config.DEFAULT_HOST, config.DEFAULT_PORT)
        while True:
            midi_data = self.midi_handler.read_midi_input()
            if midi_data:
                self.led_controller.light_key(midi_data.note, config.NOTE_COLORS[midi_data.note % 7])
                await self.network_sync.send_data(midi_data)

    async def run_learning_mode(self):
        print("Running in learning mode...")
        await self.network_sync.connect_to_server(config.DEFAULT_HOST, config.DEFAULT_PORT)
        while True:
            midi_data = await self.network_sync.receive_data()
            if midi_data:
                self.led_controller.light_key(midi_data.note, config.NOTE_COLORS[midi_data.note % 7])
                self.midi_handler.send_midi_output(midi_data)

    async def main_loop(self):
        mode = input("Enter mode (teach/learn): ").lower()
        if mode == "teach":
            await self.run_teaching_mode()
        elif mode == "learn":
            await self.run_learning_mode()
        else:
            print("Invalid mode. Please choose 'teach' or 'learn'.")

if __name__ == "__main__":
    app = RemotePianoTeacher()
    asyncio.run(app.main_loop())