from plex_test_case import PlexTestCase
from Framework.api.objectkit import ObjectContainer

class MyChannelTest(PlexTestCase):

    def test_main_menu(self):
        # Load './MyChannelTest/MainMenuObjectContainer.xml' as expected XML generated by channel.
        expected = self.get_file_contents('MainMenuObjectContainer.xml')
        # Fix HTTP response from the './MyChannelTest/Index.html' file contents.
        self.networking.http_response_body = self.get_file_contents('Index.html')
        # Make a request to channel code (which makes a HTTP request mocked above).
        status, headers, body = self.request('/video/mychannel')
        # Check the return values against expected.
        self.assertEquals(200, status)
        self.assertEquals('application/xml', headers['Content-Type'])
        self.assertEquals(expected, body)