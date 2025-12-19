import face_recognition
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import Attend
from django.shortcuts import render

class Classify(APIView):
    def post(self, request):
        try:
            # Cek userkey
            user_key = request.headers.get('Userkey')
            if user_key != "ap1att3ndpr0":
                return Response({"error": "Invalid Header"}, status=status.HTTP_403_FORBIDDEN)

            # Ambil file gambar dari request
            photo1 = request.FILES.get('photo1')
            photo2 = request.FILES.get('photo2')

            if not photo1 or not photo2:
                return Response({"error": "Both photo1 and photo2 are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Simpan gambar sementara di model Attend
            x = Attend()
            x.photo1.save(photo1.name, photo1)
            x.photo2.save(photo2.name, photo2)
            x.save()

            # Proses face recognition
            known_image = face_recognition.load_image_file(x.photo1.path)
            unknown_image = face_recognition.load_image_file(x.photo2.path)

            # Dapatkan encoding wajah
            known_encoding = face_recognition.face_encodings(known_image)
            unknown_encoding = face_recognition.face_encodings(unknown_image)

            # Periksa apakah wajah terdeteksi di kedua gambar
            if not known_encoding or not unknown_encoding:
                x.photo1.delete(save=False)
                x.photo2.delete(save=False)
                x.delete()
                return Response({"error": "Face not detected in one or both images."}, status=status.HTTP_400_BAD_REQUEST)

            # Bandingkan wajah
            results = face_recognition.compare_faces([known_encoding[0]], unknown_encoding[0], tolerance=0.4)

            # Hapus file setelah selesai
            x.photo1.delete(save=False)
            x.photo2.delete(save=False)
            x.delete()


            # Kembalikan respons berdasarkan hasil perbandingan
            if results[0]:
                return Response({"success": "Faces match."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Faces do not match."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def home(request):
    return render(request, 'index.html')