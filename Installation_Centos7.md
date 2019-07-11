# Download and install python3 from the source.
===============================================================================
Follow the instruction below to install python from the source.

```bash
$ sudo su -
[root] $ yum groupinstall -y "development tools"
[root] $ yum install -y \
  libffi-devel \
  zlib-devel \
  bzip2-devel \
  openssl-devel \
  ncurses-devel \
  sqlite-devel \
  readline-devel \
  tk-devel \
  gdbm-devel \
  db4-devel \
  libpcap-devel \
  xz-devel \
  expat-devel

[root ] $ cd /usr/src
[root ] $ wget http://python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
[root ] $ tar xf Python-3.6.4.tar.xz
[root ] $ cd Python-3.6.4
[root ] $ ./configure --enable-optimizations
[root ] $ make altinstall
[root ] $ exit
```

Important:
Make altinstall causes it to not replace the built in python executable.

Ensure secure_path in /etc/sudoers file includes /usr/local/bin . The line should look like below

```bash
Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin
```

### Upgrade Pip (might not be necessary)
The version of pip that we have might be up-to-date, but it’s good practice to try to update it after the installation. We need to use the pip3.6 executable because we’re working with Python 3, and we use sudo so that we can write files under the /usr/local directory.

```bash
$ sudo pip3.6 install --upgrade pip
```

End
