import os
from configparser import ConfigParser


def parse_config(filename='db.ini', section='test'):
    # initialise a parser object
    parser = ConfigParser()
    # read the ini file
    parser.read(filename)

    # get section default to test
    db = {}
    # try to locate the section using the parser
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
