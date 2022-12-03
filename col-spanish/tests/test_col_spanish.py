from col_spanish import __version__
from col_spanish import del_punctuation, del_accents

def test_version():
    assert __version__ == '0.0.1'

def test_del_punctuation():
    text = "Hola, como estas? bien!"
    clean_text = del_punctuation(text)
    assert clean_text == "Hola como estas bien"

def test_del_accents():
    text = "el día sábado quiero más pan"
    clean_text = del_accents(text)
    assert clean_text == "el dia sabado quiero mas pan"