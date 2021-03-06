import pytest
import unittest

from modules.sfp_dronebl import sfp_dronebl
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleDronebl(unittest.TestCase):

    def test_opts(self):
        module = sfp_dronebl()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        sf = SpiderFoot(self.default_options)
        module = sfp_dronebl()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_dronebl()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_dronebl()
        self.assertIsInstance(module.producedEvents(), list)
