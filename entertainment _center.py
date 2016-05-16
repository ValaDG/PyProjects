import  media
import fresh_tomatoes

# a single movie object
toyStory = media.Movie("toy story","a good movie","http://aforismi.meglio.it/img/film/Toy_story.jpg"
                       ,"https://www.youtube.com/watch?v=7FQ68Rw25gM")
batman = media.Movie("Batman the Dark Knight", "a great experience for comic fans",
                       "http://geekretreatimages.s3.amazonaws.com/wp-content/uploads/2016/03/The-Dark-Knight.jpg"
                       , "https://www.youtube.com/watch?v=EXeTwQWrcwY")
equilibrium = media.Movie("Equilibrium", "a great action movie, with a deep message",
                        "http://www.gstatic.com/tv/thumb/movieposters/30590/p30590_p_v8_aa.jpg"
                        , "https://www.youtube.com/watch?v=raleKODYeg0")


#the list of movie objects to be displayed in the webpage
movies = [toyStory,batman,equilibrium]

fresh_tomatoes.open_movies_page(movies)

