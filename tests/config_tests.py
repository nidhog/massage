from nose.tools import *
from massage.config import default_host
from massage.config import default_port

def host_is_localhost():
	assert_equal(default_host, 'localhost')