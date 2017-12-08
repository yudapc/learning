from sklearn import tree

#jeruk = 0
#apel = 1
#halus = 0
#kasar = 1

ciri = [
    [120, 1],
    [150, 1],
    [200, 0],
    [250, 0]
]

label = [0, 0, 1, 1]

mesin = tree.DecisionTreeClassifier()
mesin = mesin.fit(ciri, label)
prediksi = mesin.predict([
    [150, 1]
])

print('Hasil dari prediksinya adalah: %s' % prediksi)
