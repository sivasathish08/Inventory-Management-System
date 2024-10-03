from rest_framework.templatetags.rest_framework import items
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

import random
import string




def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random string
    random_string = ''.join(random.choices(characters, k=length))
    return random_string



class ItemCreateTestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='sathish', password='sathish')
        self.client.login(username='sathish', password="sathish")  # Log in the user




    def test_create_item_success(self):
        # Define the URL for the ItemCreate API
        self.url = reverse('item-create')  # Ensure that this URL name matches your URL config
        self.url2 = reverse('token_obtain_pair')
        # Test the successful creation of a new item
        self.item_name=generate_random_string(4)
        data = {
            "name": self.item_name,
            "description": "A new item",
            "price": 200.00,
            "quantity": 5,
            "category": "Books"
        }
        data1={'password': 'sathish', 'username': 'sathish'}
        token_response = self.client.post(self.url2, data1, format='json')
        # Ensure the request was successful
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        token=token_response.data
        headers = {
            'Authorization': f'Bearer {token.get("access")}'
        }
        # Make a POST request to create the item
        response = self.client.post(self.url, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.data.get("id")
        #Fail Case 1
        # Make a POST request to create the item
        response = self.client.post(self.url, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Pass Case 1
        # Get the URL for the item-detail view using the 'reverse' function
        url3 = reverse('item-delete', kwargs={'pk': item_id})
        # Make a PUT request to create the item
        response = self.client.delete(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item_success(self):
        # Define the URL for the ItemCreate API
        self.url = reverse('item-create')  # Ensure that this URL name matches your URL config
        self.url2 = reverse('token_obtain_pair')
        # Test the successful creation of a new item
        self.item_name=generate_random_string(4)
        data = {
            "name": self.item_name,
            "description": "A new item",
            "price": 200.00,
            "quantity": 5,
            "category": "Books"
        }
        data1={'password': 'sathish', 'username': 'sathish'}
        token_response = self.client.post(self.url2, data1, format='json')
        # Ensure the request was successful
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        token=token_response.data
        headers = {
            'Authorization': f'Bearer {token.get("access")}'
        }
        # Make a POST request to create the item
        response = self.client.post(self.url, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.data.get("id")
        # Pass Case 1
        self.url3 = "/api/items/"+str(item_id)+"/update"
        data = {
            "name": "new_data",
            "description": "A new item",
            "price": 200.00,
            "quantity": 5,
            "category": "Books"
        }
        # Make a PUT request to update the item
        response = self.client.put(self.url3, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.url3 = "/api/items/1000/update"
        # Fail Case
        # Make a PUT request to update the item
        response = self.client.put(self.url3, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Pass Case 1
        # Get the URL for the item-detail view using the 'reverse' function
        url3 = reverse('item-delete', kwargs={'pk': item_id})
        # Make a PUT request to create the item
        response = self.client.delete(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_success(self):
        # Define the URL for the ItemCreate API
        self.url = reverse('item-create')  # Ensure that this URL name matches your URL config
        self.url2 = reverse('token_obtain_pair')
        # Test the successful creation of a new item
        self.item_name=generate_random_string(4)
        data = {
            "name": self.item_name,
            "description": "A new item",
            "price": 200.00,
            "quantity": 5,
            "category": "Books"
        }
        data1={'password': 'sathish', 'username': 'sathish'}
        token_response = self.client.post(self.url2, data1, format='json')
        # Ensure the request was successful
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        token=token_response.data
        headers = {
            'Authorization': f'Bearer {token.get("access")}'
        }
        # Make a POST request to create the item
        response = self.client.post(self.url, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.data.get("id")
        # Pass Case 1
        # Get the URL for the item-detail view using the 'reverse' function
        url3 = reverse('item-detail', kwargs={'pk': item_id})
        # Make a GET request to get the item
        response = self.client.get(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url3 = reverse('item-detail', kwargs={'pk': "100000"})
        # Fail Case
        # Make a GET request to get the item
        response = self.client.get(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Pass Case 1
        # Get the URL for the item-detail view using the 'reverse' function
        url3 = reverse('item-delete', kwargs={'pk': item_id})
        # Make a PUT request to create the item
        response = self.client.delete(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item_success(self):
        # Define the URL for the ItemCreate API
        self.url = reverse('item-create')  # Ensure that this URL name matches your URL config
        self.url2 = reverse('token_obtain_pair')
        # Test the successful creation of a new item
        self.item_name=generate_random_string(4)
        data = {
            "name": self.item_name,
            "description": "A new item",
            "price": 200.00,
            "quantity": 5,
            "category": "Books"
        }
        data1={'password': 'sathish', 'username': 'sathish'}
        token_response = self.client.post(self.url2, data1, format='json')
        # Ensure the request was successful
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        token=token_response.data
        headers = {
            'Authorization': f'Bearer {token.get("access")}'
        }
        # Make a delete request to create the item
        response = self.client.post(self.url, data, format='json',headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.data.get("id")
        # Pass Case 1
        # Get the URL for the item-detail view using the 'reverse' function
        url3 = reverse('item-delete', kwargs={'pk': item_id})
        # Make a PUT request to create the item
        response = self.client.delete(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url3 = reverse('item-delete', kwargs={'pk': item_id})
        # Fail Case
        # Make a delete request to delete the item
        response = self.client.delete(url3,headers=headers)
        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



