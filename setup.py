from setuptools import setup, find_packages

setup(
    name="SentinelOps",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": ["pytest"],
    },
    entry_points={
        "console_scripts": [
            "sentinelops=core.sentinel:main",
        ]
    },
)
