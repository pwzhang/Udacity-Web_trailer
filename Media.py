import webbrowser

class Movie():

    '''class for representing a movie'''
    def __init__(self, title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        # initial a movie object
        self.title = title      # title of movie
        self.storyline = movie_storyline       # brief introduction of the movie
        self.poster_image_url = poster_image          # image source url
        self.trailer_youtube_url = trailer_youtube     # url of trailer from youtube
        self.release_date = release_date

    def show_trailer(self):
        ''' Opens trailers in a web browser'''
        webbrowser.open(self.trailer_youtube_url)