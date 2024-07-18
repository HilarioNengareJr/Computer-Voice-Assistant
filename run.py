import pyaudio
import numpy as np
import pvporcupine
import struct
import os
import sys
import random
import time
from src.akey import access_key
from src.command_processor import CommandProcessor
from src.command_execution import CommandExecution
from src.speech_recognizer import SpeechRecognizer
from src.text_to_speech import TextToSpeech
from src.voice_assistant import VoiceAssistant

def matrix_animation():
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    columns = int(columns)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    columns_list = [0] * columns

    start_time = time.time()
    duration = 5
    while time.time() - start_time < duration:
        for i in range(len(columns_list)):
            if random.random() > 0.98:
                columns_list[i] = 0
            else:
                columns_list[i] = min(rows, columns_list[i] + 1)
        
        os.system('clear')

        for row in range(rows):
            line = ""
            for col in range(columns):
                if row < columns_list[col]:
                    line += random.choice(characters) + " "
                else:
                    line += "  "
            print(line)
        
        time.sleep(0.05)

def jarvis_wake_call():
    print("Initializing systems...")
    time.sleep(2)
    matrix_animation()
    print("Jarvis is online...")

def execute_assistant(assistant):
    try:
        assistant.listen_and_respond()
    except Exception as e:
        print(f"An error occurred while executing assistant: {e}")

def main():
    porcupine = None
    pa = None
    audio_stream = None
    temp = TextToSpeech()
    assistant = None

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["computer", "jarvis"])
        
        # Redirect stderr to suppress ALSA errors
        sys.stderr = open(os.devnull, 'w')
        
        pa = pyaudio.PyAudio()
        
        # Restore stderr
        sys.stderr = sys.__stderr__

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        while True:
            try:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                keyword_index = porcupine.process(pcm)

                if keyword_index >= 0:
                    temp.speak("Yes, sir")
                    print("Yes, sir")
                    
                    if assistant is None:
                        recognizer = SpeechRecognizer()
                        cmd = CommandExecution()
                        speaker = TextToSpeech()
                        command_processor = CommandProcessor(cmd)
                        assistant = VoiceAssistant(recognizer, speaker, command_processor)

                    execute_assistant(assistant)
                    assistant = None
            except Exception as e:
                print(f"An error occurred: {e}")

    except KeyboardInterrupt:
        temp.speak("Exiting, sir")
        print("Exiting...")
    except Exception as e:
        temp.speak("Something went wrong, sir")
        print(f"An error occurred: {e}")
    finally:
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()
        if porcupine is not None:
            porcupine.delete()

if __name__ == "__main__":
    jarvis_wake_call() 
    main()
