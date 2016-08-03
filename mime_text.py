from mime_base import MIMEBase

class MIMEText(MIMEBase):
    def __init__(self,
                 text=None,
                 sub_type=None,
                 char_set=None,
                 **params):
        if sub_type is None:
            MIMEBase.__init__(self,'text','plain')
        else:
            MIMEBase.__init__(self,'text',sub_type)
        if char_set is None:
            self.header['Content-Type'] += '; charset="us-ascii"'
        else:
            self.header['Content-Type'] += '; charset="%s"' % char_set 
        self.header['Content-Transfer-Encoding'] = '7bit'
        self.payload = text

    def attach_payload(self, text):
        self.payload = text

