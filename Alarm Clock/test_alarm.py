import unittest
import alarm_clock
from datetime import *


class MyTestCase(unittest.TestCase):
    def test_alarm(self):
        current_time = datetime.now()
        min = current_time.minute
        hour = current_time.hour

        current_time_as_string = str(hour) + ":" + str(min)
        self.assertEqual(
            False, alarm_clock.alarm(current_time_as_string)
        )  # add assertion here


if __name__ == "__main__":
    unittest.main()
