from setuptools import setup

setup(
    name='hodp_templates',
    version='0.1.0',
    description='Templates for python data visualizations developed for the Harvard Open Data Project',
    url='https://github.com/jladan/package_demo',
    author='Kevin Huang',
    author_email='kevin_huang@college.harvard.edu',
    packages=[
        'hodp_templates',
        'hodp_templates.plotly'
    ],
    install_requires=[
        'plotly'
    ],
    license='MIT',
    long_description=open('README.md').read(),
)
