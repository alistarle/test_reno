from setuptools import setup

setup(
    name='test_reno',
    version='0.1',
    command_options={
        'build_reno': {
            'output_file': ('setup.py', 'RELEASENOTES.txt'),
        },
    },
)