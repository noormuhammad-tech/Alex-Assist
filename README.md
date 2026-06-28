# AlexAssist - Voice Assistant

A Python-based AI voice assistant that listens to your voice, understands commands, and responds using OpenAI GPT. Built as a personal project to learn Python, APIs, and speech recognition.

---

## What It Does

- Wakes up when you say **"Hello"**
- Opens websites like Google, YouTube, Facebook, and Instagram on voice command
- Plays songs from a custom music library
- For any other question or command, it uses **OpenAI GPT-3.5** to give an intelligent reply and speaks it out loud

---

## How It Works

1. Alex continuously listens through your microphone
2. When it hears **"Hello"**, it replies **"Ya"** and starts listening for a command
3. If the command matches a built-in action (open a site, play a song) — it does it
4. If the command is not recognized — it sends it to OpenAI and speaks the AI response
5. AI response is spoken aloud.

---

## Tech Stack

- **Python** — core language
- **SpeechRecognition** — to capture and convert voice to text
- **pyttsx3** — text to speech (Alex speaks back to you)
- **OpenAI API** — GPT-3.5 for intelligent replies
- **webbrowser** — to open websites

---

## Project Structure

```
alex/
│
├── main.py           # Main file — runs Alex
├── musicLibrary.py   # Dictionary of songs and their YouTube links
├── client.py         # Simple OpenAI API test file
├── .gitignore        # Ignores venv and cache files
└── README.md         # This file
```

---

## Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/noormuhammad-tech/alex.git
cd alex
```

**2. Create a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install SpeechRecognition openai pyttsx3
```

**4. Add your OpenAI API key**

Open `main.py` and replace `Your_API_Key_Here` with your actual key:
```python
client = OpenAI(
    api_key="your-real-api-key-here",
)
```

**5. Run the assistant**
```bash
python main.py
```

---

## Voice Commands

| Say This | What Alex Does |
|---|---|
| `Hello` | Wakes up Alex |
| `Open Google` | Opens google.com |
| `Open YouTube` | Opens youtube.com |
| `Open Facebook` | Opens facebook.com |
| `Open Instagram` | Opens instagram.com |
| `Play [song name]` | Plays the song from music library |
| `Anything else` | Asks OpenAI and speaks the answer |

---

## Note

You need a valid **OpenAI API key** to use the AI response feature. Get one at [platform.openai.com](https://platform.openai.com).

---

## Author

**Noor Muhammad**  
BSCS Student  
GitHub: [github.com/noormuhammad-tech](https://github.com/noormuhammad-tech)
