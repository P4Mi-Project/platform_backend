import unittest
from services.CourseService import CourseService
import traceback
import asyncio

class CourseServiceTest(unittest.TestCase):
    def setUp(self):
        self.course_service = CourseService()
    def test_get_courses(self):
        res = self.course_service.get_courses()

        self.assertNotEqual(len(res),0)