from __future__ import print_function
"""gameuniterror

Shows how to create a custom exception class for the Attack of the Orcs game

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The use of this module is illustrated in Chapter 2, exception handling.

RUNNING THE PROGRAM:
--------------------
This is NOT run as a standalone program. See `attackoftheorcs_v_1_1.py`

# --------------------------------------------------------------------------
# Alternate implementation where you subclass the custom exception,
# GameUniError. The following code would eliminate the need of
# maintaining an error_dict object in GameUnitError. See the chapter for
# further details.
# --------------------------------------------------------------------------
# class GameUnitError(Exception):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.padding = '~'*50 + '\n'
#         self.error_message = " Unspecified Error!"
#
# class HealthMeterException(GameUnitError):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.error_message = (self.padding +
#                              "ERROR: Health Meter Problem" +
#                              '\n' + self.padding )
#
# class AttackException(GameUnitError):
#     # Code similar to that of HealthMeterException .
#     pass

.. seealso:: `attackoftheorcs_v_1_1.py`, `heal_exception_example.py`

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses"""    
    def __init__(self, message='', code=000):
        super().__init__(message)
        self.padding = '~'*50 + '\n'
        self.error_message = "Unspecified Error!"

class HealthMeterException(GameUnitError):
    "Custom exception to report Health Meter related problems"
    def __init__(self, message=" "):
        super().__init__(message)
        self.error_message = (self.padding + 
                              "ERROR: Health Meter Problem "+
                              '\n' + self.padding)

class HutNumberGreaterThatFiveError(GameUnitError):
    def __init__(self, message=" "):
        super().__init__(message)
        self.error_message = (self.padding + 
                        "ERROR: Hut number greater than 5 "+
                        '\n' + self.padding)

class HutNumberNegativeError(GameUnitError):
    def __init__(self, message=" "):
        super().__init__(message)
        self.error_message = (self.padding + 
                        "ERROR: Hut number smaller than 1 "+
                        '\n' + self.padding)


