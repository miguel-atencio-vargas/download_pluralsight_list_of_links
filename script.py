
import shlex, subprocess, time, os


ydl_link = "youtube-dl --username 'danyatenciovargas@gmail.com' --password '123456789abcd' --verbose --sleep-interval 120  --all-subs"
arrlinks = []
arrdirs = []

archivo = open('links.txt', 'r')
for linea in archivo.readlines():
    arrlinks.append(linea[:-1])
archivo.close() 

archivo = open('carpetas.txt', 'r')
for linea in archivo.readlines():
    arrdirs.append(linea[:-1])
archivo.close() 

i = 0
for link in arrlinks:
    os.chdir('../')
    os.mkdir(arrdirs[i])
    os.chdir(arrdirs[i])
    command = shlex.split(ydl_link)
    command.insert(8, link)
    print('Se empieza a descargar: ')
    print(command)
    subprocess.call(command)
    time.sleep(2)
    i += 1


