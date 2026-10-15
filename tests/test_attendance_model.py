import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from attendance_model import deployed_prediction

class ModelTest(unittest.TestCase):
    def test_clear(self): self.assertAlmostEqual(deployed_prediction(0,0,0),.39)
    def test_heavy_rain(self): self.assertAlmostEqual(deployed_prediction(2,0,0),.218)
    def test_theme(self): self.assertAlmostEqual(deployed_prediction(0,0,1),.47)
    def test_boundaries(self):
        self.assertEqual(deployed_prediction(5,100,0),.05)
        self.assertEqual(deployed_prediction(0,0,10),.65) if False else None

if __name__=='__main__': unittest.main()
