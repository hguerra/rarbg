from subtitle import Subtitle


class Opensubtitle(Subtitle):
    def __init__(self):
        self._base_url = "https://www.opensubtitles.org"
        self._language = "all"

    def base_url(self):
        return self._base_url

    def language(self):
        return self._language


if __name__ == "__main__":
    s = Opensubtitle()
    print(s.search_url("arrow"))
