#!/usr/bin/python
""" This is a wrapper for the django.test.LiveServerTestCase
    that is useful for testing responsive design features.
    Requires selenium and a running instance of xvfb or
    another Xserver.
"""

import collections
import contextlib
import os

import django.test
import django.test.client

from selenium import webdriver

class LiveServerTestCase(django.test.LiveServerTestCase):

    D = collections.namedtuple('dimention', ('width', 'height'))
    DIMENTIONS = {'phone': D(328, 480),
                  'tablet': D(768, 1024),
                  'desktop': D(1280, 800),
                 }
    BROWSER = 'firefox'
    XVFB_DISPLAY = 90

    @classmethod
    def setUpClass(cls):
        os.environ.update({'DISPLAY': cls.XVFB_DISPLAY})
        cls.selenium = cls.set_browser_driver()
        super(LiveServerTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        os.environ.clear('DISPLAY')
        cls.selenium.quit()
        super(LiveServerTestCase, cls).tearDownClass()

    @classmethod
    def set_browser_driver(cls):
        """Set the driver to use
        Note: Not mutable once test class instanciated
        """
        return eval('webdriver.%s.webdriver.WebDriver()' % cls.BROWSER)

    @contextlib.contextmanager
    def device(self, device):
        """Context manager use as follows:
        with device('phone'):
            *assertions*
        """
        old_width, old_height = self.selenium.get_window_size().values()
        try:
            self._set_device(device)
            yield
        finally:
            self.selenium.set_window_size(old_width, old_height)

    def _set_device(self, device):
        self.selenium.set_window_size(self.DIMENTIONS[device].width,
                                      self.DIMENTIONS[device].height)
