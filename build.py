# -*-coding:utf8;-*-
from datetime import date, datetime
from termcolor import cprint
import holidays
import json

"""
script untuk auto generate api.json.
author: guangrei
"""

list_libur = holidays.ID()
libur_prefix = ("raya", "natal", "tahun baru", "cuti", "fitri")
credit = {
    "updated": datetime.now().strftime("%Y%m%d %H:%I:%S"),
    "author": "guangrei",
    "link": "https://github.com/guangrei"}


def check_libur(tanggal, deskripsi, list_pref):
    if date(tanggal.year, tanggal.month, tanggal.day) in list_libur:
        cprint(
            f'{tanggal.strftime("%Y-%m-%d")}: {deskripsi} | libur verified by python-holidays.',
            "red")
        return True
    else:
        for i in list_pref:
            if i in deskripsi.lower():
                cprint(
                    f'{tanggal.strftime("%Y-%m-%d")}: {deskripsi} | libur verified by libur_prefix.',
                    "blue")

                return True
    cprint(f'{tanggal.strftime("%Y-%m-%d")}: {deskripsi} | tidak libur!', "green")
    return False


def gen_cal(pref):
    res = {}
    format_tanggal = "%Y-%m-%d"
    year = datetime.now().year
    with open("calendar.json", "r") as f:
        js = json.loads(f.read())
    del js["created-at"]
    for k, v in js.items():
        tanggal = datetime.strptime(k, "%Y%m%d")
        if tanggal.year >= year:
            res[tanggal.strftime(format_tanggal)] = {}
            res[tanggal.strftime(format_tanggal)]["nama"] = "Deprecated! please use V2 https://github.com/guangrei/APIHariLibur_V2"
            res[tanggal.strftime(format_tanggal)]["libur"] = check_libur(
                tanggal, v["deskripsi"], pref)
    res["info"] = credit
    return res


if __name__ == "__main__":
    js = gen_cal(libur_prefix)
    with open("api.json", "w") as f:
        f.write(json.dumps(js, sort_keys=True))
    print("Done!")
