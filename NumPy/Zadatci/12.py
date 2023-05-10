#12.tvorite 2D Numpy polje dimenzija 2x3. Ukoliko je srednja vrijednost svih elemenata veća od 10
#ispišite sumu svih elemenata, u suprotnom ispišite vrijednost najvećeg elementa u polju
import numpy as np

polje = np.array([[1, 2, 3],
                  [4, 5, 6]])

if np.mean(polje) > 10:
    suma = np.sum(polje)
    print("Suma svih elemenata:", suma)
else:
    max_vrijednost = np.max(polje)
    print("Najveći element u polju:", max_vrijednost)













