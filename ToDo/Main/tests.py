from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import To_do

# Create your tests here.


class TareasTests(APITestCase):
    
    def test_create_tarea(self):
        url = reverse('task-list-create')
        data = {'Titulo':'Test Task', 'Descripcion':'Description', 'Completado': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)