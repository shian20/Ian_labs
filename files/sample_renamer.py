import os.path
import argparse
import logging
import re
import glob
import shutil
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description="Renaming process of bulk files.", epilog="Created by Adrian Arcilla")

parser.add_argument("new_name", type=str, help="Files matching 'file_pattern' will be renamed with this value. An incrementing count will also be added.")

parser.add_argument("file_pattern", help="Files to rename (Regex compatible).")

parser.add_argument("target_dir", type=Path, help="Directory where the files to rename reside.")

parser.add_argument("-L", "--log-level", dest='logs', metavar="LOG_LEVEL", default=logging.INFO, help="Set log level.")

parser.add_argument("--copy", dest='copy', help="Copy files instead of just renaming them.", action='store_const', const=False, default=False)

args = parser.parse_args()
newName = args.new_name
targetDir = args.target_dir
# destination = args.target_dir + "/" + args.new_name
pattern = args.file_pattern
logLevel = args.logs
rootDir = Path('.' / targetDir)

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(filename)s %(lineno)d - %(message)s', level=logging.INFO)

try:
    i = 1
    # for source in rootDir.glob(pattern):
    res = [s for s in glob.glob(f'{rootDir}/*') if re.search(pattern, s)]
    for source in res:
        sourceFile = os.path.basename(source)

        if args.copy:
            file = shutil.copy(source, f'./{rootDir}/{newName}{i}')
            copyFile = os.path.basename(file)
            logging.info(f'Copied {sourceFile} -> {copyFile}')

        else:
            file = shutil.move(source, f'./{rootDir}/{newName}{i}')
            newFile = os.path.basename(file)
            logging.info(f'Renamed {sourceFile} -> {newFile}')

        i += 1
    sys.exit(0)

except (SystemError) as e:
    print(e)
    sys.exit(1)
