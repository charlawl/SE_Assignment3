from setuptools import setup

setup(name="lightbox",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Charlotte Hearne",
      author_email="charlotte.hearne@ucdconnect.ie",
      licence="GPL3",
      packages=['light_box'],
      test_suite="tests",
      entry_points={
        'console_scripts': ['light_box=light_box.main:main']
        },
      requires = ['requests']
      )