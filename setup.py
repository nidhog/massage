try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description':'MultiAgent System utilities',
	'author':'Ismail Elouafiq',
	'url':'https://github.com/nidhog/massage',
	'download_url':'https://github.com/nidhog/massage/archive/massage.zip',
	'author_email':'i.elouafiq@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['massage'],
	'scripts':[],
	'name':'Massage'
}

setup(**config)