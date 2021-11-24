import matplotlib.font_manager

j = matplotlib.font_manager.win32InstalledFonts()
for k in j:
    print(k)