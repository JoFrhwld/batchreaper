from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='batchreaper',
      version='0.1',
      description='runs reaper in batch',
      long_description = readme(),
      url='https://github.com/JoFrhwld/batchreaper',
      author='Josef Fruehwald',
      author_email='jofrhwld@gmail.com',
      license='MIT',
      packages=['batchreaper'],
      scripts=['bin/batchreaper'],
      zip_safe=False)