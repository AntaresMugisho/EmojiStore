# This file uses the following encoding : utf-8

from distutils.core import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='EmojiStore',
    packages=['EmojiStore'],
    version='1.0',
    license='MIT',
    description='A python package that stores all unicode emojis grouped by category !',
    long_description=long_description,
    author='Antares Mugisho',
    author_email='antaresmugisho@gmail.com',
    url='https://antaresmugisho.vercel.app/',
    download_url='https://github.com/AntaresMugisho/EmojiStore/archive/refs/tags/v1.0-alpha.tar.gz',
    keywords=['python', 'emoji', 'sticker', 'mood'],
    install_requires=[
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
