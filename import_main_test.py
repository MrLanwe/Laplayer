from main import surfWeb

movies = surfWeb('eve online')

movie_addr = "http://www.youtube.com/watch?v="

print(movies)

for i in range(2):
    movie = movies[i]
    print(movie_addr + movie)
