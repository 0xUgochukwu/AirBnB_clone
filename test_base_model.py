import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    def test_save(self):
        # Create a new instance of BaseModel
        model = BaseModel()
        # Save the initial created_at and updated_at values
        initial_created_at = model.created_at
        initial_updated_at = model.updated_at
        # Call the save() method to update the instance's updated_at value
        model.save()
        # Verify that updated_at was updated after calling save()
        self.assertNotEqual(model.updated_at, initial_updated_at)
        # Verify that created_at remains the same after calling save()
        self.assertEqual(model.created_at, initial_created_at)
if __name__ == '__main__':
    unittest.main()
