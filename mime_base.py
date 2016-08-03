from collections import OrderedDict

class MIMEBase(object):
    def __init__(self, 
                 main_type, 
                 sub_type,
                 **params):

        self.header = OrderedDict()
        self.header['Content-Type'] = None
        self.header['MIME-Verision'] = '1.0'
        self.header['Content-Type'] = '%s/%s' % (main_type, sub_type)
        self.payload = None

    def __str__(self):
        msg = ''
        for key, value in self.header.items():
            msg += '%s: %s\r\n' % (key, self.header[key])
        if self.payload is not None:
            msg += '\r\n%s' % self.payload
        return msg 

    def __getitem__(self, key): 
        return self.header[key]

    def __setitem__(self, key, item):
        self.header[key] = item

    def attach_payload(payload):
        pass
