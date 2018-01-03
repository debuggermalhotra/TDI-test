from app import app, request, upload_file
import unittest

class FlaskTestCase(unittest.TestCase):

    #test for checking if flask server was setup up correctly

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_upload(self):
        tester = app.test_client(self)
        response = tester.get('/upload',content_type='image/*')
        self.assertTrue(request.files['img'] in upload_file)
        self.assertEqual(response.status_code, 200)



if __name__=='__main__':
    unittest.main()
