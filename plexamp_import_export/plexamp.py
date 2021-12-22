from configparser import ConfigParser
import sys
# import create_ini

HOST = '127.0.0.1'
PORT = 32400
SECTION = 0
BASE_URL = ''
TOKEN = ''
PLEX_PATH = ''
IMPORT_PATH = ''
EXPORT_PATH = ''
SECTION_URL = ''
OVERWRITE = False

# TODO:
def parse_ini(config):
    # server variables:
    HOST        = config.get('server', 'host')
    PORT        = config.getint('server', 'port')
    SECTION     = config.getint('server', 'section_id')
    BASE_URL    = config.get('server', 'base_url')
    TOKEN       = config.get('server', 'token')
    PLEX_PATH   = config.get('server', 'plex_path')

    # import variables
    IMPORT_PATH = config.get('import', 'import_path')
    SECTION_URL = config.get('import', 'section_url')

    # export variables
    EXPORT_PATH = config.get('export', 'export_path')
    OVERWRITE   = config.getboolean('export', 'overwrite')


# TODO:
def import_ratings():
    pass
    """
    when using the playlists, maybe ask for what ratings are all involved in the playlist
    then i can create a dict or something with the file name and ratings?

    or maybe only take a single rating, and add the ability to skip a playlist.
    """


# TODO:
def export_ratings():
    pass


"""
start by looking for the renamed config file
 - if not present, ask if they want a guided setup
   - if not, exit
   - if so, prompt for values
"""
config = ConfigParser()
check = config.read('config.ini')
# print(config.defaults())

if len(check) == 0:
    print('no config.ini found. this is not included by default for privacy. exiting.')
    sys.exit(0)

else:
    print('config.ini found.')
    #TODO: parse the INI, setting variables for use
    parse_ini(config)

"""
then ask if ratings are to be imported or exported
"""

response = ''
while response not in ('I', 'i', 'E', 'e'):
    response = input('import or export? (I/E): ')

if response in ('I', 'i'):
    import_ratings()

else:
    export_ratings()

