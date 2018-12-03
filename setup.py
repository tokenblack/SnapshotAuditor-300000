from setuptools import setup

setup(
	name='SnapshotAuditor-30000',
	version='0.1',
	author="Mawande M., a.k.a tokenblack",
	author_email="mistermadolo@gmail.com",
	description="SnapshotAuditor 30k is tool to manage AWS EC2 snapshots.",
	license="GPLv3",
	package=['scripts'],
	url="https://github.com/tokenblack/SnapshotAuditor-300000",
	install_requires=['click', 'boto3'],
	entry_points=
		'''
		[console_scripts]
		tokenblack=scripts.ls_instances.py:cli
		''',
		
)
