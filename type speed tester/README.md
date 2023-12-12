# Type Speed Tester

A simple python program to test your typing speed.

<a href="https://ibb.co/Dz5JMNV"><img src="https://i.ibb.co/0mh79kD/Screenshot-20231212-185753.png" alt="Screenshot-20231212-185753" border="0"></a>

## How to run
```bash
python3 -m main.py
```
Set difficulty level and click on the button named _Difficult_. Once done click on Results to obtain the scores. If you want to reset the scores hit Reset.

## Working
The application will ask you to select a difficulty level. Finally Score and Time taken will be displayed. The score is determined by number of correctly typed out words. 

## Dependencies
The application uses the following dependencies:
1. Tkinter
2. wonderswords

Tkinter is used to build the GUI and wonderswords is used to generate random sentences. The project uses a different approach. Rather than selecting random sentences from a text file, the package helps in providing random sentences which helps in obtaining a diverse set of sentences.