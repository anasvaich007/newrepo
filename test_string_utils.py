import pytest
from string_utils import StringUtils

utils = StringUtils()

# ---------- capitalize ----------
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),       
    ("Skypro", "Skypro"),       # первая буква заглавная
    ("s", "S"),                 # одна буква
    ("", ""),                   # пустая строка
    ("123abc", "123abc"),       # строка с цифры
    (" hello", " hello")        # строка начинается с пробела
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected


# ---------- trim ----------
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),       # пробелы слева
    ("skypro   ", "skypro   "),    # пробелы справа остаются
    ("skypro", "skypro"),          # без пробелов
    ("", ""),                      # пустая строка
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


# ---------- contains ----------
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),      # символ в начале
    ("SkyPro", "P", True),      # символ в середине
    ("SkyPro", "o", True),      # символ в конце
    ("SkyPro", "U", False),     # символ отсутствует
    ("", "a", False),           # пустая строка
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# ---------- delete_symbol ----------
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # удаляем букву
    ("SkyPro", "Pro", "Sky"),      # удаляем подстроку
    ("SkyPro", "x", "SkyPro"),     # символ отсутствует-строка без изменений
    ("", "a", ""),                 # пустая строка
    ("aaa", "a", ""),              # удаляем все символы
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
