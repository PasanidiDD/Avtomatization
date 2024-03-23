import pytest

from string_utils import StringUtils

string_util = StringUtils()
#Тестовый пример 1: Проверяет, делает ли функция "capitalize" первую букву заглавной
@pytest.mark.parametrize('string, result', [
    #позитивные тест кейсы:
    ("dmitrii", "Dmitrii"),
    ("sveta", "Sveta"),
    ("mary Anne", "Mary anne"),
    ("ty'jan", "Ty'jan"),
    ("king1", "King1"),
    ("example-1", "Example-1"),
    #негативные тест кейсы:
    ("", ""),
    ("Steve", "Steve"),
    ("GPS", "Gps"), 
    ("123abc", "123abc"), 
    ("  leading space", "  leading space"),  
    ("trailing space  ", "Trailing space  "),  
    ("éxample", "Éxample")  # другой алфавит
])

def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

#Тестовый пример 2: Проверяет, удаляет ли функция "trim" пустое пространство перед строкой
@pytest.mark.parametrize('string, result', [
    #позитивные тест кейсы:
    ("  dog", "dog"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    (" Mary-Anne", "Mary-Anne"),
    ("   Dmitrii", "Dmitrii"),
    #негативные тест кейсы:
    ("", ""),
    ("ca t", "ca t"),
    ("monkey", "monkey"),
    ("123  ", "123  "),
    (1, 1),
    (0, 0)
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

#Тестовый пример 3: Проверяет, преобразует ли функция "to_list" строку в список
@pytest.mark.parametrize('string, divider, result', [
    #позитивные тест кейсы:
    ("dog,cat,bird", ",", ["dog", "cat", "bird"]),
    ("flower,tree,forest", ",", ["flower", "tree", "forest"]),
    ("pen;pencil;marker", ";", ["pen", "pencil", "marker"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    #негативные тест кейсы:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    
    print(f"Actual result: {res}")
    
    assert res == result

#Тестовый пример 4: Проверяет, правильно ли функция "contains" проверяет, содержит ли строка символ
@pytest.mark.parametrize('string, symbol, result', [
    #позитивные тест кейсы:
    ("footbol", "f", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("Mary-Anne", "-", True),
    ("123", "1", True),
    ("GPS", "P", True),
    ("", "", True),
    #негативные тест кейсы:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),  
    ("hello", "!", False), 
    ("hello", "", False),  
    ("", "x", False),  
    ("hello", "xyz", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

#Тестовый пример 5: Проверяет, удаляет ли функция "delete_symbol" указанный символ
@pytest.mark.parametrize('string, symbol, result', [
    #позитивные тест кейсы:
    ("test", "t", "es"),
    ("Street", "r", "Steet"),
    ("Mountain", "M", "ountain"),
    ("123", "1", "23"),
    ("Mary-Anne", "-", "MaryAnne"),
    ("Sky Pro", "", "SkyPro"),
    ("plate", "pla", "te"),
    #негативные тест кейсы:
    ("spoon", "k", "spoon"),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk"),
    ("park ", "", "park"),
    ("carpet  ", "r", "capet  ")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Тестовый пример 6: Проверяет, идентифицирует ли функция "starts_with" начальный символ
@pytest.mark.parametrize('string, symbol, result', [
    #позитивные тест кейсы:
    ("table", "t", True),
    ("", "", True),
    ("Headphones", "H", True),
    (" car", "", True),
    ("Film  ", "F", True),
    ("Anne-Mary", "A", True),
    ("Mary Anne", "M", True),
    ("123", "1", True),
    ("list", "", True),
    #негативные тест кейсы:
    ("Headphones", "h", False),
    ("tea", "T", False),
    ("", "v", False),
    ("Test", "t", False),
    ("eleven", "n", False),
    ("twenty", "w", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

#Тестовый пример 7: Проверяет, идентифицирует ли функция "end_with" конечный символ
@pytest.mark.parametrize('string, symbol, result', [
    #позитивные тест кейсы:
    ("winter", "r", True),
    ("GREAT", "T", True),
    ("", "", True),
    ("cat ", "", True),
    ("123", "3", True),
    ("Mary-Anne", "e", True),
    ("Anne Mary", "y", True),
    ("Peter1", "1", True),
    ("test", "", True),
    #негативные тест кейсы:
    ("morning", "P", False),
    ("evening", "e", False),
    ("door", "R", False),
    ("", "n", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

#Тестовый пример 8: Проверяет, идентифицирует ли функция "is_empty" пустую строку
@pytest.mark.parametrize('string, result', [
    #позитивные тест кейсы:
    ("", True),
    (" ", True),
    ("  ", True),
    #негативные тест кейсы:
    ("tree", False),
    (" flower", False),
    ("123", False),
    ("cat ", False)   
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

#Test Case 9: Tests if function "list_to_string" converts a list to a string
@pytest.mark.parametrize('lst, joiner, result', [
    #позитивные тест кейсы:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Mary", "Anne"], "-", "Mary-Anne"),
    #негативные тест кейсы:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result