from setuptools import setup, find_packages
from distutils.util import convert_path

namespace = {}
version_path = convert_path('source/pdf_play/_version.py')

with open(version_path) as f:
    content = f.read()
    print(exec(content, namespace))
    # exec(f.read(), namespace)

print(f'NS: {namespace}')

setup(version=namespace.get('VERSION', '12345'))
