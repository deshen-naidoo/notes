"""
Comprehensive unit tests for the notes application.
Covers Models, Full CRUD Views, Validation, and Edge Cases.
"""
from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    """
    Tests the integrity and edge cases of the Note model.
    """
    def setUp(self):
        """Sets up a default note for testing."""
        Note.objects.create(
            title="Setup Note",
            content="Content for setup note."
        )

    def test_note_creation(self):
        """Validates that a note is correctly created in the database."""
        test_note = Note.objects.get(id=1)
        expected_title = "Setup Note"
        self.assertEqual(test_note.title, expected_title)

class NoteViewCRUDTest(TestCase):
    """
    Tests all CRUD operations, routing, and edge cases.
    """
    def setUp(self):
        """Sets up a default note for view testing."""
        self.note = Note.objects.create(
            title="View Test Note",
            content="View test content."
        )

    def test_note_list_view(self):
        """Tests the Read operation (List)."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_detail_view(self):
        """Tests the Read operation (Detail) for a specific note."""
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")

    def test_note_detail_404_edge_case(self):
        """Tests robustness by requesting a note ID that does not exist."""
        response = self.client.get(reverse("note_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_create_view(self):
        """Tests the Create operation via POST request."""
        post_data = {
            "title": "New Post Test",
            "content": "New post content."
        }
        response = self.client.post(reverse("note_create"), data=post_data)
        # 302 signifies a successful redirect after creation
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update_view(self):
        """Tests the Update operation via POST request."""
        update_data = {
            "title": "Updated Title",
            "content": "Updated content."
        }
        response = self.client.post(
            reverse("note_update", args=[self.note.id]), data=update_data
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")

    def test_note_delete_view(self):
        """Tests the Delete operation."""
        response = self.client.post(
            reverse("note_delete", args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)