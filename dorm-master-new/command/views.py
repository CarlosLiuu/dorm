from django.shortcuts import render
from django.shortcuts import redirect

import serial
# Create your views here.

def send_command(request):
	SER = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, interCharTimeout=0.001)
	
