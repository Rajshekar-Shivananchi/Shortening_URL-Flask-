class URL_Shortener:
    id = 10000000000
    url_id = {}

    def shorten_url(self, m_url):
        if m_url in self.url_id:
            id = self.url_id[m_url]
            shorten_url = self.encode(id)
        else:
            self.url_id[m_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1
        return "short_url.com/" + shorten_url

    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        return "".join(ret[::-1])