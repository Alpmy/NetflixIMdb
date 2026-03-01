import pandas as pd

try:
    df=pd.read_csv("C:\\Users\\Alp\\PycharmProjects\\NetflixIMdb\\netflixOriginals.csv")
except:
    print('File not found')
    exit()

group=df.groupby("Genre")

print("______________________________________________________________________")
print("______________________________________________________________________")
print(group["IMDB Score"].mean().to_string())
print("______________________________________________________________________")
groupHigh=group["IMDB Score"].mean()
groupHigh = groupHigh[(groupHigh>=7)].sort_values(ascending=False)
print((groupHigh).to_string())
print("______________________________________________________________________")
print("______________________________________________________________________")