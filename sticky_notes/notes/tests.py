"""
This module contains unit tests for the notes application.
It validates models, views, and form logic.
"""

from django.test import TestCase
from django.urls import reverse
# Update this import based on your model name. 
# If your model is named 'Note', use this:
from .models import Note 

class NoteModelTest(TestCase):
    """
    Tests the integrity of the Note model.
    """
    def setUp(self):
        """
        Sets up the test environment by creating a test Note object.
        """
        Note.objects.create(
            title='Test Title', 
            content='Test content for the sticky note.'
        )

    def test_note_has_expected_title(self):
        """
        Ensures the Note object returns the correct title.
        """
        test_note = Note.objects.get(id=1)
        expected_title = 'Test Title'
        self.assertEqual(test_note.title, expected_title)

    def test_note_has_expected_content(self):
        """
        Ensures the Note object returns the correct content.
        """
        test_note = Note.objects.get(id=1)
        expected_content = 'Test content for the sticky note.'
        self.assertEqual(test_note.content, expected_content)

class NoteViewTest(TestCase):
    """
    Tests the CRUD views for the Sticky Notes application.
    """
    def setUp(self):
        """
        Sets up the test environment with a note.
        """
        Note.objects.create(
            title='Test Title', 
            content='Test content.'
        )

    def test_note_list_view_status_code(self):
        """
        Tests that the list view returns a 200 OK status.
        """
        # Change 'note_list' to whatever you named your URL in urls.py
        url_name = 'note_list'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)