import webbrowser #imported the webbrowser library of python to use webbrowser.open() for show trailor

#defining class Movie to keep all its properties at one place
class Movie(): 

    #defining init fuction, defining variables with values
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube,movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    #defining the fuction to open the webbrowser to play trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_url)

