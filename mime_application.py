from mime_base import MIMEBase
import base64


def set_payload(encoder, data):
    if encoder == 'base64':
        return base64.b64encode(data)
    else:
        return data

class MIMEApplication(MIMEBase):
    def __init__(self,
                 data=None,
                 sub_type=None,
                 encoder=None,
                 name=None,
                 **params):

        if sub_type is None:
            MIMEBase.__init__(self,'application','octet-stream')
        else:
            MIMEBase.__init__(self,'application',sub_type)
        
        if name is not None:
            self.header['Content-Type'] += '; Name="%s"' % name
        
        if encoder is None:
            self.encoder = 'base64'
        else:
            self.encoder = encoder
        
        self.header['Content-Transfer-Encoding'] = self.encoder
       
        self.payload = set_payload(self.encoder, data)

    def attach_payload(self, data):
        self.payload = data

