from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='devforge-cli',  # Changed to avoid name conflict
    version='1.0.1',  # Version bump for colorful output and version command
    description='Universal project scaffolder for React, FastAPI, and Flutter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Isaka Mtweve',
    author_email='isakamtweve69@gmail.com',
    url='https://github.com/isaka-12/devforge',
    project_urls={
        'Bug Reports': 'https://github.com/isaka-12/devforge/issues',
        'Source': 'https://github.com/isaka-12/devforge',
        'Documentation': 'https://github.com/isaka-12/devforge#readme',
    },
    packages=find_packages(exclude=['tests*', 'docs*']),
    install_requires=[
        'click>=8.0.0',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'devforge=devforge.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
    keywords='scaffolding, code generator, react, fastapi, flutter, cli, boilerplate',
    license='MIT',
)
