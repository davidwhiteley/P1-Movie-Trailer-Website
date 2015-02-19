# Full Stack Web Developer Nanodegree from Udacity
# P1 Movie Trailer Website
# Last updated 17 February 2015 by David Whiteley


# for definition of Movie class
import media

# for generation of Movie Trailers web page
import fresh_tomatoes

# Movie details - instances of Movie class
# Movie poster URLs from Wikipedia
# Movie trailer URLs from YouTube
toy_story = media.Movie("Toy Story",
                        "Toys come to life and have an adventure.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine goes native on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

paddington = media.Movie("Paddington",
                         "A bear comes to London.",
                         "http://upload.wikimedia.org/wikipedia/en/0/06/PaddingtonPOSTER.jpg",
                         "https://www.youtube.com/watch?v=CxeBdrGGU8U")

social_network = media.Movie("The Social Network",
                             "Harvard student builds tech start-up.",
                             "http://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=9y2DbqtpDno")

notting_hill = media.Movie("Notting Hill",
                           "An ordinary boy bumps into a girl.",
                           "http://upload.wikimedia.org/wikipedia/en/3/38/NottingHillRobertsGrant.jpg",
                           "https://www.youtube.com/watch?v=h_daSz5FZYs")

apocalypse_now = media.Movie("Apocalypse Now",
                             "A soldier goes to find a rogue Colonel.",
                             "http://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
                             "https://www.youtube.com/watch?v=IkrhkUeDCdQ")

# Compile list of movies for display on Movie Trailers web site
movies = [toy_story, avatar, paddington, social_network, notting_hill, apocalypse_now]

# Generate Movie Trailers web site with list of movies
fresh_tomatoes.open_movies_page(movies)
