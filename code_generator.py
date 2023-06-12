import openai
import openai.error
import time
import pywinauto
from pywinauto import keyboard, Application
import webbrowser
import os
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def searchForProgram(program_name):
    keyboard.send_keys("{VK_LWIN down}{VK_LWIN up}")
    time.sleep(1)
    keyboard.send_keys(program_name,with_spaces=True)
    keyboard.send_keys("{ENTER}")

def requestCode(instruction):
  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      temperature = 0.2,
      messages=[
        {"role": "system", "content": """
        You are a computer assistant that will automate voice commands from the user.
        Your task is to write Python code that carries out user's request.
        You have access to Python and are capable of interacting with browsers and the Windows environmnt with following libraries: webbrowser, pywinauto.
        When using pywinauto, always pass with_spaces=True to the type_keys function when you type.
        If you need to open a program, use the function searchForProgram(program_name).
        Remember that opening windows or programs takes time, so you should include a small with time.sleep(seconds) of no more than 2 seconds.
        Do not close windows or programs unless explicitly told to do so.
        IMPORATNT: You do not need to import the Python libraries.
        IMPORTANT: You must only respond with executable Python code.
        IMPORTANT: Do not add comments.

        From here on is the user's request:
        """},
        {"role":"user", "content": "I want to "+instruction}
      ],
      max_tokens = 200
    )
  except openai.error.RateLimitError:
     return "The API could not respond (Rate Limit Error)"
  text_response = response.choices[0].message.content
  return text_response

import sys

if __name__ == "__main__":
    command = requestCode(sys.argv[1])
    print(command)
    exec(command)
