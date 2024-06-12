from django.urls import path 
from . import views

urlpatterns = [
  path('bahan/' , views.getBahan , name='getbahan' ),
  path('bahan/create' , views.createBahan , name='createbahan'),
  path('bahan/storebahan' , views.storeBahan , name='storebahan'),
  path('bahan/editbahan/<int:id>' , views.editBahan , name='editbahan'),
  path('bahan/updatebahan/<int:id>' , views.updateBahan , name='updatebahan'),

  path('kondisi/' , views.getKondisi , name='getkondisi' ),
  path('kondisi/create' , views.createKondisi , name='createkondisi'),
  path('kondisi/storekondisi' , views.storeKondisi , name='storekondisi'),
  path('kondisi/editkondisi/<int:id>' , views.editKondisi , name='editkondisi'),
  path('kondisi/updatekondisi/<int:id>' , views.updateKondisi , name='updatekondisi'),


  path('warna/' , views.getWarna , name='getwarna' ),
  path('warna/create' , views.createWarna , name='createwarna'),
  path('warna/storewarna' , views.storeWarna , name='storewarna'),
  path('warna/editwarna/<int:id>' , views.editWarna , name='editwarna'),
  path('warna/updatewarna/<int:id>' , views.updateWarna , name='updatewarna'),

   path('kategori/' , views.getKategori , name='getkategori' ),
  path('kategori/create' , views.createKategori , name='createkategori'),
  path('kategori/storekategori' , views.storeKategori , name='storekategori'),
  path('kategori/editkategori/<int:id>' , views.editKategori , name='editkategori'),
  path('kategori/updatekategori/<int:id>' , views.updateKategori , name='updatekategori'),

  path('ukuran/' , views.getUkuran , name='getukuran' ),
  path('ukuran/create' , views.createUkuran , name='createukuran'),
  path('ukuran/storeukuran' , views.storeUkuran , name='storeukuran'),
  path('ukuran/editukuran/<int:id>' , views.editUkuran , name='editukuran'),
  path('ukuran/updateukuran/<int:id>' , views.updateUkuran , name='updateukuran'),

   path('' , views.predictView , name='get' ),
   path('/predict' , views.predict , name='predict')
]