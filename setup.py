from setuptools import setup

setup(
    name='tftp-log-collector',
    version='0.1.0',
    python_requires='>=3.5',
    install_requires=['ptfpd'],
    scripts=['log_collector.py'],
)
