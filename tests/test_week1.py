import week1.extensions.extensions as extensions
import week1.interpreter.interpreter as interpreter
import week1.meal.meal as meal
from week1.bank import bank as bank
from week1.deep import deep as deep


def test_42():
    assert 'Yes' == deep.answer(' 42 ')


def test_42_words_hyphen():
    assert 'Yes' == deep.answer('forty-two')


def test_42_words_space():
    assert 'Yes' == deep.answer('forty two')


def test_42_words_case():
    assert 'Yes' == deep.answer('FORTY TWO')
    assert 'Yes' == deep.answer('FORTY-TWO')


def test_43_words_case():
    assert 'No' == deep.answer('43')


def test_bank_hello_leading_space():
    assert '$0' == bank.answer('   Hello')


def test_bank_hello_trailing_space():
    assert '$0' == bank.answer('Hello ')


def test_bank_hello_newman():
    assert '$0' == bank.answer('Hello, Newman')


def test_bank_hey():
    assert '$20' == bank.answer('   Hey')


def test_bank_bingo():
    assert '$100' == bank.answer('   What''s up')


# Extensions

def test_extensions_gif():
    assert 'image/gif' == extensions.mime_type('abc.gif')


def test_extensions_jpg():
    assert 'image/jpeg' == extensions.mime_type('abc.jpg')


def test_extensions_jpeg():
    assert 'image/jpeg' == extensions.mime_type('abc.jpeg')


def test_extensions_png():
    assert 'image/png' == extensions.mime_type('abc.png')


def test_extensions_pdf():
    assert 'application/pdf' == extensions.mime_type(' abc.PDF ')


def test_extensions_txt():
    assert 'text/plain' == extensions.mime_type('abc.txt')


def test_extensions_zip():
    assert 'application/zip' == extensions.mime_type('abc.zip')


def test_extensions_unknown():
    assert 'application/octet-stream' == extensions.mime_type('abc.docx')


def test_interpreter_addition():
    assert '2.0' == interpreter.interpret('1 + 1')


def test_interpreter_subtraction():
    assert '-1.0' == interpreter.interpret('2 - 3')


def test_interpreter_division():
    assert '3.3' == interpreter.interpret('10 / 3')


def test_interpreter_multiplication():
    assert '90.0' == interpreter.interpret('30 * 3')


def test_meal_convert_700():
    assert 7.0 == meal.convert('7:00')


def test_meal_convert_715():
    assert 7.25 == meal.convert('7:15')


def test_meal_convert_730():
    assert 7.5 == meal.convert('7:30')


def test_meal_convert_1930():
    assert 19.5 == meal.convert('19:30')


def test_meal_breakfast():
    assert 'breakfast time' == meal.mealtime('7:00')
    assert 'breakfast time' == meal.mealtime('7:30')
    assert 'breakfast time' == meal.mealtime('8:00')
    assert '' == meal.mealtime('6:59')
    assert '' == meal.mealtime('8:01')


def test_meal_lunch():
    assert 'lunch time' == meal.mealtime('12:00')
    assert 'lunch time' == meal.mealtime('13:00')
    assert 'lunch time' == meal.mealtime('13:00')
    assert '' == meal.mealtime('13:01')
    assert '' == meal.mealtime('11:59')


def test_meal_dinner():
    assert 'dinner time' == meal.mealtime('18:00')
    assert 'dinner time' == meal.mealtime('18:01')
    assert 'dinner time' == meal.mealtime('19:00')
    assert '' == meal.mealtime('17:59')
    assert '' == meal.mealtime('19:01')
