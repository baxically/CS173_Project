# CS173_Project

## Installation
1. Install python requirements via pip (`pip install -r requirements.txt`)

### Testing Speech Recognition
To test if the SpeechRecognition module works, you can execute `python -m speech_recognition`.

### Lark Example
To see an example of the lark parser generator, look at `lark_example.py` which is copy of a lark example that implements
a basic calculator.

## Running
To test the grammar parser, you can run `python lark_parser.py` which is a read-evaluate-print-loop (REPL) where you can type in the words you want to convert to C++ code!
Try typing in `if x greater than 5 then declare y as int and set y to 5` into the loop and see what code is generated!

To test the entire thing, you can run `python project.py` where you can say the C++ code verbally and the speech recognizer will convert your audio to text and the grammar parser generator will generate the respective C++ code.