from setuptools import setup

setup(name='plexamp_import_export',
      version='0.1',
      description='importing and exporting ratings',
      url='https://github.com/educatedCaveman/plexamp_import_export',
      author='educated_caveman',
      author_email='j.drake.hoffman@gmail.com',
      license='MIT',
      packages=['plexamp_import_export'], 
      install_requires=[
          'plexapi',
          'tabulate',
      ],
      zip_safe=False)