from setuptools import setup, find_packages

setup(
    name="GitBookToPDF",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pdfkit"
    ],
    entry_points={
        "console_scripts": [
            "gitbook_to_pdf=gitbook_to_pdf:main",
        ],
    },
)
