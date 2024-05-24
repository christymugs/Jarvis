import speech_recognition as sr  # Importing the speech recognition library
import os  # Importing the os library for system operations
import pywhatkit  # Importing the pywhatkit library for YouTube operations
import datetime  # Importing the datetime module for time and date operations
import wikipedia  # Importing the Wikipedia library for fetching information
import random  # Importing the random module for generating random responses
import re  # Importing the re module for regular expressions

class Jarvis:
    def __init__(self):
        self.listener = sr.Recognizer()  # Creating a recognizer object for speech recognition

    def talk(self, text):
        os.system('say "{}"'.format(text))  # Using the 'say' command to speak out the text

    def input_instruction(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                speech = self.listener.listen(source)  # Listening to microphone input
                instruction = self.listener.recognize_google(speech)  # Using Google Speech Recognition to recognize speech
                instruction = instruction.lower()  # Converting the recognized speech to lowercase
                print(instruction)
                return instruction  # Returning the recognized instruction
        except Exception as e:
            print("Error recognizing instruction:", e)
            return ""  # Returning an empty string in case of an error

    def solve_math_problem(self, problem):
        try:
            # Remove any non-alphanumeric characters except math symbols
            problem = re.sub(r'[^0-9+\-*/^()]', '', problem)  # Using regular expressions to remove unwanted characters
            result = eval(problem)  # Evaluating the mathematical expression
            return result  # Returning the result of the evaluation
        except Exception as e:
            return str(e)  # Returning the error message as a string in case of an error

    def play_Jarvis(self):
        while True:  # Continuous conversation loop
            instruction = self.input_instruction()  # Getting the user's input
            print(instruction)

            if "play" in instruction:  # If the instruction contains "play"
                song = instruction.replace('play', "").strip()
                self.talk("playing " + song)
                pywhatkit.playonyt(song)  # Playing the specified song on YouTube

            elif 'time' in instruction:  # If the instruction contains "time"
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                self.talk('Current time is ' + current_time)  # Speaking out the current time

            elif 'date' in instruction:  # If the instruction contains "date"
                current_date = datetime.datetime.now().strftime('%d/%m/%Y')
                self.talk("Today's date is " + current_date)  # Speaking out the current date

            elif 'how are you' in instruction:  # If the instruction contains "how are you"
                responses = ["I'm functioning within normal parameters.", "I'm feeling excellent, thank you for asking!",
                             "I'm here and ready to assist you!", "As an AI, I don't experience emotions, but I'm ready to help."]
                response = random.choice(responses)
                self.talk(response)  # Speaking out a random response

            elif 'what is your name' in instruction:  # If the instruction contains "what is your name"
                self.talk('My name is Jarvis, how can I assist you today?')  # Speaking out the response

            elif 'who is' in instruction:  # If the instruction contains "who is"
                query = instruction.replace('who is', "").strip()
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    print(summary)
                    self.talk(summary)  # Speaking out the Wikipedia summary of the queried topic
                except wikipedia.exceptions.DisambiguationError as e:
                    self.talk("There are multiple options. Please be more specific.")
                except wikipedia.exceptions.PageError as e:
                    self.talk("Sorry, I couldn't find any information on that.")

            elif 'tell me a joke' in instruction:  # If the instruction contains "tell me a joke"
                jokes = ["Why was the math book sad? It had too many problems.",
                         "Why don't skeletons fight each other? They don't have the guts.",
                         "Why don't scientists trust atoms? Because they make up everything."]
                joke = random.choice(jokes)
                self.talk(joke)  # Speaking out a random joke

            elif 'solve' in instruction:  # If the instruction contains "solve"
                problem = instruction.replace('solve', "").strip()
                result = self.solve_math_problem(problem)
                self.talk("The result is " + str(result))  # Speaking out the result of the mathematical problem

            elif 'exit' in instruction or 'bye' in instruction:  # If the instruction contains "exit" or "bye"
                self.talk("Goodbye!")  # Speaking out the goodbye message
                break  # Exiting the conversation loop

            else:
                self.talk('I did not understand that. Can you please repeat?')  # Speaking out the request for repetition

jarvis = Jarvis()
jarvis.play_Jarvis()
