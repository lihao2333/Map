from django.shortcuts import render
from MapModel.models import Loc
from django.conf import settings
import zipfile
import matplotlib.pyplot as plt
def map(request):
    ctx = {}
    ctx['locs'] = Loc.objects.all()
    x, y, para, attribute = get_get(request.GET)
    ctx['output'] = para + attribute
    gen_data(para + attribute, settings.BASE_DIR + "/static/data/")
    gen_image(para + attribute, settings.BASE_DIR + "/static/images/")
    return render(request, 'map.html', ctx)
def get_get(get_list):
    x = get_list.get("x", "")
    y = get_list.get("y", "")
    para = get_list.get("para", "")
    if x!="" and y!="":
        attribute = Loc.objects.filter(x=float(x), y=float(y))[0].attribute
    else:
        attribute = ""
    return [x, y, para, attribute ]
def gen_data(input, path):
    with open(path + 'data.txt', 'w') as mfile:
        mfile.write(input)
    azip = zipfile.ZipFile(path + 'data.zip', 'w',zipfile.ZIP_DEFLATED)
    azip.write(path + 'data.txt', 'data.txt')
    azip.close()
def gen_image(input, path):
    plt.plot([1,2,3,4])
    plt.xlabel(input)
    plt.savefig(path + 'image.png')
