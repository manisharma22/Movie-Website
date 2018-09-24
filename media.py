# imported the webbrowser library of python to use webbrowser.open()
import webbrowser


class Movie():
    """
    The Movie class take five parameters considering self as defined
    argument, it generates instance variables for the parameters passed
    into it.
    """

    def __init__(self,
                 movie_title, movie_storyline, poster_image, trailer_youtube,
                 movie_rating):
        """
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        :param trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    def show_trailer(self):
        """
        The show_trailer takes self as an argument and opens the
        web browser to play trailer using the webbrowser.open()
        function imported from webbrowser
        """
        webbrowser.open(self.trailer_url)
