import Media
import fresh_tomatoes

def main():
    '''This is a object of movies
    Attributes:
        Title = title of the movie
        story_line = introduction of the movie
        url_image = source of image of the movie
        url_trailer = url of the movie trailer from youtube
        release_time = time to release the movie'''

    The_Dark_Tower = Media.Movie(
        "The Dark Tower",
        '''In a world full of superheroes, there's only one Gunslinger.''',
        'https://upload.wikimedia.org/wikipedia/en/4/49/The_Dark_Tower_teaser_poster.jpg',
        'https://www.youtube.com/watch?v=GjwfqXTebIY',
        'May 3, 2017'
    )

    The_Defenders = Media.Movie(
        "Marvel's The Defenders",
        '''A quartet of singular heroes with one common goal - to save New York City.''',
        'http://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/article_width/public/'
        '2017/01/marvel-the-defenders-comics_0.jpg?itok=865DJd9Y',
        'https://www.youtube.com/watch?v=4h3m7B4v6Zc',
        'August 18, 2017'
    )

    Thor = Media.Movie(
        "Thor 3 Ragnarok",
        '''Thor must defeat the Hulk in a gladiatorial duel in time to save Asgard.''',
        'https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Thor_Ragnarok_poster.jpg/220px-Thor_Ragnarok_poster.jpg',
        'https://www.youtube.com/watch?v=OctRQoCodVw',
        'November 3, 2017'
    )

    Blade_runner = Media.Movie(
        "Blade Runner 2049",
        '''American neo-noir science fiction film directed by Denis Villeneuve''',
        'https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png',
        'https://www.youtube.com/watch?v=qJA48WZ9bis',
        'October 6, 2017'
    )



    movies = [The_Dark_Tower, The_Defenders, Thor, Blade_runner]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
