import setuptools

# Set Up Meta Data
REQUIRED = ['feedparser', 'QtPy', 'QDarkStyle']

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='ANF Feed Reader',
    version='0.0.1.dev1',
    author='m1ghtfr3e',
    description='Read ANF Feeds',
    keywords='anf, feed, rss',
    long_description=long_description,
    url='https://github.com/m1ghtfr3e/ANF-Feed-Reader',
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    include_package_data = True,
    data_files=[
        ('', ['assets/*'])
    ],
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        ],
    python_requires='>=3',
    project_urls={
        'Source': 'https://github.com/m1ghtfr3e/ANF-Feed-Reader',
        'Bug Reports': 'https://github.com/m1ghtfr3e/ANF-Feed-Reader/issues'
    }
)
