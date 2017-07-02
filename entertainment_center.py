import media
import fresh_tomatoes

# create toy story
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# create avatar
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# create snowden
snowden = media.Movie("Snowden",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzYzNzgzOF5BMl5BanBnXkFtZTgwOTg4NzQ4OTE@._V1_SY1000_CR0,0,641,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=QlSAiI3xMh4")

# create before i fall
before_i_fall = media.Movie("Before I Fall",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNDYwOTY0MDI2OV5BMl5BanBnXkFtZTgwOTE5NzM2MDI@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/watch?v=q3Zyy4ZXegE")

# create get out
get_out = media.Movie("Get Out",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

# create wonder wooman
wonder_woman = media.Movie("Wonder Woman",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")


# create movie array and pass to fresh_tomatoes
movies = [toy_story, avatar, snowden, before_i_fall, get_out, wonder_woman]
fresh_tomatoes.open_movies_page(movies)
