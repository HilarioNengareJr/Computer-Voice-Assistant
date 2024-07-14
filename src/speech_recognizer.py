import os
import sys
import speech_recognition as speech

class SpeechRecognizer:
    
    def recognize_speech(self):
        
        recognizer = speech.Recognizer()
        
        # Suppress ALSA errors
        sys.stderr = open(os.devnull, 'w')
        
        with speech.Microphone() as source:
            try:
                audio = recognizer.listen(source)
                print("\nListening....\n")
                return recognizer.recognize_google(audio)
            
            except speech.UnknownValueError:
                print("Could not understand audio")
                return None
                
            except speech.RequestError as e:
                print(f"Could not request results; {e}")
                return None
                
        # Re-enable stderr
        sys.stderr = sys.__stderr__    
                
        return None
        
    def is_command_legit(self, command):
        pass