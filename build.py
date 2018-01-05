import os

os.system("cd hellolib & conan create . user/testing")
os.system("cd helloapp & conan create . user/testing")
# Alternative 1: deploy()
os.system("conan install App/0.1@user/testing")
os.system(os.sep.join([".", "bin", "app"]))
os.system("rm -rf bin deploy_manifest.txt")
# Alternative 2: with virtualrunenv (no deploy())
os.system("conan install App/0.1@user/testing -g virtualrunenv")
os.system("activate_run & app")
os.system("rm -rf bin deploy_manifest.txt *.bat *.ps1")