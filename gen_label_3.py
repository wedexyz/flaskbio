import pandas as pd
import numpy as np 
from glob import glob

import os
import sys
import socket
import random
import json
import pandas as pd
localIP     = '127.0.0.1'
localPort   =5000
bufferSize  = 20000

UDPServerSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

def load_data (file):  
    data = glob(file)

    arr = []
    for x in data :
        xa = pd.read_csv(x)
        xa = np.array(xa).tolist()
        arr.append(xa)
    
    out = np.array(arr).reshape(-1,10)
    df  = pd.DataFrame(out)
    df  = df.drop([0],axis=1) 
    df.columns= ['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8','label']
    X1 = df.drop(['label'],axis=1)
    data = np.array(X1)
    
   
    return data

while True :
    
    
    for i in range (1):
        dataen= load_data('datacsv\datapola3\*.csv')
        print(dataen)
        for data in dataen : 
            d1 = data[0].tolist()
            print(d1)
            d2 = data[1].tolist()
            d3 = data[2].tolist()
            d4 = data[3].tolist()
            d5 = data[4].tolist()
            d6 = data[5].tolist()
            d7 = data[6].tolist()
            d8 = data[7].tolist()
          

            data = json.dumps({"d1": d1, "d2": d2, "d3": d3,"d4": d4,
                          "d5": d5, "d6": d6 ,"d7": d7, "d8": d8
                        })
            data = str.encode(data)
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            UDPServerSocket.sendto(data, address)
            print(data)
    



 
   




 
