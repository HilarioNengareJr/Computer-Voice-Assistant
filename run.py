import pyaudio
import numpy as np
import pvporcupine
import struct
from src.akey import access_key
from src.command_processor import CommandProcessor
from src.command_execution import CommandExecution
from src.speech_recognizer import SpeechRecognizer
from src.text_to_speech import TextToSpeech
from src.voice_assistant import VoiceAssistant

def execute_assistant(assistant):
    assistant.listen_and_respond()

def main():
    porcupine = None
    pa = None
    audio_stream = None
    temp = TextToSpeech()
    assistant = None

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["computer", "jarvis"])
        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        while True:
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
    main()
