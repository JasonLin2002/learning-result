import pkg_resources
import os
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s" % i.key for i in installed_packages])
for package in installed_packages_list:
    os.system("pip uninstall -y " + package)