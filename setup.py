from setuptools import setup, find_packages

with open('VERSION_JENKINS', mode='r') as f:
    VERSION = f.readline().strip()

setup(
    name='moneybook',
    version=VERSION,
    description='편한가계부 PC가계부 API 도구',
    author='Jaeseok Lee',
    author_email='jaeseoklee00@gmail.com',
    packages=find_packages(exclude=['test']),
    setup_requires=[],
    zip_safe=False,
    install_requires=['argparse', 'openpyxl', 'requests', 'furl', 'numpy']
)
