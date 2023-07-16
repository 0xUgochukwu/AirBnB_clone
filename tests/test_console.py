import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
import json
from datetime import datetime


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.file_path = "file.json"

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_create_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_create_with_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create MyModel")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_create_and_show_instance(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create BaseModel")
            output = output.getvalue().strip()
            self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd(f"show BaseModel {output}")
            self.assertIn(output, output.getvalue())

    def test_show_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_show_with_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show MyModel")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_show_with_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_show_with_nonexistent_instance(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show BaseModel 121212")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_destroy_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_destroy_with_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy MyModel")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_with_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_destroy_with_nonexistent_instance(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy BaseModel 121212")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_update_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("update")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_update_with_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("update MyModel")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_update_with_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("update BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_update_with_nonexistent_instance(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("update BaseModel 121212")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_update_with_missing_attribute_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create BaseModel")
            instance_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd(f"update BaseModel {instance_id}")
            self.assertEqual(output.getvalue().strip(), "** attribute name missing **")

    def test_update_with_missing_value(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create BaseModel")
            instance_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd(f"update BaseModel {instance_id} first_name")
            self.assertEqual(output.getvalue().strip(), "** value missing **")

    def test_all_with_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("all MyModel")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create BaseModel")
            instance_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("all BaseModel")
            self.assertIn(instance_id, output.getvalue())


if __name__ == "__main__":
    unittest.main()

