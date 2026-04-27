movies = [
    {"title": "3 Idiots", "genre": "comedy", "rating": 8.4},
    {"title": "PK", "genre": "comedy", "rating": 8.1},
    {"title": "Andhadhun", "genre": "thriller", "rating": 8.2},
    {"title": "Drishyam", "genre": "thriller", "rating": 8.2},
    {"title": "Magadheera", "genre": "action", "rating": 8.0},
    {"title": "Baahubali", "genre": "action", "rating": 8.1},
    {"title": "Loki", "genre": "sci-fi", "rating": 8.3},
    {"title": "Interstellar", "genre": "sci-fi", "rating": 8.6},
    {"title": "Inception", "genre": "sci-fi", "rating": 9.0},
    {"title": "Yeh Jawaani Hai Deewani", "genre": "romance", "rating": 7.2},
]

n = input("please enter your choice of search(genre or title):")
results =[]
if (n == "title"):
    search = input("please enter your title choice:").lower()

    results = [n for n in movies if search in n["title"].lower()]

elif(n == "genre"):
    search = input("please enter your genre choice:").lower()
    results = [n for n in movies if search in n["genre"].lower()]
else:
    print("please enter right think")


results = sorted(results, key=lambda x : x["rating"], reverse=True)
if(results) :
    if n == "genre":
        print(f"\nTop {len(results)} movies in the {search.title()} genre:\n")
    else:
        print(f"\nFound {len(results)} movie(s) matching '{search.title()}':\n")
        
    for i in results:
        print(f"  {i['title']} — ⭐ {i['rating']}")
else :
    #avaliable = set(n["genre"] for n in movies)
    #print(f"genre not found. Try {',' .join(avaliable)}")
    print(f"\nNo results found for your search.")
