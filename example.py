#!/usr/bin/python

from responsive_testing import LiveServerTestCase
from django.core.urlresolvers import reverse

class ResponsiveTests(LiveServerTestCase):

    BROWSER = 'chrome'

    def livetest_responsive_render(self):
        with self.device('desktop'):
            self.selenium.get(self.live_server_url + reverse('use'))
            menu = self.selenium.find_element_by_class_name('menu-class')
            assert menu.is_displayed() == True
        with self.device('phone'):
            self.selenium.get(self.live_server_url + reverse('use'))
            menu = self.selenium.find_element_by_class_name('menu-class')
            assert menu.is_displayed() == False

    def livetest_register_error_messages(self):
        self.selenium.get(self.live_server_url + reverse('register'))
        self.do_register_process('invalid@email', 'secret')
        e = self.selenium.find_element_by_class_name('error')
        assert e.is_displayed() == True
        assert e.text == (u"The email address must be in the format"
                          u" \u201cname@example.com\u201d")
