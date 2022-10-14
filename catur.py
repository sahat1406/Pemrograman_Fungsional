import collections;
Bidak = collections.namedtuple('Catur', ['warna','posisi'])

class bidakCatur:
   warna = 'hitam putih'.split()
   posisi = 'raja ratu kuda1 kuda2 peluncur1 peluncur2 kastil1 kastil2 pion1 pion2 pion3 pion4 pion5 pion6 pion7 pion8'.split()

   def __init__(self):
       self._bidak = [
               Bidak(warna, posisi)
                   for warna in self.warna
                   for posisi in self.posisi
           ]

   def __len__(self):
       return len(self._bidak)

   def __getitem__(self, posisi):
       return self._bidak[posisi]

   def __str__(self):
       return str(self._bidak)


print(bidakCatur());

