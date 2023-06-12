# Murmur
A desktop assistant powered by GPT-3.5 and the Whisper APIs

## Getting started
Clone this repo
```bash
git clone https://github.com/Skeyne/Murmur.git
```
Install dependencies (Recommend using Python 3.11)
```bash
pip install -r requirements.txt
```
Get free a picovoice.ai access key: https://picovoice.ai/platform/porcupine/

Get an OpenAI API key (not free): https://platform.openai.com/

Create a .env file and add the keys:
```
PORCUPINE_KEY={YOUR_PICOVOICE_ACCESS_KEY}
OPENAI_API_KEY={YOUR_OPENAI_ACCESS_KEY}
```
## Usage
Start the application
```bash
python app.py
```
A GUI will appear on the left showing the assistant's actions.

Use the wakeword "computer" to start a command, then give it a natural instruction like "Open Youtube". If the assistant fails to carry out the task the attempted action will be logged to the console.

## Current features
- Very good at opening websites
- Can open programs searchable with the windows menu (e.g. Open Word)
- Can close windows although doesn't always succeed
- A lot more untested things as GPT-3.5 generates all the code. These are only the confirmed use cases.

## TODO
- Give it access to better libraries for manipulation of browser windows (Selenium?)
- Implement a skill library (Inspred by https://voyager.minedojo.org/)
- Improve UI feedback
- More wakewords for improved functionality and learning (e.g. retry -> send back failed code and user feedback) second point contigent on skill library implemention
