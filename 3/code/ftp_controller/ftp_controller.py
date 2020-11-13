import os
from ftplib import FTP


class FTPController:

    IGNORE_LIST = [
        'idea',
        '__pycache__',
        '__init__'
    ]

    @staticmethod
    def get_directory_list_and_size(host: str, port: int, user: str, passwd: str):
        ftp = FTP()
        ftp.connect(host, port=port)

        #ftp.login(user=user, passwd=passwd)
        ftp.sendcmd('USER ' + user)
        ftp.sendcmd('PASS ' + passwd)

        def get_dirs_ftp(folder="", final_size=0, size_to_each_type={}):
            contents = ftp.nlst(folder)
            folders = []
            for item in contents:
                joined = os.path.join(folder, item)

                # Ignore some folders
                ignore = False
                for ignore_name in FTPController.IGNORE_LIST:
                    if ignore_name in item:
                        ignore = True

                if ignore:
                    continue

                # Save folder
                if "." not in item:
                    folders.append(joined)
                    continue
                # Write size of the file
                if '.' in item:
                    ftp.voidcmd('TYPE i')
                    cur_type = item.split('.')[-1]

                    # The SIZE command is defined in RFC-3659, i.e. with prefix '213'
                    #cur_size = ftp.size(joined)
                    cur_size = int(ftp.sendcmd('SIZE ' + joined)[3:].strip())

                    if size_to_each_type.get(cur_type) is None:
                        size_to_each_type[cur_type] = cur_size
                    else:
                        size_to_each_type[cur_type] += cur_size

                    final_size += cur_size
            return folders, final_size

        def get_all_dirs_ftp(folder="\\"):
            dirs = []
            size_to_each_type = {}

            new_dirs, final_size = get_dirs_ftp(folder, final_size=0, size_to_each_type=size_to_each_type)
            while len(new_dirs) > 0:
                for dir in new_dirs:
                    dirs.append(dir)

                old_dirs = new_dirs[:]
                new_dirs = []
                for dir in old_dirs:
                    new_folders, new_size = get_dirs_ftp(dir, final_size=0, size_to_each_type=size_to_each_type)
                    final_size += new_size
                    for new_dir in new_folders:
                        new_dirs.append(new_dir)
            dirs.sort()
            return dirs, final_size, size_to_each_type

        allfiles, final_size, size_to_each_type = get_all_dirs_ftp()

        return allfiles, final_size, size_to_each_type

