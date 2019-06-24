# WtStat python modules

import logging
logging.basicConfig(level=logging.INFO, format="{:15}  %(levelname)s  %(message)s".format("[%(name)s]"))
logging.addLevelName(logging.WARNING, "\033[1;31m{:8}\033[1;0m".format(logging.getLevelName(logging.WARNING)))
logging.addLevelName(logging.ERROR, "\033[1;35m{:8}\033[1;0m".format(logging.getLevelName(logging.ERROR)))
logging.addLevelName(logging.INFO, "\033[1;32m{:8}\033[1;0m".format(logging.getLevelName(logging.INFO)))
logging.addLevelName(logging.DEBUG, "\033[1;34m{:8}\033[1;0m".format(logging.getLevelName(logging.DEBUG)))
