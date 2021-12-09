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

file_path = "C:\\Users\\julja\\Desktop\\informatique\\voicerecognition\\"
audio_information = "record"
count = 0

def microphone(c):
    
    fs = 44100
    seconds = 8 
    print("debut")
    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels =2)
    sd.wait()
    print("milieu")
    write(file_path + audio_information + str(c) + ".wav", fs, myrecording)
    print("fin")
    
    return "C:\\Users\\julja\\Desktop\\informatique\\voicerecognition\\"+ audio_information + str(c) + ".wav"
    #return "speechbrain/asr-crdnn-commonvoice-fr/" + audio_information + str(c) + ".wav"


asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr", savedir="pretrained_models/asr-crdnn-commonvoice-fr")

dico = {('HIGREK', 'HIGRESKI','IREC', 'IREK' ,'GREC','YRIC','IRIC', 'Y', 'YGREK','YOREK','YRAK', 'YOREK'):"Y"}

def reduction_voc(mots):
    
    restriction =[]
    
    for mot in mots:
        change = False
        print(mot)
        for liste_mots in dico.keys():
            if mot in liste_mots:
                restriction.append(dico[liste_mots])
                change = True
            
        if not change:
            restriction.append(mot)
            
    return restriction

while True:
    soundFilePath = microphone(count)
    count +=1
    print(count)
    transcription = asr_model.transcribe_file(soundFilePath)
    print(transcription)
    array = transcription.split(" ")
    print(array)
    print(reduction_voc(array))
