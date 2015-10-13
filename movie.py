# Movie class


class Movie:
    """
    The Movie class represents a film and some of its salient properties:
    title, year, poster art, trailer, director, length (in minutes) and links to more information
    Note: all of these properties must be provided when creating an instance
    """

    def __init__(self, movie_title, movie_year,
                 movie_poster, movie_trailer_url,
                 movie_director, movie_length, movie_links):
        """
        Initialises an instance of class Movie
        :param movie_title:         film title, string
        :param movie_year:          release year, int
        :param movie_poster:        url to film's poster art, string
        :param movie_trailer_url:   youtube url to film's trailer, string
        :param movie_director:      film's director, string
        :param movie_length:        length of film in minutes, int
        :param movie_links:         links to more info about the film, string tuples ex. (name of resource, url)
        """
        self.title = movie_title
        self.year = movie_year
        self.poster_url = movie_poster
        self.trailer_url = movie_trailer_url
        self.director = movie_director
        self.length = movie_length
        self.links = movie_links

    def show_trailer(self):
        return self.trailer_url