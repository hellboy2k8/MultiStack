"""
Provides base class for working with different Cloud providers
"""


class BaseProvider:
	"""
	Implement a general interface for hanlding multiple cloud
	providers.

	The Provider object provides set of common methods to handle
	provider specific operations in abstracted way.
	"""

	self.conn = None
	self.keypair = None
	self.master_security_group = None
	self.slave_security_group = None

	def __init__(name, credentials):
		self.conn = self._connect(credentials)
		self.keypair = ('multistack-{0}'.format(name))
		self.master_security_group = ('multistack-{0}-master'.format(name))
		self.slave_security_group = ('multistack-{0}-slave'.format(name))

	def _connect(self, credentials):
		raise NotImplementedError('Connect not implemented for this Provider')

	def boot_instances():
		raise NotImplementedError

	def create_keypair():
		raise NotImplementedError

	def create_security_groups():
		raise NotImplementedError

	def release_public_ips():
		raise NotImplementedError

	def release_public_ip():
		raise NotImplementedError

	def associate_public_ip():
		raise NotImplementedError
