class clickLink:
    def __init__(self, url, text):
        self.data = f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

    def url(self):
        return self.data
