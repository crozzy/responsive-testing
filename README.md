responsive-testing
==================

Django Responsive testing is a collection of tools used to effectively test
responsive website with continually hassling your QA department.


Usage
=====

This is a wrapper for the django.test.LiveServerTestCase that is useful for
testing responsive design features. Requires selenium and a running instance
of xvfb or another Xserver.

Simply subclass LiveServerTestCase and check example.py
