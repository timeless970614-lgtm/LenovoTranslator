from qtsymbols import *
import functools
from myutils.config import globalconfig
from gui.usefulwidget import makescrollgrid, SuperCombo
from language import UILanguages, Languages


def get_about_info():
    return "LenovoTranslator"


def changeUIlanguage(_):
    languageChangeEvent = QEvent(QEvent.Type.LanguageChange)
    QApplication.sendEvent(QApplication.instance(), languageChangeEvent)


class __delayloadlangs(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.como = SuperCombo(static=True)
        # Set placeholder; real items loaded in delayload
        self.como.addItem(
            Languages.fromcode(globalconfig["languageuse2"]).nativename
            if Languages.fromcode(globalconfig["languageuse2"])
            else UILanguages[0].nativename
        )
        QTimer.singleShot(0, self.delayload)
        self.addWidget(self.como)

    def delayload(self):
        self.como.clear()
        inner = [_.code for _ in UILanguages]
        vis = [_.nativename for _ in UILanguages]
        self.como.addItems(vis, inner)
        self.como.setCurrentData(globalconfig["languageuse2"])
        self.como.currentIndexChanged.connect(
            lambda _: (
                globalconfig.__setitem__("languageuse2", self.como.getCurrentData()),
                changeUIlanguage(0),
            )
        )


def setTab_about(self: QWidget, basel):
    makescrollgrid(
        [
            [
                {
                    "name": "aboutlayout",
                    "parent": self,
                    "grid": [
                        ["UI语言", __delayloadlangs],
                    ],
                },
            ],
        ],
        basel,
    )
