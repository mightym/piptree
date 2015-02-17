# coding:utf-8
import pkg_resources

installed_packages = dict(
            [(p.project_name.lower(), p) for p in pkg_resources.working_set])

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def process(value, depth):
    if depth == 0:
        print '└── ' + value
    else:
        print (depth + 3) * ' ' + '└── ' + value

def getRequirements(package):
    dist = installed_packages[package]
    return list(dep.project_name for dep in dist.requires())

def process_tree(reqlist, callback, depth):
    for k in reqlist:
        if getRequirements(k.lower()):
            callback(k, depth)
            process_tree(getRequirements(k.lower()), callback, depth + 1)
        else:
            callback(k, depth)


def showPackageTree(lines):
    totalDependecies = []
    allrequirements = []

    for line in lines:
        normalized_name = line.split('==', 1)[0].strip().lower()
        if normalized_name in installed_packages:

            totalDependecies += getRequirements(normalized_name)
            allrequirements += [normalized_name]

    sortedrequirements = sorted(allrequirements)

    for r in sortedrequirements:
        if getRequirements(r.lower()):
            print bcolors.OKBLUE + installed_packages[r].project_name + ' ' + installed_packages[r].version + bcolors.ENDC
            process_tree(getRequirements(r.lower()), process, 0)
        else:
            print bcolors.OKBLUE + installed_packages[r].project_name + ' ' + installed_packages[r].version + bcolors.ENDC

def show(requirementsfile):
    with open(requirementsfile) as f:
        showPackageTree(f.readlines())
