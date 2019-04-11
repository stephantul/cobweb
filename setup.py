# -*- coding: utf-8 -*-
"""Setup file."""
from setuptools import setup, find_packages


setup(name='cobweb',
      version="0.0.1",
      description='Cobweb diagrams',
      author='Stéphan Tulkens',
      author_email='stephan.tulkens@uantwerpen.be',
      url='https://github.com/stephantul/cobweb',
      license='gplv3',
      packages=find_packages(exclude=["images"]),
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3'],
      keywords='computational psycholinguistics neural networks',
      zip_safe=True)
