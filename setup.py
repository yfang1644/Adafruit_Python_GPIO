print('Adafruit GPIO Library')
print('Works best with Python 2.7')
print('THIS INSTALL SCRIPT MAY REQUIRE ROOT/ADMIN PERMISSIONS')

from distutils.core import setup

# Define required packages.
requires = ['adafruit-pureio']

setup(name              = 'Adafruit_GPIO',
      version           = '1.0.4',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Library to provide a cross-platform GPIO interface on the Raspberry Pi and Beaglebone Black using the RPi.GPIO and Adafruit_BBIO libraries.',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_GPIO/',
      install_requires  = requires,
      test_suite        = 'tests',
      packages          = ['Adafruit_GPIO']
     )
