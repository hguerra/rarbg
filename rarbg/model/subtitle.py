class Subtitle(object):
    def base_url(self):
        raise NotImplementedError

    def language(self):
        raise NotImplementedError

    def search_url(self, term):
        return self.base_url() + self.__search_path(term)

    def __search_path(self, term):
        return "/en/search2/sublanguageid-{}/moviename-{}".format(self.language(), term)
