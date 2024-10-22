from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy, QScrollBar

import app.assets.resources

# RESOURCE IMAGE
RESOURCE_HOME: str = u":/img/img/favicon.svg"
RESOURCE_NEWS: str = u":/img/button/black/news.svg"
RESOURCE_COLLECTION: str = u":/img/button/black/collection.svg"
RESOURCE_PLANNING: str = u":/img/button/black/planning.svg"
RESOURCE_SEARCH: str = u":/icons/icons/black/search.svg"
RESOURCE_PANIER: str = u":/icons/icons/black/shopping-cart.svg"
RESOURCE_ACCOUNT: str = u":/icons/icons/black/user.svg"

RESOURCE_PAUSE: str = u":/icons/icons/black/pause.svg"
RESOURCE_VALIDER: str = u":/icons/icons/black/check.svg"

RESOURCE_ADD: str = u":/icons/icons/black/check.svg"
RESOURCE_SUIVRE: str = u":/icons/icons/black/check.svg"
RESOURCE_MASQ: str = u":/icons/icons/black/check.svg"

RESOURCE_NEWS_HOVER: str = u":/img/button/red/news.svg"
RESOURCE_COLLECTION_HOVER: str = u":/img/button/red/collection.svg"
RESOURCE_PLANNING_HOVER: str = u":/img/button/red/planning.svg"
RESOURCE_SEARCH_HOVER: str = u":/icons/icons/red/search.svg"
RESOURCE_PANIER_HOVER: str = u":/icons/icons/red/shopping-cart.svg"
RESOURCE_ACCOUNT_HOVER: str = u":/icons/icons/red/user.svg"

# STYLE
STYLE_COLOR_PRIMARY: str = "rgb(207, 0, 10)"
STYLE_COLOR_BACKGROUND: str = "rgb(255, 255, 255)"
STYLE_COLOR_BORDER: str = "rgb(224, 224, 224)"
STYLE_COLOR_CARD: str = "rgb(255, 255, 255)"
STYLE_COLOR_TEXT: str = "rgb(28, 28, 28)"
STYLE_COLOR_TEXT_DETAIL: str = "rgb(119, 119, 119)"
STYLE_COLOR_ICON: str = "rgb(187, 187, 187)"
STYLE_COLOR_READ: str = "rgb(61, 90, 254)"
STYLE_COLOR_CART: str = "rgb(245, 176, 39)"
STYLE_COLOR_STATE_HOVER: str = "rgba(0, 0, 0, 0.07)"
STYLE_COLOR_STATE_PRESS: str = "rgba(0, 0, 0, 0.12)"
STYLE_SCROLL_BAR = f"""
            QScrollBar:vertical {{
                background: rgba(0, 0, 0,0);
                border: 1px solid  {STYLE_COLOR_BORDER};
                border-radius: 7px;
                width: 15px;
            }}
            
            QScrollBar:handle:vertical {{
                background: {STYLE_COLOR_TEXT_DETAIL};
                border: 1px solid  #000;
                width: 10px;
                border-radius: 6px;
                max-height: 18px;
            }}
            
            QScrollBar:sub-line:vertical {{
                background: rgba(0, 0, 0,0);
                border-radius: 6px;
                height: 8px;
            }}
            
            QScrollBar:add-line:vertical {{
                background: rgba(0, 0, 0,0);
                border-radius: 7px;
            }}
            
            QScrollBar:add-page:vertical,
            QScrollBar:sub-page:vertica {{
            }}
        """

# COLOR
COLOR_PRIMARY = QColor(207, 0, 10)
COLOR_BACKGROUND = QColor(255, 255, 255)
COLOR_BORDER = QColor(224, 224, 224)
COLOR_CARD = QColor(255, 255, 255)
COLOR_TEXT = QColor(28, 28, 28)
COLOR_TEXT_DETAIL = QColor(119, 119, 119)
COLOR_ICON = QColor(61, 90, 254)
COLOR_READ = QColor(61, 90, 254)
COLOR_CART = QColor(245, 176, 39)

# FONT
family_helvetica: str = "Helvetica"
FONT_11: QFont = QFont(family_helvetica, 11, 50)
FONT_12: QFont = QFont(family_helvetica, 12, 50)
FONT_14: QFont = QFont(family_helvetica, 14, 50)
FONT_16: QFont = QFont(family_helvetica, 16, 50)
FONT_17: QFont = QFont(family_helvetica, 17, 50)
FONT_18: QFont = QFont(family_helvetica, 18, 50)
FONT_42: QFont = QFont(family_helvetica, 42, 50)
FONT_42.setBold(True)
FONT_26: QFont = QFont(family_helvetica, 26, 50)

# SIZE
SIZE_BUTTON_MENU: QSize = QSize(46, 46)
SIZE_ICON_BUTTON_MENU: QSize = QSize(26, 26)
SIZE_IMAGE_NEWS_ITEM: QSize = QSize(220, 330)
SIZE_PAGE_MIN: QSize = QSize(732, 480)

# ICON
ICON_HOME = QIcon(RESOURCE_HOME)
ICON_NEWS = QIcon(RESOURCE_NEWS)
ICON_NEWS_HOVER = QIcon(RESOURCE_NEWS_HOVER)
ICON_COLLECTION = QIcon(RESOURCE_COLLECTION)
ICON_PLANNING = QIcon(RESOURCE_PLANNING)
ICON_SEARCH = QIcon(RESOURCE_SEARCH)
ICON_PANIER = QIcon(RESOURCE_PANIER)
ICON_ACCOUNT = QIcon(RESOURCE_ACCOUNT)

ICON_MENUE_PAUSE = QIcon(RESOURCE_PAUSE)
ICON_MENUE_VALIDATE = QIcon(RESOURCE_VALIDER)
ICON_MENUE_ADD = QIcon(RESOURCE_ADD)
ICON_MENUE_SUIVRE = QIcon(RESOURCE_SUIVRE)
ICON_MENUE_ADD_PANIER = QIcon(RESOURCE_PANIER)
ICON_MENUE_MASQ = QIcon(RESOURCE_MASQ)

# SPACER
SPACER_EXPAND_V = QSpacerItem(1000, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)
SPACER_EXPAND_H = QSpacerItem(1000, 1000, QSizePolicy.Expanding, QSizePolicy.Minimum)
SPACER_4_V = QSpacerItem(4, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)
SPACER_13_V = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)
SPACER_15_V = QSpacerItem(15, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
SPACER_18_V = QSpacerItem(18, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)
SPACER_20_V = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

SPACER_13_H = QSpacerItem(13, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)
SPACER_18_H = QSpacerItem(18, 18, QSizePolicy.Fixed, QSizePolicy.Minimum)
