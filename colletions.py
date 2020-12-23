"""
 Aprendendo a manipular informações usando coleções do python
"""

from collections import Counter as cnt
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

texto = "Robson rodrigues de souza maria das dores rodrigues da silva roberta rodrigues de souza"

palavras = texto.split()
palavras = dict(cnt(palavras))

palavras_df = pd.DataFrame(palavras.items(), columns=['Palavras', 'Quantidade'])
palavras_df = palavras_df.sort_values(by=["Quantidade"], ascending=False)
palavras_df.head(10).plot(kind='bar', x='Palavras', y='Quantidade', title="Palavraaaas mais escritas")

#x = [0, 1, 2, 3, 4, 5]
#y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
#plt.plot(x, y)
#plt.show()
