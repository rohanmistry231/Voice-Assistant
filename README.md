# OWN 1.0 - Personal Voice Assistant

![OWN 1.0 Logo](https://via.placeholder.com/150?text=OWN+1.0) <!-- Replace with actual logo if available -->

OWN 1.0 is a modular, voice-activated personal assistant built in Python, designed to streamline daily tasks through natural language interaction. Inspired by fictional assistants like JARVIS, OWN 1.0 leverages speech recognition, NLP, and API integrations to perform tasks such as opening applications, searching the web, sending emails, setting alarms, and more. This project showcases modern software engineering practices, including modular design, error handling, and NLP integration, making it a standout portfolio piece for an AI/ML fresher.

## Features

- **Voice Interaction**: Uses `pyttsx3` for text-to-speech and `SpeechRecognition` for voice input, enabling seamless user interaction.
- **Natural Language Processing**: Integrates `spaCy` for intent recognition, improving command understanding.
- **Web and App Control**: Opens websites (e.g., Google, YouTube, Netflix) and applications (e.g., VS Code, Notepad) with voice commands.
- **Search Capabilities**: Performs Google, YouTube, and Wikipedia searches using `pywhatkit` and `wikipedia` APIs.
- **Email and Messaging**: Sends emails via Gmail SMTP and WhatsApp messages using `pywhatkit`.
- **System Control**: Manages system volume, locks the device, shuts down, and clears the recycle bin.
- **Productivity Tools**: Sets alarms, takes notes, and remembers user inputs stored in text files.
- **News Updates**: Fetches and reads latest news from various categories using the News API.
- **Mathematical Calculations**: Solves math queries using Wolfram Alpha API.
- **Keyboard Shortcuts**: Executes browser shortcuts (e.g., copy, paste, pause) via `pyautogui`.
- **Extensibility**: Modular architecture allows easy addition of new features.

## Project Structure

```
voice_assistant/
├── config.py               # Configuration and environment variable management
├── app.py                  # Main application logic
├── modules/                # Modular feature implementations
│   ├── chrome_shortcut.py  # Browser shortcut handling
│   ├── search.py           # Web search functionalities
│   ├── apps.py             # Application and website launching
│   ├── keyboard.py         # System keyboard controls
│   ├── news.py             # News fetching and reading
│   ├── calculator.py       # Mathematical calculations
│   ├── whatsapp.py         # WhatsApp messaging
│   ├── alarm.py            # Alarm setting and ringing
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
```

## Installation

### Prerequisites
- Python 3.8+
- A microphone for voice input
- Windows OS (due to `pyttsx3` SAPI5 and system-specific commands)
- API keys for Wolfram Alpha and News API
- Gmail account with app password for email functionality

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rohanmistry231/voice-assistant.git
   cd voice-assistant
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install spaCy Model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Configure Environment Variables**:
   Create a `.env` file in the project root with the following:
   ```env
   WOLFRAM_ALPHA_KEY=your_wolfram_alpha_key
   NEWS_API_KEY=your_news_api_key
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_gmail_app_password
   ```
   - Obtain API keys from [Wolfram Alpha](https://developer.wolframalpha.com/) and [News API](https://newsapi.org/).
   - Generate a Gmail app password at [Google Account Settings](https://myaccount.google.com/security).

6. **Ensure Music File for Alarms**:
   Place a `music.mp3` file in the project root or update `alarm.py` to point to an existing audio file.

7. **Run the Assistant**:
   ```bash
   python app.py
   ```

## Usage

1. **Start the Assistant**: Run `app.py`. The assistant greets you based on the time of day and asks for your name.
2. **Issue Voice Commands**: Speak commands like:
   - "Open YouTube"
   - "Search Google for Python tutorials"
   - "Send an email to mama"
   - "Set an alarm for 10 and 30"
   - "Tell me a joke"
   - "What's the time?"
   - "Volume up"
   - "Show notes"
3. **Exit**: Say "exit" to stop the assistant.

### Example Commands
| Command | Action |
|---------|--------|
| "Open Google" | Opens google.com in the default browser |
| "Search Wikipedia for AI" | Reads a Wikipedia summary about AI |
| "Play song" | Plays an MP3 file from the music directory |
| "Email to user" | Prompts for email content and recipient |
| "Calculate 2 plus 2" | Solves the math query using Wolfram Alpha |
| "News" | Fetches latest news in a chosen category |
| "Remember that meeting at 5 PM" | Saves the reminder to a file |

## Technical Details

### Technologies Used
- **Python Libraries**:
  - `pyttsx3`: Text-to-speech for voice output
  - `SpeechRecognition`: Voice input via Google Speech API
  - `spaCy`: NLP for intent recognition
  - `pywhatkit`: YouTube and WhatsApp automation
  - `wikipedia`: Wikipedia summaries
  - `requests`: API calls for news
  - `wolframalpha`: Mathematical calculations
  - `pyautogui`: Keyboard and mouse automation
  - `pynput`: System volume control
  - `python-dotenv`: Environment variable management
- **APIs**:
  - Wolfram Alpha API
  - News API
- **Other**:
  - Modular architecture with separate modules for each feature
  - Logging for debugging and error tracking
  - Environment variables for secure configuration

### Key Features
- **Modular Design**: Each feature (e.g., search, apps, news) is encapsulated in its own module, enhancing maintainability.
- **NLP Integration**: `spaCy` processes user queries to identify intents (e.g., "open", "search"), improving command accuracy.
- **Error Handling**: Comprehensive try-except blocks and logging ensure robustness.
- **Security**: Sensitive data (API keys, email credentials) are stored in a `.env` file.
- **Performance**: Optimized speech recognition with ambient noise adjustment and timeouts.

## Development Highlights

This project demonstrates skills critical for an AI/ML fresher:
- **AI/ML**: Integration of NLP with `spaCy` for intent recognition, showcasing understanding of natural language processing.
- **Software Engineering**: Modular codebase, logging, and environment variable management reflect professional development practices.
- **API Integration**: Seamless use of external APIs (Wolfram Alpha, News API) for enhanced functionality.
- **Automation**: System control via `pyautogui` and `pynput` demonstrates automation capabilities.
- **User Experience**: Context-aware greetings and clear voice feedback enhance usability.

## Future Enhancements

- **GUI Interface**: Add a Tkinter or PyQt interface for visual interaction.
- **Advanced NLP**: Integrate a transformer model (e.g., BERT) for better intent recognition.
- **Wake Word Detection**: Implement wake-word activation (e.g., "Hey OWN") using Porcupine.
- **Cross-Platform Support**: Adapt for Linux/Mac by replacing Windows-specific commands.
- **Cloud Integration**: Store notes and reminders in a cloud database (e.g., Firebase).
- **Multi-Language Support**: Add support for non-English voice commands.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows PEP 8 guidelines and includes appropriate tests.

## Acknowledgments

- Inspired by fictional assistants like JARVIS from Iron Man.
- Thanks to the open-source community for libraries like `pyttsx3`, `SpeechRecognition`, and `spaCy`.
- Built as a portfolio project to demonstrate AI/ML and software engineering skills.

## Contact

- **Author**: Rohan S. Mistry
- **Email**: rohanmistry231@gmail.com
- **LinkedIn**: [linkedin](https://www.linkedin.com/in/rohan-mistry-493987202/)

Feel free to reach out for collaboration or feedback!

---

*Built with ❤️ by Rohan S. Mistry*