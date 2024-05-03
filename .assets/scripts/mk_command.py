import os
os.chdir("./../usr/bin")
f=open("ci-terminal.sh", "w")
f.write("cd\npython CoolIntro/.assets/scripts/terminal.py")
f.close()
os.system("mv ci-terminal.sh ci-terminal")
os.system("chmod +x ci-terminal")
print("Python script finished.")
