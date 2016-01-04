# encoding: utf-8

from distutils.core import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs
import subprocess
import versioneer


def pkg_config(*args):
    cmd = ['pkg-config']
    cmd.extend(args)
    return subprocess.check_output(cmd).decode().split()

if __name__ == '__main__':
    setup(name='pyjags',
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass(),
          description='Python interface to JAGS library for Bayesian data analysis.',
          author=u'Tomasz Miąsko',
          author_email='tomasz.miasko@gmail.com',
          url='https://github.com/tmiasko/pyjags',
          license='GPLv2',
          classifiers=[
              'Development Status :: 4 - Beta',
              'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
              'Operating System :: POSIX',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Topic :: Scientific/Engineering',
          ],
          packages=['pyjags'],
          ext_modules=[
              Extension(
                  'pyjags.console',
                  include_dirs=['pybind11/include/'] + get_numpy_include_dirs(),
                  libraries=['jags'],
                  define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
                  extra_compile_args=['-std=c++11'] + pkg_config('jags', '--cflags'),
                  extra_link_args=pkg_config('jags', '--libs'),
                  sources=['pyjags/console.cc'])
          ],
          requires=['numpy'])
