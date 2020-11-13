from ftplib import FTP


def main():
    ftp = FTP()
    ftp.connect('localhost', port=8080)

    ftp.login(user='lokesh', passwd='123')
    print(ftp.pwd())
    ftp.retrlines('LIST')

    def get_dirs_ftp(folder=""):
        contents = ftp.nlst(folder)
        print(contents)
        folders = []
        for item in contents:
            if "." not in item:
                folders.append(item)
            elif '.' in item and 'idea' not in item:
                print('item: ' + item + '   size: ' + str(ftp.size(item)))
        return folders

    def get_all_dirs_ftp(folder=""):
        dirs = []
        new_dirs = []
        new_dirs = get_dirs_ftp(folder)
        while len(new_dirs) > 0:
            for dir in new_dirs:
                dirs.append(dir)

            old_dirs = new_dirs[:]
            new_dirs = []
            for dir in old_dirs:
                for new_dir in get_dirs_ftp(dir):
                    new_dirs.append(new_dir)
        dirs.sort()
        return dirs

    allfiles = get_all_dirs_ftp()
    print(allfiles)


if __name__ == '__main__':
    main()
