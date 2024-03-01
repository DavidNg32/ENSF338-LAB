import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('songdata.json')

group1 = df[df['loudness'] < -8]
group2 = df[(df['loudness'] >= -8)]

plt.hist(group1['loudness'], bins=30)
plt.title('Tempo distribution for songs with loudness < -8')
plt.tight_layout()
plt.savefig('hist1.png')

plt.hist(group2['loudness'], bins=30)
plt.title('Tempo distribution for songs with loudness >= -8')
plt.tight_layout()
plt.savefig('hist2.png')
