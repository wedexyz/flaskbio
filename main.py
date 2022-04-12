import json
import random
import time
from datetime import datetime
import random, threading, webbrowser
import socket
from flask import Flask, render_template, url_for, request
from flask import Flask, Response, render_template
import scipy.signal
from scipy import signal
import numpy as np
import pandas as pd
import os
import psutil
import subprocess
import time,webbrowser, pyautogui
import serial.tools.list_ports

file1 = r"gen_label_1.py"
file2 = r"gen_label_2.py"
file3 = r"gen_label_3.py"
prog = r"python.exe"



## filteringS 
low = 7/100
high = 13/100
pole = 3
samp_freq = 200 
notch_freq = 60.0  
quality_factor =10.0 

def tes():
    dat =[]
    for i in range(1):
        for i in range(200):
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())
            a = dec.get("d1")
            b = dec.get("d2")
            c = dec.get("d3")
            d = dec.get("d4")
            e = dec.get("d5")
            f = dec.get("d6")
            g = dec.get("d7")
            h = dec.get("d8")
            x = a,b,c,d,e,f,g,h
            #print(x)
            dat.append(x)
    dat = np.array(dat)
    df = pd.DataFrame(dat)
    df.columns = ['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8']
    
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
    outnot = signal.filtfilt(b_notch, a_notch,df.ch2)
    outnot3 = signal.filtfilt(b_notch, a_notch,df.ch3)

    b, a = scipy.signal.butter(pole, [low, high], 'band')
    outbp = scipy.signal.lfilter(b, a, outnot)
    outbp3 = scipy.signal.lfilter(b, a, outnot3)

    return outnot,outbp,outnot3,outbp3
            
            

application = Flask(__name__)
random.seed()  # Initialize the random number generator
msgFromClient       = "200"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5000)
bufferSize          = 20000
UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
app = Flask(__name__)
app = Flask(__name__ ,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route("/", methods=['GET', 'POST'])
def index():
        ot = "aktifkan server"
        d= []
        h = []
        ports = serial.tools.list_ports.comports()
        for hub, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(hub, desc, hwid))
            d.append(desc)
            h.append(hwid)
        print(request.method)
        if request.method == 'POST':
            if request.form.get('gen1') == 'gen1':
                subprocess.Popen([prog, file1])
                ot = "server satu aktif"
                
            elif  request.form.get('server') == 'server':
                subprocess.Popen([prog, file2])
                ot = "server Dua aktif"
                
            elif  request.form.get('gen3') == 'gen3':
                subprocess.Popen([prog, file3])
                ot = "server tiga aktif"
                
            elif  request.form.get('off1') == 'off1':
                pyautogui.hotkey('ctrl', 'w')
                ot = ".....offf"
               
                time.sleep(5)
                os.system("""taskkill /im python.exe""")
                #
        usbne = d,h
        keluar = ot
        return render_template("index.html",metune =keluar ,cek=usbne)

@app.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            nt,bp,nt3,bp3 =  tes()
            
            
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())
            a = dec.get("d1")
            b = dec.get("d2")
            c = dec.get("d3")
            d = dec.get("d4")
            e = dec.get("d5")
            f = dec.get("d6")
            g = dec.get("d7")
            h = dec.get("d8")
            
            json_data = json.dumps(
            
                {'time': datetime.now().strftime('%M:%S'), 
                'v1': a,'v2': b,'v3': c,'v4': d,
                'v5': e,'v6': f,'v7': g,'v8': h,
                'nt':nt[150],'bp':bp[150],}

                )
            #print(json_data)
            yield f"data:{json_data}\n\n"
            time.sleep(0.02)

    return Response(generate_random_data(), mimetype='text/event-stream')




@app.route('/keglobal')
def keglobal():
   return render_template('global.html')

@app.route('/keproses')
def keproses():
   return render_template('proses.html')
   
@app.route('/kechart')
def kechart():
   return render_template('chartall.html')
@app.route('/ke3d')
def ke3d():
   return render_template('tes.html')




if __name__ == '__main__':
    port = 8001#+ random.randint(0, 999)
    url = "http://127.0.0.1:{0}/".format(port)
    threading.Timer(1.5, lambda: webbrowser.open(url) ).start()
    app.run(host='127.0.0.1',threaded=False,port=8001)