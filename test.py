import requests

API_KEY ="9e63b0c56166d252dda5203e2043ebc1"
search = input("Search for a movie: ")
response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={search}")

data = response.json()

results = sorted(data["results"], key=lambda x: x["vote_average"], reverse=True)

for movie in results[:5]:
    print(f"{movie['title']} — ⭐ {movie['vote_average']}")