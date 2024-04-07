import winsound
import time
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class Location:
    
    def __init__(self,number):
        self.number=number
        
    
    def signal(self):
        duration=1000
        frequency=1000
        num_beeps=7
        for _ in range(num_beeps):
            winsound.Beep(frequency,duration)
            time.sleep(1)
        

    def email(self):
        sendgridapi='639f83ce8d349fae368607d3446f15b4-6fbb86a2-d303-4b36-b8bb-62b267be6ced'
        message=Mail(from_email="cyberbrigade.wms@gmail.com",to_emails='kaashvi.mail21@gmail.com',subject="Garbage Bin Full Alert",html_content='<strong>Garbage can is full and needs to be emptied<\strong>')
        try: 
            sg=SendGridAPIClient(sendgridapi)
            response=sg.send(message)
            print("Email sent successfully")
        except Exception as e:
            print("Email not sent")        



    
