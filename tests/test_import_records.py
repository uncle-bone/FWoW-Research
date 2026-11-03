import unittest
from tools.import_records import normalize
class Tests(unittest.TestCase):
 def test_record(self):
  r=normalize({"id":123,"source_url":"https://example.org","observed_build":"1.60.1.69893","method":"local","license":"original"},"items")
  self.assertEqual(r["id"],"123")
  self.assertEqual(len(r["record_key"]),20)
 def test_missing_source(self):
  with self.assertRaises(ValueError): normalize({"id":1},"items")
 def test_reject_confidence(self):
  with self.assertRaises(ValueError): normalize({"id":1,"source_url":"x","observed_build":"x","method":"x","license":"x","confidence":"verified"},"items")
if __name__=="__main__": unittest.main()
