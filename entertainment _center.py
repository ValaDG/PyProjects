import  media
import fresh_tomatoes

toyStory = media.Movie("toy story","a good movie","http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg"
                       ,"https://www.youtube.com/watch?v=7FQ68Rw25gM")
toyStory2 = media.Movie("toy story", "a good movie",
                       "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg"
                       , "https://www.youtube.com/watch?v=7FQ68Rw25gM")

movies = [toyStory,toyStory2]

fresh_tomatoes.open_movies_page(movies)

