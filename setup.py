from setuptools import setup, find_packages

setup(
    name="anujscan",
    version="1.0.0",
    description="AnujScan - A CLI Penetration Testing Toolkit",
    author="Anuj Prajapati",
    packages=find_packages(),
    include_package_data=True,  # ✅ include data files from MANIFEST
    install_requires=[
        "requests",
        "python-whois"
    ],
    entry_points={
        "console_scripts": [
            "anujscan=anujscan.toolkit:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
