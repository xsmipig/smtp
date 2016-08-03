'''
MIME Header RFC 2045
MIME-message-headers := entity-headers
                        fields
                        version CRLF

entity-headers := [ content CRLF ]
                  [ encoding CRLF ]
                  [ id CRLF ]
                  [ description CRLF ]
                  *( MIME-extension-field CRLF )
'''
class mime_message(object):
    def __init__(self):

        self.fields = []

        self.header = {'content_type':None,
                       'encoding':None,
                       'id':None,
                       'description':None,
                       'version':None,
                       'fields':self.fields}


    def set_message_header(self,
                           content_type=None,
                           encoding=None,
                           version=None,
                           **fields):
        self.set_version(version)
        self.set_encoding(encoding)
        self.set_type(content_type)
        for name in fields:
            self.fields.append(fields[name])


    #version := "MIME-Version" ":" 1*DIGIT "." 1*DIGIT
    def set_version(self,
                    mime_version=None):
        if mime_version is None:
            self.header['version'] = "MIME-Version: 1.0"
        else:
            self.header['version'] = mime_version

    #discrete-type := "text" / "image" / "audio" / "video" / "application"
    #composite-type := "message" / "multipart"
    def set_type(self, content_type=None):
        #This default is assumed if no Content-Type header field is specified.
        #Content-type: text/plain; charset=us-ascii
        if content_type is None:
            self.header['content_type'] = "Content-type: text/plain; charset=us-ascii" 
        else:
            self.header['content_type'] = content_type

    '''
    encoding := "Content-Transfer-Encoding" ":" mechanism
    mechanism := "7bit" 
                 "8bit" 
                 "binary"
                 "quoted-printable"
                 "base64" 
    '''    
    def set_encoding(self, encoding=None):
        self.header['encoding'] = encoding

    #return mime content as string
    #def to_string(self):

#class MIMEText(object):
#    def __init__(self,_text[, _subtype[, _charset]]

class MIMEMultipart(object):
    def __init__(self,
                 sub_type=None,
                 boundary=None):
        self.boundary = ""
        self.mime_part_headers = []
        self.data = {}
        self.msg = "Content-Type: multipart/"
        if sub_type is None:
            self.msg += "mixed; boundary="
        else:
            self.msg = self.msg + sub_type + "; boundary="
        if boundary is None:
            self.msg += '"===wwwqqqppp123==="\r\n'
        else:
            self.msg += boundary + "\r\n"
        self.msg += "MIME-Version: 1.0\r\n" 

    def attach(self, 
               mime_message):
        self.mime_part_headers.append(mime_message)

    def __getitem__(self, key): 
        return self.data[key]

    def __setitem__(self, key, item):
        self.data[key] = item
        self.msg = self.msg + key + ": " + self.data[key] + "\r\n"

    def __str__(self):
        return self.msg

'''
mime_message1 = mime_message()
mime_message2 = mime_message()
mime_message1.set_message_header(field1="From: test@123.com",
                                field2="To: test@456.com",
                                encoding="Content-Transfer-Encoding: 7bit")
mime.add_mime_message(mime_message1)
mime_message2.set_message_header()
mime.add_mime_message(mime_message2)
for mime_message in mime.mime_part_headers:
    print mime_message['header']
    print "\r\n"
'''  

'''
NOTE TO IMPLEMENTORS:  When checking MIME-Version values any RFC 822
comment strings that are present must be ignored.  In particular, the
following four MIME-Version fields are equivalent:
    MIME-Version: 1.0
    MIME-Version: 1.0 (produced by MetaSend Vx.x)
    MIME-Version: (produced by MetaSend Vx.x) 1.0
    MIME-Version: 1.(produced by MetaSend Vx.x)0
'''

'''
Any field not beginning with "content-" can have 
no defined meaning and may be ignored.
'''
