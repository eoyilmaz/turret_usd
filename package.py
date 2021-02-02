# -*- coding: utf-8 -*-

name = 'turret_usd'

version = '1.1.11'

authors = [ 'ben.skinner',
            'daniel.flood',
            'wen.tan' ]

requires = [
    'turret_lib-1.1.22+<2',
    'PyOpenGL-3.1.0',
    'jemalloc-4',
    'jinja',
]

private_build_requires = [
    'cmake-3.16',
]

variants = [
	# ['platform-linux', 'arch-x86_64', 'usd-0.8.5'],
	# ['platform-linux', 'arch-x86_64', 'usd-18.09'],
	# ['platform-linux', 'arch-x86_64', 'usd-18.11'],
	# ['platform-linux', 'arch-x86_64', 'usd-19.01'],
	# ['platform-linux', 'arch-x86_64', 'usd-19.07'],
	# ['platform-linux', 'arch-x86_64', 'usd-19.11'],
	# ['platform-linux', 'arch-x86_64', 'usd-20.02'],
	# ['platform-linux', 'arch-x86_64', 'houdini-18.0'],
    ['platform-linux', 'arch-x86_64', 'houdini-18.5.351', 'devtoolset-9']
	## ['platform-linux', 'arch-x86_64', 'nuke-12.2.1'],
    # ['platform-linux', 'arch-x86_64', 'KatanaUsdPlugins-19.11.3.1', 'katana-3.6.2', 'tbb_katana']
    #['platform-linux', 'arch-x86_64', 'multiverse-6.6']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/plugin')
    env.PXR_PLUGINPATH_NAME.append('{root}/plugin/usd/')
    
