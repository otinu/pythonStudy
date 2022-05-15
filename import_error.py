#インポート先のディレクトリが変わることなどを想定して例外処理(ImportError)をすることも可能

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice("word")