from django.shortcuts import render , redirect
from .models import Bahan , Kondisi , Kategori , Warna , Sepatu , Ukuran
from django.http import JsonResponse 
import logging 
from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)

API_URL = "https://entire-elnore-sneakersdaily-b3c43214.koyeb.app/"

# Create your views here.
def getBahan(request):
  bahan = Bahan.objects.all()
  return render(request=request , template_name='bahan/index.html' , context={'list_bahan' : bahan})

def getKondisi(request):
  kondisi = Kondisi.objects.all()
  return render(request=request , template_name='kondisi/index.html' , context={'list_kondisi' : kondisi})

def getWarna(request):
  warna = Warna.objects.all()
  return render(request=request , template_name='warna/index.html' , context={'list_warna' : warna})

def getKategori(request):
  kategori = Kategori.objects.all()
  return render(request=request , template_name='kategori/index.html' , context={'list_kategori' : kategori})

def getUkuran(request):
  ukuran = Ukuran.objects.all()
  return render(request=request , template_name='ukuran/index.html' , context={'list_ukuran' : ukuran})

def createBahan(request):
  return render(request=request , template_name='bahan/create.html' )

def createKondisi(request):
  return render(request=request , template_name='kondisi/create.html' )

def createWarna(request):
  return render(request=request, template_name='warna/create.html')

def createKategori(request):
  return render(request=request , template_name='kategori/create.html' )


def createUkuran(request):
  return render(request=request , template_name='ukuran/create.html' )


def storeBahan(request):
  nama_bahan_field = request.POST['nama_bahan_field']
  bahan = Bahan(nama_bahan=nama_bahan_field)
  bahan.save()
  return redirect('/bahan')

def storeKondisi(request):
  nama_kondisi_field = request.POST['nama_kondisi_field']
  kondisi = Kondisi(nama_kondisi=nama_kondisi_field)
  kondisi.save()
  return redirect('/kondisi')

def storeWarna(request):
  nama_warna_field = request.POST['nama_warna_field']
  warna = Warna(nama_warna=nama_warna_field)
  warna.save()
  return redirect('/warna')

def storeKategori(request):
  nama_kategori_field = request.POST['nama_kategori_field']
  kategori = Kategori(nama_kategori=nama_kategori_field)
  kategori.save()
  return redirect('/kategori')

def storeUkuran(request):
  nama_ukuran_field = request.POST['nama_ukuran_field']
  ukuran = Ukuran(nama_ukuran=nama_ukuran_field)
  ukuran.save()
  return redirect('/ukuran')

def editBahan(request , id):
  bahan = Bahan.objects.get(id=id)
  return render(request=request , template_name='bahan/edit.html' , context={'bahan' : bahan})

def editKondisi(request , id):
  kondisi = Kondisi.objects.get(id=id)
  return render(request=request , template_name='kondisi/edit.html' , context={'kondisi' : kondisi})

def editWarna(request , id):
  warna = Warna.objects.get(id=id)
  return render(request=request , template_name='warna/edit.html' , context={'warna' : warna})

def editKategori(request , id):
  kategori = Kategori.objects.get(id=id)
  return render(request=request , template_name='kategori/edit.html' , context={'kategori' : kategori})

def editUkuran(request, id):
  ukuran = Ukuran.objects.get(id=id)
  return render(request=request , template_name='ukuran/edit.html' , context={'ukuran' : ukuran})

def updateBahan(request , id):
  bahan = Bahan.objects.get(id=id)
  bahan.nama_bahan = request.POST['nama_bahan_field']
  bahan.save()
  return redirect('/bahan')

def updateKondisi(request , id):
  kondisi = Kondisi.objects.get(id=id)
  kondisi.nama_kondisi = request.POST['nama_kondisi_field']
  kondisi.save()
  return redirect('/kondisi')

def updateWarna(request , id):
  warna = Warna.objects.get(id=id)
  warna.nama_warna = request.POST['nama_warna_field']
  warna.save()
  return redirect('/warna')

def updateKategori(request , id):
  kategori = Kategori.objects.get(id=id)
  kategori.nama_kategori = request.POST['nama_kategori_field']
  kategori.save()
  return redirect('/kategori')

def updateUkuran(request , id):
  ukuran = Ukuran.objects.get(id=id)
  ukuran.nama_ukuran = request.POST['nama_ukuran_field']
  ukuran.save()
  return redirect('/ukuran')


def predictView(request):
  ukuran = Ukuran.objects.all()
  kategori = Kategori.objects.all()
  warna = Warna.objects.all()
  bahan = Bahan.objects.all()
  kondisi = Kondisi.objects.all()

  return render(request=request, template_name='predict.html', context={'list_ukuran' : ukuran, 'list_kategori' : kategori, 'list_warna' : warna, 'list_bahan' : bahan, 'list_kondisi' : kondisi})


def predict(request):
          try:
            ukuran = request.POST.get('ukuran_field')
            warna = request.POST.get('warna_field')
            harga = request.POST.get('harga_field')
            kategori = request.POST.get('kategori_field')
            bahan = request.POST.get('bahan_field')
            kondisi = request.POST.get('kondisi_field')

            # Check if any field is missing
            if not all([ukuran, warna, harga, kategori, bahan, kondisi]):
                missing_fields = [field for field, value in {
                    'ukuran_field': ukuran,
                    'warna_field': warna,
                    'harga_field': harga,
                    'kategori_field': kategori,
                    'bahan_field': bahan,
                    'kondisi_field': kondisi
                }.items() if not value]
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                logger.error(error_message)
                return JsonResponse({'error': 'Invalid input', 'details': error_message}, status=400)

            # Mempersiapkan data untuk dikirim ke API
            payload = {
                'ukuran': ukuran,
                'warna': warna,
                'harga': harga,
                'kategori': kategori,
                'bahan': bahan,
                'kondisi': kondisi
            }

            # Log payload
            logger.info(f"Sending payload: {payload}")

            # Mengirim POST request ke API
            response = requests.post('https://entire-elnore-sneakersdaily-b3c43214.koyeb.app/predict', data=payload)

            # Log status code dan respons dari API
            logger.info(f"Received response: {response.status_code}, {response.text}")

            # Mengembalikan respons dari API
            if response.status_code == 200:
                return render(request=request , template_name='predict.html' , context={'data' : response.json()})
            else:
                # Check if the response content type is HTML
                if 'text/html' in response.headers['Content-Type']:
                    # Parse HTML to extract error message
                    soup = BeautifulSoup(response.text, 'html.parser')
                    error_message = soup.get_text()
                    logger.error(f"Received HTML error response: {error_message}")
                    return JsonResponse({'error': 'Failed to get prediction', 'details': error_message}, status=response.status_code)
                else:
                    return JsonResponse({'error': 'Failed to get prediction', 'details': response.text}, status=response.status_code)
          except Exception as e:
            logger.error(f"Error during prediction: {e}")
            return JsonResponse({'error': 'An error occurred during prediction', 'details': str(e)}, status=500)
          else:
            return JsonResponse({'error': 'Invalid request method'}, status=400)