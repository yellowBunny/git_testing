import pandas as pd

def open_csv(path):
    with open(path, 'r') as file:
        matrix = pd.read_csv(file, sep=';')
    return matrix

path = r'C:\Users\seb\Desktop\m2.csv'
m = open_csv(path)
X = m[['pow','liczba pokoi', 'pietro','czynsz']]
Y = m[['cena']]
# print(X)
# print(Y)
print(X['pow'][1])
print(X.loc[1,'pow'])