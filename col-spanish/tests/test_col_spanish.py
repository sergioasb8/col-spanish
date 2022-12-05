from col_spanish import __version__
from col_spanish import del_punctuation, del_accent

def test_version():
    assert __version__ == '0.0.2'

def test_del_punctuation():
    text = "Hola, como estas? bien!"
    clean_text = del_punctuation(text)
    assert clean_text == "Hola como estas bien"

def test_del_accent():
    text = "el día sábado quiero más pan"
    clean_text = del_accent(text)
    assert clean_text == "el dia sabado quiero mas pan"