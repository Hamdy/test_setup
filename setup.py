import sys
import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# setup.py file is imported while running
# python manage.py {django-command} 
# causing django commands to fail.
disabled = False
if sys.argv and 'manage.py' in sys.argv:
    disabled = True

if not disabled:
    setuptools.setup(
        name='huspy',
        packages=setuptools.find_packages(),
        include_package_data=True,
        version='0.1.0',
        license='MIT',
        description='Huspy  SDK',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='Hamdy Farag',
        author_email='hamdy@huspy.io',
        url='https://github.com/huspy/crm-sdk.git',
        install_requires=[
            'Django>=4.0.0',
            'djangorestframework>=3.0.0',
            'hubspot-api-client==5.0.1',
            'ujson==5.2.0',
        ],  # list all packages that your package uses
        keywords=["huspy", "sdk"],  # descriptive meta-data
        classifiers=[  # https://pypi.org/classifiers
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Documentation',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],

        download_url="https://github.com/mike-huls/toolbox_public/archive/refs/tags/0.0.3.tar.gz",
    )

