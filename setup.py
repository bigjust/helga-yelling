from setuptools import setup, find_packages

version = '0.2.1'

setup(name="helga-yelling",
      version=version,
      description=('fights fire with fire'),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='irc bot yelling',
      author='Justin Caratzas',
      author_email='bigjust@lambdaphil.es',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga_yelling'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'yelling = helga_yelling:yelling',
          ],
      ),
)
