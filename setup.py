from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="reader-leon-123",
    version="1.1.0",
    description="Read the latest news from Realpython",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/leon11s/reader",
    author="Leon",
    author_email="test@test.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    packages=["reader"],
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
