import webbrowser

class Movie():

    """This class contains a movie constructor."""

    def __init__(self, movie_title, poster_image, trailer_youtube):

        """This initializes the movie. It takes in a movie title,
        poster image, and link to the trailer and assigns it to
        the respective properties."""

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
