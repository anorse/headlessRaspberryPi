#This script will run, find the IP of the pi, and email it to me each time it
#is powered on. 1-20-14
import smtplib
import socket
import fcntl
import struct
import lcddriver
import time
#from time import *

def get_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,struct.pack('256s', ifname[:15])
        )[20:24])
try:
        IpAddress = get_ip('eth0')

        fromAddress = 'From@gmail.com'
        toAddress = 'T@gmail.com'o
        msg = "\r\n".join([
                'From: God',
                'To: To@gmail.com',
                'Subject: Pi IP Address update',
                '',
                'The IP address is '+str(IpAddress)])

        username = 'From'
        password = 'Your Password'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromAddress,toAddress,msg)
        server.quit()

        currentTime = time.strftime("%H:%M %D")
        server.starttls()
        server.login(username,password)
        server.sendmail(fromAddress,toAddress,msg)
        server.quit()

        currentTime = time.strftime("%H:%M %D")
        currentTime = "boot " + currentTime
        IpAddress = "IP: " + IpAddress

        lcd = lcddriver.lcd()
        lcd.lcd_display_string("Welcome to the Pi", 1)
        lcd.lcd_display_string(currentTime, 2)
        lcd.lcd_display_string(IpAddress,3)
except:
        lcd = lcddriver.lcd()
        lcd.lcd_display_string("An error occured",1)
        lcd.lcd_display_string("Check the ethernet",2)
        lcd.lcd_display_string(" connection",3)