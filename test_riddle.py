"""Unit tests for riddle-me-this.py"""

import unittest
from riddle_me_this import Riddle

class TestRiddle(unittest.TestCase):
    """Tests for the Riddle class."""

    def test_riddle_initialization(self):
        """Test that a Riddle object is initialized correctly."""
        r = Riddle("What has keys but can't open locks?", "piano")
        self.assertEqual(r.getRiddle(), "What has keys but can't open locks?")
        self.assertEqual(r.getAnswer(), "piano")

    def test_riddle_answer(self):
        """Test that getAnswer returns the correct answer."""
        r = Riddle("What has a heart but no other organs?", "artichoke")
        self.assertEqual(r.getAnswer(), "artichoke")

if __name__ == '__main__':
    unittest.main()