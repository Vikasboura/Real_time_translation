🎤 Real-Time Translator for Video Conferencing 🌐


A standalone Python application that provides live, two-way voice translation during video calls on platforms like Zoom and Google Meet.

This tool acts as your personal, real-time interpreter. It allows you to understand meetings in a foreign language and speak back in your own language, breaking down communication barriers instantly.

📋 Table of Contents
How It Works

Live Demo

✨ Key Features

🛠️ Required Software

⚙️ Installation & Setup

▶️ How to Use

🤔 Troubleshooting

🔮 Future Work

How It Works
The application uses a Virtual Audio Cable to create a seamless audio loop. The process is slightly different for listening versus speaking.

Listening Mode (Translating for YOU)
1. Zoom/Meet Audio           -->   2. CABLE Input (Virtual Speaker)
     |                                      |
     | (Audio Sent to Cable)                | (Script is Listening Here)
     V                                      V
4. Your Headphones/Speakers   <--   3. Python Script (Translates & Speaks)
     ^                                      ^
     | (Translated Audio Played)            |
     |______________________________________|

Speaking Mode (Translating YOUR Voice)
1. Your Real Microphone       -->   2. Python Script (Listens & Translates)
     |                                      |
     | (You Speak Here)                     | (Translated Audio is Generated)
     V                                      V
4. Zoom/Meet                <--   3. CABLE Output (Virtual Microphone)
     ^                                      ^
     | (Meeting Hears This)                 |
     |______________________________________|

Live Demo
Here is a short demonstration of the application in action.

(This is a placeholder. You can create a GIF of your app working and place it here. Tools like ScreenToGif or Loom are great for this.)

✨ Key Features
🎤 Two-Way Translation: Translates both incoming audio from the meeting and outgoing audio from the user.

🖥️ Standalone Application: Works without a complex browser extension, making it more reliable and easier to set up.

** MENU-DRIVEN INTERFACE**: An easy-to-use command-line menu to switch between listening and speaking modes.

🌐 Multi-Language Support: Easily configurable for various languages (e.g., Hindi, English, Spanish).

🤖 Automatic Device Detection: The script automatically finds the necessary virtual audio devices to simplify setup.

🛠️ Required Software
Before you begin, you must install the following software on your Windows machine:

Python 3.9+: Make sure to check the box "Add python.exe to PATH" during installation.

VB-CABLE (Virtual Audio Cable): This is the most important tool for routing audio.

Download VB-CABLE here

After downloading, unzip the file, right-click VBCABLE_Setup_x64.exe and select "Run as administrator".

⚙️ Installation & Setup

Step 1: Get the Project and Install Libraries
Download or clone the project files to your computer.

Open your terminal (Command Prompt or PowerShell) and navigate to the python_backend folder.

cd C:\Path\To\Your\Project\python_backend

Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

Step 2: Configure Windows Audio (One-Time Setup)
Important: This step prevents the "listening timed out" error by ensuring your virtual devices are not muted.

Right-click the speaker icon on your taskbar and open Sounds.

Go to the Playback tab, right-click on CABLE Input, and select Properties.

Go to the Levels tab and make sure the volume is set to at least 75 and is not muted.

▶️ How to Use

Step 1: Run the Application
Navigate to the python_backend folder in your terminal and run the main script:

python translator_app.py
