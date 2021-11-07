import requests

url = "https://animechan.vercel.app/api/random"
data = requests.get(url).json()
ani = data['anime']
char = data['character']
qu = data['quote']
print(f"**''{qu}''**\n\n-__{char}__ (__{ani}__)")
    
