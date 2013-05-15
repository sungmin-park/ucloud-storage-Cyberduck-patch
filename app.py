# -*- coding: utf-8 -*-
from os import path
from biplist import readPlist, writePlist
from subprocess import call

PLIST = path.expanduser('~/Library/Preferences/ch.sudo.cyberduck.plist')
DATA = {
    'ssproxy.ucloudbiz.olleh.com.certificate.accept':
    'CN=*.ucloudbiz.olleh.com, OU=Cloud Business Department, O=KT, '
    'L=Seongnam-si, S=Gyeonggi-do, C=KR',
    'cf.authentication.context': '/auth/v1.0'
}


def alert(message):
    call(
        "/usr/bin/osascript -e 'tell app \"System Events\" to display alert"
        "\"%s\"'" % message,
        shell=True
    )


def run():
    data = readPlist(PLIST)
    data.update(DATA)
    writePlist(data, PLIST)
    alert(u"패치되었습니다.")

if __name__ == '__main__':
    run()
