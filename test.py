

import os, csv
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support




def find(f):
    print(f"processing file: {f}")
    iids = ["575481bdf9c249cb95e4c29f895b2b44", "534cf1abbad34ba3bbddc5c54bf63754",
            "29e9952de4e6455f878dc5179f4a41cf", "f4949869163b4f9c838a19f457882628"]
    # iids = ["AAEwgk6895QAABCS4PvOOw", "AAJPVE69XSgAABDkTHVi0Q", "AALPsE6_ovYAABA7PchUGg"]
    file = list(csv.reader(open(f, "r").readlines(), delimiter="\t"))
    line_count = 0
    found = False
    res = []
    for line in file:
        line_count += 1
        for iid in iids:
            if iid in line:
                found = True
                print(f"{iid} found in file {f}")
                res.append((iid, line))
    if found:
        return found, f, res

    return False, f, res


def run(workers=4):
    freeze_support()
    executor = ProcessPoolExecutor(max_workers=workers)
    files = os.listdir(os.path.relpath("LiveRamp"))
    files = list(map(lambda x: "LiveRamp/" + x, files))

    # single
    # l = []
    # for f in files:
    #     l.append(find(f))

    # multi
    futures = executor.map(find, files)
    return list(futures)

if __name__ == '__main__':

    k = run(workers=20)
    print(k)
    for e in k:
        if e[0]:
            # found, filename, line, iid = e
            print(e)

{'LRTest_R-840606_Cognitiv_Cookie_20210203_172708': ['575481bdf9c249cb95e4c29f895b2b44', 'Xi1365M0Ey7W8Mw74bD0WDbGLEGrMIKPEIRuVFx7og8S1h0VkOscrzaOAuJ4pLCdbK7Sdc', 'UNMATCHED']}
{'LRTest_R-840606_Cognitiv_Cookie_20210216_133042', ['29e9952de4e6455f878dc5179f4a41cf', 'XY1365lbLZMITDPNaeZR2FXrMNbIt3tz4mDe1q7zZ6fCtnaNQ', 'hY1365B0rx119I07b0l983fzw2zoKiJ9P13tEvmjklTKHpl-g']}
{'LRTest_R-840606_Cognitiv_Cookie_20210224_232646', ['575481bdf9c249cb95e4c29f895b2b44', 'XY1365Za6l-M_5K1Rr-K4FSSmLIjsncYkzBnVIR4HhGgKoF1k', 'hY1365NQo2g_-QgRWo1fPNdQ3jYPxzk4WGqkYWfNGpYJEXo8s']}