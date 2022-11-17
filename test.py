# -*- coding: utf-8 -*-
import unittest
import json


def coba(jsfile):
	try:
		with open(jsfile, 'r') as f:
			js = json.loads(f.read())
		return True
	except BaseException as e:
		print(str(e))
		return False

class JsonTest(unittest.TestCase):
	def test_calendar(self):
		self.assertTrue(coba("calendar.json"))
	
	def test_calendar(self):
		self.assertTrue(coba("calendar.min.json"))


if __name__ == '__main__':
	unittest.main()
