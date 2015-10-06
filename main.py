# -*- encoding: utf-8 -*-
import pyaudio,wave,subprocess,os, pyttsx,time, urllib2, json,webbrowser
from psychopy.microphone import *
from termcolor import colored
colorgrn = "\033[1;36m{0}\033[00m"

######## Voz ############
#jarvis = pyttsx.init()
#jarvis.setProperty('voice', "spanish")
#jarvis.setProperty('rate', jarvis.getProperty('rate')-50)
#jarvis.setProperty("languages","spanish")
#jarvis.runAndWait()
#########################

def parseToText(): #segun quiera acettos o no
	try:
		url="http://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
		r= urllib2.Request(url, open('audio.flac').read())
		r.add_header("Content-Type","audio/x-flac; rate=16000") #agrego content type
		response = urllib2.urlopen(r).read().strip('{"result":[]}') #elimino primer json que es nulo
		jon= json.loads(response) #cargo json
		print jon
		return jon['result'][0]['alternative'][0]['transcript'].lower()
	except ValueError:
		#El archivo de audio no contenia nada
		return "Null"
	

def listening(seg):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 16000
	WAVE_OUTPUT_FILENAME = "audio.wav"
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
	            channels=CHANNELS,
	            rate=RATE,
	            input=True,
	            frames_per_buffer=CHUNK)
	frames = []
	for i in range(0, int(RATE / CHUNK * seg)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	wav2flac('audio.wav', keep=True)
	texto=parseToText()
	return texto

def say(texto):
	#jarvis.say(texto)
	#jarvis.runAndWait()
	print colorgrn.format(texto)

if __name__ == '__main__':
	say("Iniciando...")
	while True:
		flag=listening(3)
		print flag
		if flag=="brian":
			#say("Hola lautaro, que deseas?")
			say("kékHeRe")
			comando=listening(5)
			with open("comandos.txt") as f:
				for linea in f:
					if comando.split(" ")[0]==linea.split("=")[0]:
						print linea.split("=")[1]
						exec(linea.split("=")[1])
		elif flag=="chau":
			pass
