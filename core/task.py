class Task:

    """ This class stores information retrieved from/to the request"""
    def __init__(self, number, target, resource, extension):

        self.number = number
        self.target = target
        self.resource = resource
        self.extension = extension

        self.payload_length = 0
        self.payload_filename = None
        self.banned_response_codes = []

        self.content = None
        self.location = ""
        self.response_code = None
        self.response_size = None
        self.response_time = None
        self.valid = True
        self.content_detected = False

    def set_payload_length(self, length):
        self.payload_length = length

    def get_payload_length(self):
        return self.payload_length

    def set_banned_response_codes(self, banned_codes):
        self.banned_response_codes = banned_codes

    def set_payload_filename(self, payload_filename):
        self.payload_filename = payload_filename

    def set_response_code(self, code):
        self.response_code = str(code)
        if self.response_code in self.banned_response_codes:
            self.valid = False

    def set_location(self, location):
        self.location = location

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def values(self):
        return (self.number,
                self.payload_filename,
                self.target,
                self.resource,
                self.extension,
                self.response_code,
                self.response_size,
                self.response_time,
                self.location)

    def get_complete_target(self):
        if '***' in self.target:
            self.target = self.target.replace('***', self.resource.replace('/', ''))
            self.resource = ""
            return self.target + self.extension
        else:
            return self.target + self.resource + self.extension

    def is_valid(self):
        return self.valid

    def content_has_detected(self, value):
        self.content_detected = value
