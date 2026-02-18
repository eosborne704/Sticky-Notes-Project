from django.test import TestCase
from django.urls import reverse
from notes.models import Note, User

# Create your tests here.
class NotesModelTest(TestCase):
    """
    Tests different components of
    the model
    """
    def setUp(self):
        user = User.objects.create(name='Test User')
        Note.objects.create(title='Test Note', content='Test Content',
                            user=user)
    def test_notes_has_title(self):
        """
        Test for whether a Note object
        renders a title
        """
        # Checks that a Note object has a
        # title renders
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_notes_has_content(self):
        """
        Test for whehter a Note object
        renders a description
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'Test Content')

class NotesViewTest(TestCase):
    """
    Tests whether the view's different components work
    """


    def setUp(self):
        """
        Initiates test for
        parts of the view
        """
        self.user = User.objects.create(name='Test User')
        Note.objects.create(title='Test Note', content='A test note',
                            user=user)

    def test_all_notes_view(self):
        """
        Tests whether the list of all notes
        renders
        """
        response = self.client.get(reverse('all_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')


    def test_view_note_view(self):
        """
        Tests whether a single note can be
        viewed
        """
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('view_note',
                        args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'A test note')