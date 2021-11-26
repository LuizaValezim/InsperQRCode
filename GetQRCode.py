import os
     
cwd = os.getcwd()
open_chrome = "am start --user 0 -n com.android.chrome/com.google.android.apps.chrome.Main"
     
print("Current working directory:", cwd)
os.system(open_chrome)