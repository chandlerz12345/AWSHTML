import webbrowser
import boto3



class HtmlDocument:
    def __init__(self):
        self.message = "<html> <head></head> <body><p>Hello World!</p></body> </html> "
        self.save1 = HtmlManager()

    def save(self):
        self.to_save = self.message 
        self.save1.writehtml(self.to_save)
       

class HtmlManager:
    def __init__(self):
        pass
    def writehtml(self, message):
        samplehtml = open('helloworld.html', 'w')
        samplehtml.write(message)
        samplehtml.close()
        webbrowser.open_new_tab('helloworld.html')

class AWSManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')
    def connect(self):
        self.s3_client.upload_file('helloworld.html','lmtd-class','chandlerzombek.html')

s1 = HtmlDocument()
s1.save()

s2 = AWSManager()
s2.connect()