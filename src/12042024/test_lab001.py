#  Logging means - Capture details, which are useful while debugging
#  and show the user details aboutexcution of program.

# Warning to the users
# Information to the user
# Errors, Critical Errors User.

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    # International Logging to User
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
    assert True == True
