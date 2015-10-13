# -*- coding: utf-8 -*-
import fresh_tomatoes
import movie

# Set logging level to logging.DEBUG when debugging
import logging
logging.basicConfig(level=logging.ERROR,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Filling movie \'database\'')

# Define / create Movie instances for six favourite-ish films
electric_dragon = movie.Movie('Electric Dragon 80.000 V', 2001,
                              r'https://upload.wikimedia.org/wikipedia/en/9/91/Electricdragon.jpg',
                              r'https://www.youtube.com/watch?v=0nHfldl5FzQ',
                              'Gakuryû Ishii', 55,
                              (('IMDB', r'http://www.imdb.com/title/tt0276935/'),
                               ('Wikipedia', r'https://en.wikipedia.org/wiki/Electric_Dragon_80.000_V')))

midnight_in_paris = movie.Movie('Midnight in Paris', 2011,
                                r'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                r'https://www.youtube.com/watch?v=FAfR8omt-CY',
                                'Woody Allen', 94,
                                (('IMDB', r'http://www.imdb.com/title/tt1605783/'),
                                 ('Wikipedia', r'https://en.wikipedia.org/wiki/Midnight_in_Paris'),
                                 ('Website', r'http://www.sonyclassics.com/midnightinparis/')))

manos = movie.Movie('Manos: The Hands of Fate', 1966,
                    r'https://upload.wikimedia.org/wikipedia/commons/f/fe/Manosposter.jpg',
                    r'https://www.youtube.com/watch?v=tRcGukCdr3c',
                    'Harold P. Warren', 75,
                    (('IMDB', r'http://www.imdb.com/title/tt0060666/'),
                     ('Wikipedia', r'https://en.wikipedia.org/wiki/Manos:_The_Hands_of_Fate')))

inception = movie.Movie('Inception', 2010,
                        r'https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg',
                        r'https://www.youtube.com/watch?v=d3A3-zSOBT4',
                        'Christopher Nolan', 148,
                        (('IMDB', r'http://www.imdb.com/title/tt1375666/'),
                         ('Wikipedia', r'https://en.wikipedia.org/wiki/Inception'),
                         ('Website', r'http://www.warnerbros.com/inception')))

wall_e = movie.Movie('WALL-E', 2008,
                     r'https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg',
                     r'https://www.youtube.com/watch?v=alIq_wG9FNk',
                     'Andrew Stanton', 98,
                     (('IMDB', r'http://www.imdb.com/title/tt0910970/'),
                      ('Wikipedia', r'https://en.wikipedia.org/wiki/WALL-E'),
                      ('Website', r'http://movies.disney.com/wall-e')))

pans_labyrinth = movie.Movie('Pan\' Labyrinth', 2006,
                             r'https://upload.wikimedia.org/wikipedia/en/6/67/Pan%27s_Labyrinth.jpg',
                             r'https://www.youtube.com/watch?v=EqYiSlkvRuw',
                             'Guillermo del Toro', 118,
                             (('IMDB', r'http://www.imdb.com/title/tt0457430/'),
                              ('Wikipedia', r'https://en.wikipedia.org/wiki/Pan%27s_Labyrinth')))

# Create list of films and populate it with the Movie instances
movies = list()
movies.append(electric_dragon)
movies.append(midnight_in_paris)
movies.append(manos)
movies.append(inception)
movies.append(wall_e)
movies.append(pans_labyrinth)

# DEBUG logging
for item in movies:
    logging.debug('========= Movie info =========')
    logging.debug('Title: ' + item.title)
    logging.debug('Year: ' + str(item.year))
    logging.debug('Poster URL: ' + item.poster_url)
    logging.debug('Trailer URL: ' + item.trailer_url)
    logging.debug('Director: ' + item.director)
    logging.debug('Length: ' + str(item.length))
    logging.debug('Links: ')
    for link in item.links:
        logging.debug('Link: name=' + link[0] + ', url=' + link[1])

# Generate page and open in browser
fresh_tomatoes.open_movies_page(movies)
