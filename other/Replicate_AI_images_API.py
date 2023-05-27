# trzeba ustawić w systemie zmienną środowiskową z tokenem mojego konta w Replicate.com
# export REPLICATE_API_TOKEN=XYZ

# instalowanie Replicate: pip install replicate
# instalowanie PIP:
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
import replicate


# ustawienia:
model_AI = "stability-ai/stable-diffusion"
fraza = "beautiful spring garden with pond and fountain"
szer = 768
wys = 512

# teraz możemy dodać do słownika np. 3 różne modele AI i napisać pętlę generującą obrazy dla każdego z tych modeli
# lub pętlę generującą kilka podobnych obrazów o różnym ustawieniu wierności obrazu z frazą
model = replicate.models.get(model_AI)
output = model.predict(prompt=fraza, width=szer, height=wys)
