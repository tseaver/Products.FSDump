import os
from setuptools import setup
from setuptools import find_packages

NAME = 'FSDump'

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'Products', NAME)

def _package_doc(name):
    f = open(os.path.join(package, name))
    return f.read()

def _doc_file(name):
    f = open(os.path.join('docs', name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = (_doc_file('Overview.rst')
         + _boundary
         + _doc_file('Dumper_editForm.rst')
         + _boundary
         + _doc_file('Mappings.rst')
         + _boundary
         + _doc_file('CHANGES.rst')
         + _boundary
         + "Download\n========"
         )

setup(name='Products.%s' % NAME,
      version=_package_doc('version.txt').strip(),
      description='Dump through-the-web Zope objects to the filesystem',
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        ],
      keywords='web application server zope zope2',
      author="Tres Seaver",
      author_email="tseaver@agendaless.com",
      url="http://pypi.python.org/pypi/Products.FSDump",
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      install_requires=['setuptools',
                       ],
      test_suite='Products.%s' % NAME,
      )
