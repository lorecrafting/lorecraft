r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *
import os

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "lorecraft"

INSTALLED_APPS += ('django_svelte',)

# Path to the lib directory containing the bulk of the codebase's code.
EVENNIA_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the game directory (containing the server/conf/settings.py file)
# This is dynamically created- there is generally no need to change this!
if EVENNIA_DIR.lower() == os.getcwd().lower() or (
    sys.argv[1] == "test" if len(sys.argv) > 1 else False
):
    # unittesting mode
    GAME_DIR = os.getcwd()
else:
    # Fallback location (will be replaced by the actual game dir at runtime)
    GAME_DIR = os.path.join(EVENNIA_DIR, "game_template")
    for i in range(10):
        gpath = os.getcwd()
        if "server" in os.listdir(gpath):
            if os.path.isfile(os.path.join("server", "conf", "settings.py")):
                GAME_DIR = gpath
                break
        os.chdir(os.pardir)

#include svelte managed webclient output files
STATICFILES_DIRS += [os.path.join(GAME_DIR, "svelte", "public", "build")]

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
