# face_counting_app/views.py
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
import dlib
import base64
from io import BytesIO
from django.http import HttpResponse


def count_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Initialize the face detector
    face_detector = dlib.get_frontal_face_detector()

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_detector(gray_image)

    return len(faces)


def index(request):
    return render(request, 'face_counting_app/index.html')


def count_faces_route(request):
    # Get the uploaded image from the POST request
    image_file = request.FILES['image']

    # Save the image file temporarily
    temp_image_path = default_storage.save(
        'temp_image.jpg', ContentFile(image_file.read()))

    # Count faces in the image
    face_count = count_faces(temp_image_path)

    # Encode the image as base64 for display in HTML
    encoded_image = base64.b64encode(open(temp_image_path, 'rb').read()).decode('utf-8')


    # Remove the temporary image file
    default_storage.delete(temp_image_path)

    return render(request, 'face_counting_app/result.html', {'encoded_image': encoded_image, 'face_count': face_count})