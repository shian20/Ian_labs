import logging
import re
import shutil
import sys
import argparse
import requests
import json
from pathlib import Path
from datetime import datetime

log = logging.getLogger('bulk_renamer')
logging.basicConfig(
    level=logging.INFO,
    format=(
        '[%(asctime)s] %(levelname)s %(module)s '
        '%(funcName)s:%(lineno)d - %(message)s'
    ),
)


def ian_gateway(api_url, input_param):
    response = requests.post(api_url, data=json.dumps(input_param))
    # pdb.set_trace()
    print(response)


def search_files(pat, target_dir):
    found = []
    substring = pat
    folder_path = Path(target_dir).glob('**/*')
    for files in folder_path:
        if re.match(substring, Path(files).name):
            found.append(Path(files).name)

    log.info(f'Searching for files in {target_dir}')
    log.debug(f'pat - {pat}')
    log.debug(f'target_dir - {target_dir}')
    log.debug(f'found - {found}')
    log.info(f'Found {len(found)} files!')
    return found


def rename_file(name_change, old_file_name, directory_container):
    count = 1
    path = directory_container
    folder_path = Path(path).glob('**/*')
    substring = old_file_name

    for files in folder_path:
        if re.match(substring, Path(files).name):
            source = path+'/'+Path(files).stem+Path(files).suffix
            destination = path + '/' + name_change + '_' +\
                str(count) + Path(files).suffix
            new_name = Path(destination)
            if new_name.exists():
                while(new_name.exists()):
                    log.info(f'{new_name.name} exists.'
                             'Finding available index')
                    destination = path + '/' + name_change + \
                        str(count) + Path(files).suffix
                    count += 1
            shutil.move(source, destination)
            count += 1
            log.info(f'File name {Path(files).name} is now {new_name.name}')
            log_level = "CRITICAL"
            msg = "Files has been renamed. process ended"
            input_params = api_info(log_level, msg)
            log.info(msg)
            ian_gateway(api_url, input_params)


def api_info(loglvl, note):
    parameters = {
        "email": "adrian.arcilla@globe.com.ph",
        "log_level": loglvl,
        "msg": note,
    }

    return parameters


def log_formatting(log_level, msg):
    str_form = '[' + datetime.now().strftime("%d-%m-%y %H:%M:%S") + '] ' + __file__ + ' ' + log_level + ' - ' + msg
    return str_form


def main(xargs):
    log.info('Start processing...')
    log.debug(f'xargs.new_name - {xargs.new_name}')
    log.debug(f'xargs.filter_pat - {xargs.filter_pat}')
    log.debug(f'xargs.target_dir - {xargs.target_dir}')
    search_files(xargs.filter_pat, xargs.target_dir)

    log_level = "WARNING"
    msg = "Files has been found"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)

    log_level = "ERROR"
    msg = "Files will be renamed"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)

    rename_file(xargs.new_name, xargs.filter_pat, xargs.target_dir)

    if not Path(xargs.target_dir).exists():
        log.error(f'xargs.target_dir "{xargs.target_dir}" does not exist.')
        print(f'The directory "{xargs.target_dir}" does not exist!')
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':

    api_url = "https://dzkeujmt32.execute-api.us-east-1.amazonaws.com"\
              "/default/lambda_function_ian"

    log_level = "INFO"
    msg = "Application started"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)

    parser = argparse.ArgumentParser()
    parser.add_argument('new_name', help=('The new name of the files.'
                        'This will be appended with a number.'))
    parser.add_argument('filter_pat', help='The name pattern to search.')
    parser.add_argument('target_dir', help='The directory to search.')
    xargs = parser.parse_args()

    log_level = "DEBUG"
    msg = "Arguments accepted"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)

    main(xargs)
