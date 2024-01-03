# Speech-to-Code
A Python application that takes speech and converts it to C++ code

## Description
Speech-to-Code was built using Python and Lark so that users do not have to specify syntax when using speech dictation to write code. Our current grammar allows for conversion of if-statements to C++ code. 

## Authors
- [Ally Thach](https://www.github.com/baxically)
- [Mahdi Aouchiche](https://github.com/mahdi-aouchiche)
- [Sanchit Goel](https://github.com/sanchitgoel01)

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
