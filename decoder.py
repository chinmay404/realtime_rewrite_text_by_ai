import re
import time
import threading

class SentenceDetector:
    def __init__(self):
        self.buffer = ""  # Holds the typed text
        self.last_check = ""  # Tracks already processed sentences

    def fast_sentence_detection(self, text):
        """
        Detect sentences using regex.
        """
        # Split text into sentences based on punctuation followed by space
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return sentences

    def process_text(self, new_text):
        """
        Process new input text to detect and display complete sentences.
        """
        self.buffer += new_text  # Append new text to the buffer
        sentences = self.fast_sentence_detection(self.buffer)

        # Process only the new complete sentences
        for sentence in sentences[:-1]:  # Exclude the last (incomplete) sentence
            if sentence not in self.last_check:
                self.last_check += sentence + " "
                return True

        # Keep only the last incomplete sentence in the buffer
        self.buffer = sentences[-1]
        return False


# def listen_to_input(detector):
#     """
#     Continuously listen to user input and feed it to the detector.
#     """
#     print("Start typing! Press Ctrl+C to stop.")
#     try:
#         while True:
#             new_input = input() + " "  # Add space to simulate real-time typing
#             print(detector.process_text(new_input))
#     except KeyboardInterrupt:
#         print("\nStopping real-time detection. Goodbye!")

# if __name__ == "__main__":
#     detector = SentenceDetector()
#     listen_to_input(detector)
