from setuptools import setup

setup(
    name='tfidf',
    version='0.0.4',
    url='http://github.com/17zuoye/tfidf/',
    license='MIT',
    author='David Chen',
    author_email=''.join(reversed("moc.liamg@emojvm")),
    description='tfidf',
    long_description='tfidf',
    packages=['tfidf'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'etl_utils',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
