import requests
import pytest
import pytest_check as check
from faker import Faker
from datetime import datetime
import logging

logger = logging.getLogger()
fake = Faker ()

def validate_api_response(response, expected_status,expected_fields=None, max_time=1.0):
    assert response.status_code == expected_status

    if expected_status != 204:
        assert 'application/json' in response.headers.get('Content-Type', '')

    if expected_fields and response.text:
        body = response.json()
        assert expected_fields <= set(body.keys())

    assert response.elapsed.total_seconds() < max_time
    return response.json() if response.text else {}



class TestGetUser:

    @pytest.mark.get
    def test_get_response_code(self, api_url):
        response = requests.get(api_url + 'users')
        data = validate_api_response(
            response= response,
            expected_status=200,
            expected_fields=[],
            max_time=2.0
        )
        assert response.status_code == 200

    @pytest.mark.get
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + 'users')
        data = response.json()

        assert len(data) > 0
        assert isinstance(data, list) 

        first_user = data[0]
        key_structure = ['id', 'name', 'username', 'phone', 'address', 'websites' ] ## Websites mal escrito para que falle el test.
        for i in key_structure:
            assert i in first_user , f'campo{i}, no esta en {first_user}'




class TestPostUser:

    @pytest.mark.post
    def test_post_response_code (self, api_url):

        new_user = {
            'name': fake.name(),
            'email' :fake.email(),
            'phone' : fake.phone_number(),
            #'createdAt' : '2022-05-05'

        }


        response = requests.post(api_url + 'users', new_user)        
        assert response.status_code == 201

        data = response.json()
        assert 'id' in data

        if 'createdAt' in data:
            created_at = data ['createdAt']
            current_year = datetime.now().year 
            assert str(current_year) in created_at, f'No es el mismo anio'



class TestUserWorkflow:
    def test_completo_users(self, api_url):
        logger.info("TEST ENCADENADOS: GET, POST, DELETE")
        logger.info("1. GET - Obtener usuarios")

        # GET: Obtener usuarios
        response = requests.get(api_url + 'users')
        data = response.json()

        logger.info(f"GET Status code: {response.status_code}")
        logger.info(f"Cantidad de usuarios obtenidos: {len(data)}")

        check.equal(response.status_code, 200)
        check.is_true(len(data) > 0)

        logger.info("2. POST - Crear usuario")

        new_user = {
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
        }

        response = requests.post(api_url + 'users', new_user)
        logger.info(f"POST Status code: {response.status_code}")
        assert response.status_code == 201

        created_user = response.json()
        logger.info(f"Usuario creado: {created_user}")

        user_id = created_user["id"]
        logger.info(f"ID del usuario creado: {user_id}")

        logger.info("3. DELETE - Eliminar usuario creado")

        response = requests.delete(api_url + f'users/{user_id}')
        logger.info(f"DELETE Status code: {response.status_code}")
        logger.info(f"DELETE response body: {response.text}")

        assert response.status_code == 200 or response.status_code == 204
