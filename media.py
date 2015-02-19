# Full Stack Web Developer Nanodegree from Udacity
# P1 Movie Trailer Website
# Last updated 17 February 2015 by David Whiteley


# for displaying Web-based documents
import webbrowser

class Movie():
    
    """ This classs provides a way to store movie related information """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ Trailer opened in new raised browser window """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url,1,True)
