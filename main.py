import webbrowser
import boto3



class HtmlDocument:
    def __init__(self):
        self.message = "<html> <head></head> <body><p>Yerrrrrr im in the cloud, frea real estate ya hurd, its ya boi Chandlerrrrrr! Ain't no friends out here. </p></body> </html> "
        self.save1 = HtmlManager()

    def save(self):
        self.to_save = self.message 
        self.save1.writehtml(self.to_save)
       

class HtmlManager:
    def __init__(self):
        pass
    def writehtml(self, message):
        samplehtml = open('chandtroduction.html', 'w')
        samplehtml.write(message)
        samplehtml.close()
        webbrowser.open_new_tab('chandtroduction.html')

class AWSManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')
    def save_to_s3 (self):
        self.s3_client.upload_file('chandtroduction.html','lmtd-class','chandlerzombek.html')
    def load_from_s3(self):
        self.s3_client.download_file('lmtd-class','chandlerzombek.html','localchandlerzombek.html')
    def list_all_buckets(self):
        print(self.s3_client.list_buckets())
    def print_all_objects(self):
        objects = self.s3_client.list_objects(
            Bucket = "lmtd-class"
        )
        print(objects)

s1 = HtmlDocument()
s1.save()

s2 = AWSManager()
s2.save_to_s3()
#s2.load_from_s3()
s2.print_all_objects()
