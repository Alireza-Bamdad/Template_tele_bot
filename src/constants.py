from types import SimpleNamespace
from src.utils.keybord import creat_buttens
import emoji


keys = SimpleNamespace(
    settings=emoji.emojize(':gear: Settings'),
    exit=emoji.emojize(':cross_mark: Exit'),
    )


keybords = SimpleNamespace(
    main = creat_buttens(keys.settings, keys.exit)
)