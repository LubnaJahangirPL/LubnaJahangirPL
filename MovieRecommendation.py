class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

class MovieRecommendation:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)

    def get_movies_by_genre(self, genre):
        genre_movies = [movie for movie in self.movies if movie.genre == genre]
        return genre_movies

    def display_movies(self):
        for movie in self.movies:
            print("Title: {}, Genre: {}".format(movie.title, movie.genre))

# Example usage
recommendation_system = MovieRecommendation()

movie1 = Movie("The Shawshank Redemption", "Drama")
recommendation_system.add_movie(movie1)

movie2 = Movie("Inception", "Sci-Fi")
recommendation_system.add_movie(movie2)

movie3 = Movie("The Dark Knight", "Action")
recommendation_system.add_movie(movie3)

print("All Movies:")
recommendation_system.display_movies()

print("Movies in the Drama genre:")
drama_movies = recommendation_system.get_movies_by_genre("Drama")
for movie in drama_movies:
    print("Title: {}, Genre: {}".format(movie.title, movie.genre))

recommendation_system.remove_movie(movie2)

print("Updated Movie List:")
recommendation_system.display_movies()
