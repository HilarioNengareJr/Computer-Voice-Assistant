import os
import sys
import speech_recognition as speech


class SpeechRecognizer:
    
    def recognize_speech(self):
        recognizer = speech.Recognizer()
        
        with speech.Microphone() as source:
            try:
                print("\nListening....\n")
                audio = recognizer.listen(source)
                print("Processing....")
                return recognizer.recognize_google(audio)
            
            except speech.UnknownValueError:
                print("Could not understand audio")
                return None
                
            except speech.RequestError as e:
                print(f"Could not request results; {e}")
                return None
                
        
                
        return None