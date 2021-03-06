# imported the media.py file to access the class

import media
# imported the fresh_tomatoes.py to access the html
import fresh_tomatoes

# defining the instances of class Movie to show movie details
# Avenger movie: movie title, storyline, poster image, trailer link and rating
avengers = media.Movie(
    "The Avengers",
    "S.H.I.E.L.D. leader Nick Fury is compelled to launch the Avengers"
    "Initiative when Loki poses a threat to planet Earth. His squad"
    "of superheroes put their minds together to accomplish the task.",
    "http://www.gstatic.com/tv/thumb/v22vodart/8815512/p8815512_v_v8_an.jpg",  # NOQA
    "https://www.youtube.com/watch?v=kq84NymZYJE",
    "8.1/10"
    )
# Caption america movie: movie title,storyline,poster image,trailer link,rating
captain_america = media.Movie(
    "Captain America: Civil War",
    "Friction arises between the superheroes when one group supports the"
    "government's decision to implement a law to control"
    "their powers while the other opposes it.",
    "http://www.gstatic.com/tv/thumb/v22vodart/10989225/p10989225_v_v8_ax.jpg",  # NOQA
    "https://www.youtube.com/watch?v=pD9fr686QfA",
    "7/10"
    )
# Black panther movie: movie title,storyline,poster image,trailer link,rating
black_panther = media.Movie(
    "Black Panther",
    "After the death of his father, T'Challa returns home to the African"
    "nation of Wakanda to take his rightful place as king."
    "When a powerful enemy suddenly reappears, T'Challa's mettle as king ",
    "http://www.gstatic.com/tv/thumb/v22vodart/12878741/p12878741_v_v8_ac.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KBPp155Fqa8",
    "9.1/10"
    )
# Infinity war movie: movie title,storyline,poster image,trailer link,rating
infinity_war = media.Movie(
    "Avengers: Infinity War",
    "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle"
    "their most powerful enemy yet -- the evil Thanos.On a mission to collect"
    "all six Infinity Stones, Thanos plans to use the artifacts to inflict"
    "his twisted will on reality.The fate of the planet and existence"
    "itself has never been more uncertain as everything the Avengers have"
    "fought for has led up to this moment.",
    "http://www.gstatic.com/tv/thumb/v22vodart/12863030/p12863030_v_v8_ae.jpg",  # NOQA
    "https://www.youtube.com/watch?v=fPtf9f6hw6I",
    "8.8/10"
    )
# Caption marvel movie: movie title,storyline,poster image,trailer link,rating
captian_marvel = media.Movie(
    "Captain Marvel",
    "Captain Marvel gets caught in the middle of a galactic war between two"
    "alien races.",
    "http://www.gstatic.com/tv/thumb/movieposters/14060049/p14060049_p_v8_aa.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Z1BCujX3pw8",
    "8.7/10"
    )
# Doctor strange movie: movie title,storyline,poster image,trailer link,rating
doctor_strange = media.Movie(
    "Doctor Strange",
    "In an accident, Stephen Strange, a famous neurosurgeon, loses the ability"
    "to use his hands. He goes to visit the mysterious Ancient "
    "One to heal himself and becomes a great sorcerer under her tutelage.",
    "http://www.gstatic.com/tv/thumb/v22vodart/11214341/p11214341_v_v8_bc.jpg",  # NOQA
    "https://www.youtube.com/watch?v=jgHbJrKdRHc",
    "9/10"
    )

# Make list of all the instance variables to pass it to media file
movies = [
    avengers,
    captain_america,
    black_panther,
    infinity_war,
    captian_marvel,
    doctor_strange
    ]
# open the HTML page file in webbrowser using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
