import speech_recognition as sr
import serial

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source, duration=1)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source, timeout=2, phrase_time_limit=4)
    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

while True:
    input('Enter para continuar...')
    frase = ouvir_microfone()
    print('Frase: ' + frase)

    if ('desligar' in frase):
        arduino.write(bytes('b', encoding='utf-8'))
        continue

    if ('ligar' in frase):
        arduino.write(bytes('a', encoding='utf-8'))
        continue