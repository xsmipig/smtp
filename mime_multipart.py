from mime_base import MIMEBase
from email import utils
import random

def generate_boundary():
    #get a random length
    length = random.randint(25, 40)
    multipart_char = '-_=1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    boundary = ''
    for i in range(length):
        index = random.randint(0,(len(multipart_char) - 1))
        boundary += multipart_char[index]
    boundary = 'NextPart==%s==' % boundary
    return boundary


class MIMEMultipart(MIMEBase):
    def __init__(self,
                 sub_type=None,
                 boundary=None,
                 **parms):
        
        if sub_type is None:
            MIMEBase.__init__(self,'multipart','mixed')
        else:
            MIMEBase.__init__(self,'multipart',sub_type)
        self.boundary = None
        if boundary is None:
            self.boundary = generate_boundary()
        self.header['Content-Type'] += '; boundary="%s"' % self.boundary
        self.fields = {}
        self.payload =''

    def attach(self, 
               mime_message):
        self.payload += '--%s\r\n' % self.boundary
        self.payload += str(mime_message)


