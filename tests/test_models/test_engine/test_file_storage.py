#!/usr/bin/python3
"""This module tests file_storage.py file.
Usage:
    To be used with the unittest module, can be use it with
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_engine/test_file_storage.py"
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os

my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
           'created_at': '2017-09-28T21:03:54.052298',
           '__class__': 'BaseModel', 'my_number': 89,
           'updated_at': '2017-09-28T21:03:54.052302',
           'name': 'Holberton'}


class TestFileStorage(unittest.TestCase):
    """Unittest for file_storage.py"""
    storage = FileStorage()
    path = storage._FileStorage__file_path
    bm_instance = BaseModel(**my_dict)
    storage.new(bm_instance)

    def test_storage_isinstance(self):
        """Tests if storage is an instance of FileStorage"""
        self.assertIsInstance(TestFileStorage.storage, FileStorage)

    def test_file_json(self):
        """Tests for path existence"""
        TestFileStorage.storage.save()
        self.assertTrue(os.path.exists(TestFileStorage.path))

    def test_save_another_instance(self):
        """Tests for save another instance in path"""
        bm2_instance = BaseModel()
        bm2_instance.save()
        key = type(bm2_instance).__name__ + "." + str(bm2_instance.id)
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            text = f.read()
        self.assertIn(key, text)

class TestFileStorage00(unittest.TestCase):
    """Tests instantiation of FileStorage."""
    def test_01(self):
        """Checks correct with no arguments."""
        fs0 = FileStorage()
        self.assertEqual(type(fs0), FileStorage)

    def test_02(self):
        """Checks correct priv class attr."""
        file_path = FileStorage._FileStorage__file_path
        self.assertEqual(type(file_path), str)

    def test_03(self):
        """Checks correct priv class attr."""
        objects_dict = FileStorage._FileStorage__objects
        self.assertEqual(type(objects_dict), dict)

    def test_04(self):
        """Checks correct storage instantiation."""
        self.assertEqual(type(storage), FileStorage)

    def test_05(self):
        """Checks if error raises."""
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorage01(unittest.TestCase):
    """Check correct implementation of all() method."""
    def test_01(self):
        """Checks for correct type of dict."""
        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def test_02(self):
        """Checks if error raises."""
        with self.assertRaises(TypeError):
            dictionary = storage.all(None)


class TestFileStorage02(unittest.TestCase):
    """Checks correct implementation of new(), save() and reload()
    method."""

    def test_01(self):
        """Checks object type BaseModel newly created in __objects"""
        obj_dict = storage.all()
        bm1 = BaseModel()
        storage.new(bm1)
        key = "BaseModel." + bm1.id
        self.assertIn(key, obj_dict.keys())

    def test_02(self):
        """Checks object type User newly created in __objects"""
        obj_dict = storage.all()
        u1 = User()
        storage.new(u1)
        key = "User." + u1.id
        self.assertIn(key, obj_dict.keys())

    def test_03(self):
        """Checks object type State newly created in __objects"""
        obj_dict = storage.all()
        s1 = State()
        storage.new(s1)
        key = "State." + s1.id
        self.assertIn(key, obj_dict.keys())

    def test_04(self):
        """Checks object type City newly created in __objects"""
        obj_dict = storage.all()
        c1 = City()
        storage.new(c1)
        key = "City." + c1.id
        self.assertIn(key, obj_dict.keys())

    def test_05(self):
        """Checks object type Place newly created in __objects"""
        obj_dict = storage.all()
        p1 = Place()
        storage.new(p1)
        key = "Place." + p1.id
        self.assertIn(key, obj_dict.keys())

    def test_06(self):
        """Checks object type Review newly created in __objects"""
        obj_dict = storage.all()
        r1 = Review()
        storage.new(r1)
        key = "Review." + r1.id
        self.assertIn(key, obj_dict.keys())

    def test_07(self):
        """Checks object type Amenity newly created in __objects"""
        obj_dict = storage.all()
        a1 = Amenity()
        storage.new(a1)
        key = "Amenity." + a1.id
        self.assertIn(key, obj_dict.keys())

    def test_08(self):
        """Checks correct implementation of save() method"""
        obj_dict = storage.all()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        with open("file.json", "r") as sf:
            save_text = sf.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_09(self):
        """Checks correct implementation of reload() method"""
        obj_dict = storage.all()
        storage.reload()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.save()
        storage.reload()
        obj_dict = storage.all()
        self.assertIn("BaseModel." + bm.id, obj_dict.keys())
        self.assertIn("User." + us.id, obj_dict.keys())
        self.assertIn("State." + st.id, obj_dict.keys())
        self.assertIn("Place." + pl.id, obj_dict.keys())
        self.assertIn("City." + cy.id, obj_dict.keys())
        self.assertIn("Amenity." + am.id, obj_dict.keys())
        self.assertIn("Review." + rv.id, obj_dict.keys())

    def test_10(self):
        """Checks if correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_11(self):
        """Checks if correct error Rises."""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_12(self):
        """Checks if correct error Rises."""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_13(self):
        """Checks if correct error Rises."""
        self.assertRaises(FileNotFoundError, storage.reload())

    def test_14(self):
        """Checks if correct error Rises."""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_15(self):
        """Tests reload function"""
        cwd = os.getcwd()
        filename = "file.json"
        mymodel = BaseModel()
        my_obj = mymodel.__class__.__name__ + '.'+mymodel.id
        storage.save()
        self.assertTrue(os.path.exists(filename))
        storage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        self.assertTrue(len(storage.all()) == 0)
        storage.reload()
        all_obj = storage.all()
        self.assertFalse(mymodel == all_obj[my_obj])
        self.assertEqual(mymodel.id, all_obj[my_obj].id)
        self.assertEqual(mymodel.__class__, all_obj[my_obj].__class__)
        self.assertEqual(mymodel.created_at, all_obj[my_obj].created_at)
        self.assertEqual(mymodel.updated_at, all_obj[my_obj].updated_at)

    def test_engine_010(self):
        """Tests reloading with all classes"""
        cwd = os.getcwd()
        filename = "file.json"
        baseobj = BaseModel()
        userobj = User()
        cityobj = City()
        ameobj = Amenity()
        placeobj = Place()
        reviewobj = Review()
        stateobj = State()
        id1 = baseobj.__class__.__name__ + '.' + baseobj.id
        id2 = userobj.__class__.__name__ + '.' + userobj.id
        id3 = cityobj.__class__.__name__ + '.' + cityobj.id
        id4 = ameobj.__class__.__name__ + '.' + ameobj.id
        id5 = placeobj.__class__.__name__ + '.' + placeobj.id
        id6 = reviewobj.__class__.__name__ + '.' + reviewobj.id
        id7 = stateobj.__class__.__name__ + '.' + stateobj.id
        # self.assertFalse(os.path.exists(filename))
        storage.save()
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(len(storage.all()) > 0)
        storage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        clist = [baseobj, userobj, cityobj,
                 ameobj, placeobj, reviewobj, stateobj]
        for i, j in zip(clist, range(1, 7)):
            ids = "id" + str(j)
            self.assertFalse(i == alldic[eval(ids)])
            self.assertEqual(i.id, alldic[eval(ids)].id)
            self.assertEqual(i.__class__, alldic[eval(ids)].__class__)

    @classmethod
    def tearDown(self):
        """Deletes instance file."""
        try:
            cwd = os.getcwd()
            os.remove(cwd + "instance.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
