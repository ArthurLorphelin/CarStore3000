from app import app
from run import launch_app

import unittest
import json

class Test(unittest.TestCase):

	def set_up(self):
		self.app = launch_app()
		self.buyer = self.test_client()

	def test_homePage(self):
		response = self.buyer().get('/')
		self.assertEqual(response.data, b'Test complete! Welcome!')

if __name__ = '__main__':
	unittest.main()