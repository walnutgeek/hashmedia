from setuptools import setup,find_packages
from setuptools.command.sdist import sdist

# MANIFEST.in ensures that requirements are included in `sdist`
install_requires = open('requirements.txt').read().split()
version = open('version.txt').read().strip()



setup(name='hashmedia',
      version=version,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: System :: Archiving :: Backup',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      description='HashStore plugins to display and process media files',
      url='https://github.com/walnutgeek/hashmedia',
      author='Walnut Geek',
      author_email='wg@walnutgeek.com',
      license='Apache 2.0',
      packages=find_packages(exclude=("tests",)),
      package_data={'': ['file_types.json']},
      entry_points={ 'hashstore.plugins' : [
          'FileType=hashmedia:types'
      ]},
      install_requires=install_requires,
      zip_safe=False)