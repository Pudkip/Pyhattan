from setuptools import setup, find_packages

setup(name='Pyhattan',
      version='0.1',
      description='Manhattan Plots in Python',
      url='http://github.com/pudkip/Pyhattan',
      author='James Biller',
      license='MIT',
      classifers={
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7'
      },
      packages=find_packages(),
      install_requires=['pandas', 'numpy', 'matplotlib'],
      zip_safe=False)


