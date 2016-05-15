import webbrowser


class Movie():
    def __init__(self, movie_title, movie_description, movie_poster_url, movie_youtube_url):
        self.title = movie_title
        self.description = movie_description
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_youtube_url

        def showTrailer(self):
            webbrowser.open(self.trailer_youtube_url)
