from app import app
import unittest
from io import BytesIO


class FlaskTestCase(unittest.TestCase):
    # test for checking if flask server was setup up correctly

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test for upload functionality

    def test_file_upload(self):
        tester = app.test_client(self)
        data = {
            'field': 'img',
            'file': (BytesIO(b'FILE CONTENT'), 'static/upload/test_image.jpg')
        }

        request = tester.post('/', buffered=True,
                              content_type='multipart/form-data',
                              data=data)
        response = tester.get('/', content_type='image/*')
        self.assertEqual(response.status_code, 200)