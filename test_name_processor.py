import unittest
from classes.names_processor import GreekNameProcessor

class TestGreekNameProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = GreekNameProcessor()

    # Test cases for the get_klitiki method
    def test_get_klitiki_hs(self):
        self.assertEqual(self.processor.get_klitiki("Αλκιβιάδης"), "Αλκιβιάδη")

    def test_get_klitiki_s(self):
        self.assertEqual(self.processor.get_klitiki("Γιάννης"), "Γιάννη")

    def test_get_klitiki_wn(self):
        self.assertEqual(self.processor.get_klitiki("Μενέλαος"), "Μενέλαε")

    def test_get_klitiki_no_suffix(self):
        self.assertEqual(self.processor.get_klitiki("Αλέξανδρος"), "Αλέξανδρε")
    
    # Test cases for the process_names method
    def test_process_names(self):
        self.assertEqual(self.processor.process_names(["Αλέξανδρος", "Μάριος"]), ["Αλέξανδρε", "Μάριε"])

    # Test cases for the process_name method
    def test_process_name(self):
        self.assertEqual(self.processor.process_name("Ανδρέας"), "Ανδρέα")

if __name__ == '__main__':
    unittest.main()
