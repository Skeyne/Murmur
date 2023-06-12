import speech_recognition as sr
import os
import webbrowser
import openai
import time
import pywinauto
import pyautogui
from pywinauto import keyboard, Application
import os
import dotenv
from code_generator import requestCode, searchForProgram
from hotword_detection import Hotpocket
from typing import Callable

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Murmur:
    def __init__(self,keywords,speech_model="whisper-1") -> None:
        self.keywords = keywords
        self.hotpocket = Hotpocket(self.keywords)
        self.recogizer = sr.Recognizer()
        self.speech_model = speech_model

    def calibrate(self) -> None:
        print(":::Calibrating:::")
        with sr.Microphone() as source:
            self.recogizer.energy_threshold = 80
            self.recogizer.dynamic_energy_threshold = False
        print(":::Done:::")

    def listen(self) -> sr.AudioData:
        with sr.Microphone() as source:
            audio = self.recogizer.listen(source,timeout=10)
        return audio

    def start(self,log_callback:Callable[[str],None]) -> None:
        while True:
            log_callback(":::Waiting for wake word:::")
            print(":::Waiting for wake word:::")
            self.hotpocket.detect()
            log_callback(":::Listening for instructions:::")
            print(":::Listening for instructions:::")
            audio = self.listen()
            log_callback(":::Recognizing...:::")
            print(":::Recognizing...:::")
            command = self.recogizer.recognize_whisper_api(
                audio,
                model=self.speech_model,
                api_key=os.getenv("OPENAI_API_KEY"))
            if "stop" in command.lower():
                break
            log_callback(command)
            response = requestCode(command)
            try:
                exec(response)
            except Exception as e:

                print("The response code:",response,"caused the error:",e)

        log_callback("Done!")
        time.sleep(1)