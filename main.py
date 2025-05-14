import tkinter as tk
from tkinter import messagebox

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Reverse dict for decoding
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


# Translator functions
def encode_to_morse(text):
    try:
        return ' '.join(MORSE_CODE_DICT[char] for char in text.upper())
    except KeyError:
        return "Unsupported character"


def decode_from_morse(morse_code):
    try:
        return ''.join(REVERSE_MORSE_CODE_DICT[code] for code in morse_code.strip().split(' '))
    except KeyError:
        return "Invalid Morse sequence"


# GUI App
class MorseApp:
    def __init__(self, root):
        self.root = root
        root.title("Morse Code Translator")
        root.geometry("500x300")
        root.resizable(False, False)
        root.configure(bg="#f0f0f0")

        self.mode = tk.StringVar(value="Encode")

        # Input
        self.input_label = tk.Label(root, text="Input:", font=("Helvetica", 12), bg="#f0f0f0")
        self.input_label.pack(pady=5)
        self.input_text = tk.Text(root, height=4, width=50, font=("Courier", 12))
        self.input_text.pack()

        # Mode selection
        self.mode_frame = tk.Frame(root, bg="#f0f0f0")
        self.mode_frame.pack(pady=5)
        tk.Radiobutton(self.mode_frame, text="Encode", variable=self.mode, value="Encode", bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.mode_frame, text="Decode", variable=self.mode, value="Decode", bg="#f0f0f0").pack(side=tk.LEFT, padx=10)

        # Translate button
        self.translate_button = tk.Button(root, text="Translate", command=self.translate, font=("Helvetica", 12), bg="#007acc", fg="white")
        self.translate_button.pack(pady=10)

        # Output
        self.output_label = tk.Label(root, text="Output:", font=("Helvetica", 12), bg="#f0f0f0")
        self.output_label.pack(pady=5)
        self.output_text = tk.Text(root, height=4, width=50, font=("Courier", 12), state='disabled')
        self.output_text.pack()

    def translate(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if not input_data:
            messagebox.showwarning("Empty Input", "Please enter some text or Morse code.")
            return

        if self.mode.get() == "Encode":
            result = encode_to_morse(input_data)
        else:
            result = decode_from_morse(input_data)

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()
