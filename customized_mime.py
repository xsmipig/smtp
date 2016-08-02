'''
MIME Header RFC 2045
MIME-part-headers := entity-headers
                     [ fields ]
                     ; Any field not beginning with
                     ; "content-" can have no defined
                     ; meaning and may be ignored.
                     ; The ordering of the header
                     ; fields implied by this BNF
                     ; definition should be ignored.
'''

class Mime(object):
    def __init__(self):
        self.entity_header = {'content_type':None,
                              'encoding':None,
                              'id':None,
                              'description':None}
        self.mime_message_header = {'version':None,
                                    'entity_header':self.entity_header,
                                    'fields':None
                }

    '''    
    MIME-message-headers := entity-headers
                            fields
                            version CRLF
    '''
    def set_mime_message_header(self,
                                 content_type=None,
                                 encoding=None,
                                 version=None):
        self.set_entity_header(content_type,encoding)
        self.set_mime_version(version)


    #version := "MIME-Version" ":" 1*DIGIT "." 1*DIGIT
    def set_mime_version(self,
                         mime_version=None):
        if mime_version is None:
            self.mime_message_header['version'] = "MIME-Version: 1.0"
        else:
            self.mime_message_header['version'] = mime_version
        
    '''
    entity-headers := [ content CRLF ]
                      [ encoding CRLF ]
                      [ id CRLF ]
                      [ description CRLF ]
                      *( MIME-extension-field CRLF )
    '''
    def set_entity_header(self, 
                          content_type=None,
                          encoding=None):
        self.set_content_type(content_type)
        self.set_encoding(encoding)

    #discrete-type := "text" / "image" / "audio" / "video" / "application"
    #composite-type := "message" / "multipart"

    def set_content_type(self, content_type=None):
        #This default is assumed if no Content-Type header field is specified.
        #Content-type: text/plain; charset=us-ascii
        if content_type is None:
            self.entity_header['content_type'] = "Content-type: text/plain; charset=us-ascii" 
        else:
            self.entity_header['content_type'] = content_type

    '''
    encoding := "Content-Transfer-Encoding" ":" mechanism
    mechanism := "7bit" 
                 "8bit" 
                 "binary"
                 "quoted-printable"
                 "base64" 
    '''
    
    def set_encoding(self, encoding=None):
        self.entity_header['encoding'] = encoding



new_mime = Mime()
new_mime.set_mime_message_header()
print new_mime.mime_message_header
        

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
