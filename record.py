#Import librairies for speech recognition
import speechbrain as sb
from speechbrain.dataio.dataio import read_audio
from IPython.display import Audio
from speechbrain.pretrained import EncoderDecoderASR


#Import librairies for listening to the user
import win32clipboard
import time
import os 
from scipy.io.wavfile import write
import sounddevice as sd

# Section about the microphone

file_path = ""
count = 0

def microphone(mot):
    
    fs = 44100
    seconds = 4
    print("Prononcer : "+ mot)
    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels =2)
    sd.wait()
    print("Fin enregistrement")
    write(file_path + str(mot) + ".mp3", fs, myrecording)
    print("Enregistré ok")
 
    
liste = ['renseignement','réception ',
'je ne sais pas',
'postopérateur',
'standardiste',
'opératrice',
'service de démonstration',
'secrétaire virtuelle',

'reconnaissance vocale ',

'assistante virtuelle ',

'Pont de conférence ',

'Espace de conférence ',

'Yassin Djaffar ',

'Ruby Gilles ',

'Racine Thomas ',

'Roullier Alain ',

'Zeglazi Oussama ',

'Mestres Jérôme ',

'Garcin Brice ',

'Pallier Thierry', 

'Nouaille Bertrand', 

'Anthony Costa ',

'Gabrielle Godard', 

'Badja Katia ',

'Salmi Nabila ',

'Vindex Gaëlle ',
]


def main():
    
    for k in liste:
        microphone(k)
    
main()


