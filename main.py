from datetime import datetime  # For current date and time
import os
import time  # To add delays in code
import asyncio  # To get current information from certain packages

import tkinter as tk  # For GUI
import speech_recognition as sr  # To get voice input
from gtts import gTTS  # To convert text to speech
from playsound import playsound  # To play audio files
import pywhatkit  # To run certain tasks
import python_weather  # For current weather
import webbrowser  # To open URLs
from AppOpener import open, close, give_appnames  # To open Apps

class VirtualAssistant:
    """Main Class.

    Attributes:
        recorder (Recognizer): Voice recognizer.
        current_time (str): Current date and time formatted as '%I:%M %p'.
        mic_gui (MicGUI): Reference to the MicGUI Class.
    """
    def __init__(self, mic_gui):
        """Initialize the VirtualAssistant.

        Args:
            mic_gui (MicGUI): Reference to the MicGUI Class.
        """
        self.recorder = sr.Recognizer()  
        self.current_time = datetime.now().strftime("%I:%M %p")
        self.mic_gui = mic_gui

    def get_speech(self, text):
        """Convert text to speech and play the audio.

        Args:
            text (str): Text to be converted to speech.
        """
        print(text)
        lang = "en"  
        for i in range(3):  
            output = gTTS(text=text, lang=lang, slow=False)
            file_name = f"hello{i}.mp3"
            output.save(file_name)
            playsound(file_name, True)
            os.remove(file_name)  

    def get_audio(self):
        """Record audio using the microphone and convert it to text.

        Returns:
            str: Recognized text from the audio.
        """
        with sr.Microphone() as source:  
            print("Speak....")
            audio = self.recorder.listen(source)  
        text = self.recorder.recognize_google(audio)  
        return text

    def run(self):
        """Main method to handle voice commands."""
        text = self.get_audio()

        if "introduce" in text.lower():
            self.handle_introduction(text)
        elif "time" in text.lower():
            self.get_speech(f"The current time is {self.current_time}")
        elif "youtube" in text.lower():
            self.handle_youtube(text)
        elif "search" in text.lower():
            self.handle_search(text)
        elif "github" in text.lower():
            self.handle_github(text)
        elif "message" in text.lower():
            self.handle_message(text)
        elif "open" in text.lower():
            self.handle_open_app(text)
        elif "weather" in text.lower():
            text = text[8:]
            self.handle_weather(text)
        elif "present" in text.lower():
            self.handle_presentation()
        elif "wiki" in text.lower():
            text = text[4:]
            self.handle_wiki(text)
        else:
            self.handle_error()

    def handle_introduction(self, text):
        """Handle introduction in different languages.

        Args:
            text (str): The user's voice command.
        """
        languages = ["english", "chinese", "arabic", "urdu", "french"]
        for lang in languages:
            if lang in text.lower():
                playsound(f"./sounds/intro_{lang}.mp3")

    def handle_youtube(self, text):
        """Play a YouTube video.

        Args:
            text (str): The user's voice command.
        """
        text = text.replace("youtube", "").strip()
        self.get_speech(f"Playing {text} on YouTube")
        pywhatkit.playonyt(text)

    def handle_search(self, text):
        """Search on Google.

        Args:
            text (str): The user's voice command.
        """
        text = text.replace("search", "").strip()
        pywhatkit.search(text)
        self.get_speech(f"Searching {text} on Google")

    def handle_github(self, text):
        """Open GitHub page.

        Args:
            text (str): The user's voice command.
        """
        webbrowser.open(f'http://github.com/{text[7:]}')
        playsound("./sounds/github.mp3")

    def handle_message(self, text): # Must be logged into Web Whatsapp
        """Send a WhatsApp message.

        Args:
            text (str): The user's voice command.
        """
        text = text.replace("message", "").strip()
        pywhatkit.sendwhatmsg_instantly("add number in this format '+COUNTRYCODE0000000000'", text, 15, True, 4)
        self.get_speech("Message sent successfully")

    def handle_open_app(self, text):
        """Open an application.

        Args:
            text (str): The user's voice command.
        """
        open(text[4:], match_closest=True)
        self.get_speech(f"Opening {text[4:]}")

    def handle_error(self):
        """Handle errors."""
        print("Sorry, but I am unable to assist you with this problem")
        playsound("./sounds/error.mp3")

    def handle_weather(self, text):
        """Fetch weather information using python_weather library.

        Args:
            text (str): The user's voice command.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._handle_weather_async(text))

    def handle_wiki(self, text):
        """Get information from Wikipedia.

        Args:
            text (str): The user's voice command.
        """
        self.get_speech(pywhatkit.info(text, 1, True))

    async def _handle_weather_async(self, text):
        """Asynchronously fetch weather information.

        Args:
            text (str): The user's voice command.
        """
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get(text)
            current_temperature = weather.current.temperature
            self.get_speech(f"The current weather in {text} is {current_temperature} degrees Celsius.")

    def handle_presentation(self):
        """For Class Presentations."""
        playsound("./sounds/introductionPresent1.mp3")
        playsound("./sounds/introductionPresent1.5.mp3")
        playsound("./sounds/introductionPresent2.mp3")
        playsound("./sounds/introductionPresent3.mp3")
        self.get_speech(f"" + self.current_time +
                        " also, if you are wondering why I sound like this now, it's because I require too much CPU usage, "
                        "anyways back to the time")
        playsound("./sounds/introductionPresent6.mp3")
        pywhatkit.search("Time in Oakville")
        playsound("./sounds/introductionPresent7.mp3")
        time.sleep(1.5)
        pywhatkit.playonyt("David Debono Music")
        time.sleep(10)
        playsound("./sounds/introductionPresent8.mp3")
        playsound("./sounds/outroPresent.mp3")

class MicGUI:
    """Class representing the Mic Icon GUI.

    Attributes:
        root (tk.Tk): The root window.
        assistant (VirtualAssistant): Reference to the VirtualAssistant.
        mic_icon_normal (tk.PhotoImage): Mic icon image.
        mic_icon_clicked (tk.PhotoImage): Active mic icon image.
        background_image (tk.PhotoImage): Background image for the canvas.
        canvas (tk.Canvas): GUI canvas for displaying images.
        mic_item (int): ID of the mic item on the canvas.
    """
    def __init__(self, assistant, root):
        """Initialize the MicGUI.

        Args:
            assistant (VirtualAssistant): Reference to the VirtualAssistant.
            root (tk.Tk): The root window.
        """
        self.root = root
        self.root.title("Mic Icon GUI")  

        self.assistant = assistant  

        self.mic_icon_normal = tk.PhotoImage(file="./images/mic_icon.png")
        self.mic_icon_clicked = tk.PhotoImage(file="./images/mic_active_icon.png")

        self.background_image = tk.PhotoImage(file="./images/background.png")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.canvas.create_image(400, 300, image=self.background_image, anchor=tk.CENTER)
        self.mic_item = self.canvas.create_image(400, 300, image=self.mic_icon_normal, anchor=tk.CENTER)

        self.canvas.tag_bind(self.mic_item, '<Button-1>', self.toggle_mic_icon)

    def toggle_mic_icon(self, event):
        """Toggle the mic icon state on click.

        Args:
            event: The click event.
        """
        self.assistant.run()

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    root = tk.Tk()
    assistant = VirtualAssistant(None)
    mic_gui = MicGUI(assistant, root)
    assistant.mic_gui = mic_gui
    root.mainloop()
