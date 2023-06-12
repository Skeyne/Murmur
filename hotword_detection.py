import pvporcupine
import pyaudio
import struct
import dotenv
import os

dotenv.load_dotenv()

ACCESS_KEY= os.getenv("PORCUPINE_KEY")

class Hotpocket:
    def __init__(self,keywords) -> None:
        self.handle = pvporcupine.create(access_key=ACCESS_KEY, keywords=['computer'])
        self.py_audio = pyaudio.PyAudio()


    def detect(self) -> bool:
        audio_stream = self.py_audio.open(self.handle.sample_rate,1,pyaudio.paInt16,True,frames_per_buffer=self.handle.frame_length)
        while True:
            try:
                snippet = audio_stream.read(self.handle.frame_length)
                snippet = struct.unpack_from("h" * self.handle.frame_length, snippet)
                if self.handle.process(snippet) > -1:
                    return True  
            except KeyboardInterrupt:
                return False
    def close(self) -> None:
        self.handle.delete()