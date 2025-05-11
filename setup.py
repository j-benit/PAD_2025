from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Jhon Benitez",
    author_email="jhon.benitez@est.iudigital.edu.co",
    description="Scraping laptops desde Mercado Libre",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "scrape-laptops=main:main"
        ]
    },
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "selenium",
        "webdriver-manager"
    ],
)