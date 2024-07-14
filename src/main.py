import pyaudio
import numpy as np
import pvporcupine
import struct
from akey import access_key
from command_processor import CommandProcessor
from file_manager import FileManager, MusicPlayer
from speech_recognizer import SpeechRecognizer
from text_to_speech import TextToSpeech
from voice_assistant import VoiceAssistant


def execute_assistant():
    recognizer = SpeechRecognizer()
    file_manager = FileManager()
    music_player = MusicPlayer()
    speaker = TextToSpeech()
    command_processor = CommandProcessor(file_manager, music_player)
    assistant = VoiceAssistant(recognizer, speaker, command_processor)

    while True:
        assistant.listen_and_respond()


def main():
    porcupine = None
    pa = None
    audio_stream = None

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
                temp = TextToSpeech()
                
                temp.speak("yes sir")
                print("yes sir")
                execute_assistant()

    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
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
