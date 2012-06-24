from distutils.core import setup, Extension
import os

ext_sock = Extension('pydev_socket',
    sources = ['Modules/socketmodule.c'],
    language = 'c'
)

ext_time = Extension('pydev_time',
    sources = ['Modules/timemodule.c'],
    language = 'c'
)

ext_thread = Extension('pydev_thread',
    sources = ['Modules/threadmodule.c'],
    language = 'c'
)

ext_select = Extension('pydev_select',
    sources = ['Modules/selectmodule.c'],
    language = 'c'
)

setup(name='PyCharm debugger libraries', version='1.0', description='Python libraries required for PyCharm debugger', 
    ext_modules=[ext_sock, ext_time, ext_thread, ext_select],
    py_modules = ['_pydev_threading', '_pydev_BaseHTTPServer', '_pydev_Queue', '_pydev_SocketServer']
    )
