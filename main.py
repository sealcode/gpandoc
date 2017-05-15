import sys

import settings
import main_dialog

from PyQt5.QtWidgets import QApplication

settings.crateFolderAboutName("temp")
settings.crateFolderAboutName("outputs")
settings.prepareGlobalVariables()
print("settings zipsFolder:", settings.zipsFolder)


def main():
    app = QApplication(sys.argv)
    window = main_dialog.MainWindow(app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
