from django.db import models

# Create your models here.
class Bahan(models.Model):
  nama_bahan = models.CharField(max_length=200)

class Kategori(models.Model) :
  nama_kategori = models.CharField(max_length=200)

class Kondisi(models.Model):
  nama_kondisi = models.CharField(max_length=200)

class Warna(models.Model):
  nama_warna = models.CharField(max_length=255)

class Ukuran(models.Model):
  nama_ukuran = models.CharField(max_length=255)


class Sepatu(models.Model):
  nama_sepatu = models.CharField(max_length=255)
  bahan = models.ForeignKey(Bahan, on_delete=models.CASCADE)
  kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
  kondisi = models.ForeignKey(Kondisi, on_delete=models.CASCADE)
  warna = models.ForeignKey(Warna, on_delete=models.CASCADE)
  harga = models.IntegerField()
  ukuran = models.ForeignKey(Ukuran , on_delete=models.CASCADE)

  