import sys
from pytest import mark, raises

from pyt_decrypt.decrypt import decrypt_msg, main


@mark.parametrize(
    'key,option,msg,msg_decrypt',
    [
        (
            'thisisasecretkey',
            'ECB',
            'a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20',
            'Sistemas Embarcados\r\r\r\r\r\r\r\r\r\r\r\r\r',
        ),
    ],
)
def test_msg_correct(key, option, msg, msg_decrypt):
    ret = decrypt_msg(key, option, msg)

    assert ret == msg_decrypt


@mark.parametrize(
    'key,option,msg,msg_error',
    [
        (
            '12345',
            'ECB',
            'a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20',
            'A chave AES deve ter 16, 24 ou 32 bytes.',
        ),
    ],
)
def test_key_size_error(key, option, msg, msg_error):

    with raises(ValueError, match=msg_error):
        decrypt_msg(key, option, msg)


@mark.parametrize(
    'key,option,msg,msg_error',
    [
        (
            'thisisasecretkey',
            'CBC',
            'a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20',
            'Modo não suportado.',
        ),
    ],
)
def test_mode_error(key, option, msg, msg_error):

    with raises(ValueError, match=msg_error):
        decrypt_msg(key, option, msg)


@mark.parametrize(
    'key,option,msg,msg_error',
    [
        (
            'thisisasecretkey',
            'EBC',
            'oiee tudo bem',
            'A mensagem Criptografada deve estar no formato hexadecimal.',
        ),
    ],
)
def test_msg_is_not_hex(key, option, msg, msg_error):

    with raises(ValueError, match=msg_error):
        decrypt_msg(key, option, msg)


@mark.parametrize(
    'key,option,msg,msg_decrypt',
    [
        (
            'thisisasecretkey',
            'ECB',
            'a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20',
            '[\033[32m\033[1mSUCCESS\033[0;0m\033[0;0m] Sistemas Embarcados',
        ),
    ],
)
def test_main_success(capsys, key, option, msg, msg_decrypt):
    setattr(
        sys,
        'argv',
        ['script.py', key, option, msg],
    )

    main()

    captured = capsys.readouterr()

    assert msg_decrypt in captured.out


@mark.parametrize(
    'key,option,msg_error',
    [
        (
            'thisisasecretkey',
            'ECB',
            '[\033[31m\033[1mABORT\033[0;0m\033[0;0m] Requeridos: KEY, MODE, MSG_CRYPT',
        ),
    ],
)
def test_main_missing_args(capsys, key, option, msg_error):
    setattr(
        sys,
        'argv',
        ['script.py', key, option],
    )

    with raises(SystemExit) as e:
        main()

    captured = capsys.readouterr()

    assert msg_error in captured.out
    assert e.value.code == 1


@mark.parametrize(
    'key,option,msg,msg_error',
    [
        (
            'thisisasecretkey',
            'CBC',
            'a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20',
            '[\033[31m\033[1mABORT\033[0;0m\033[0;0m] Modo não suportado.',
        ),
    ],
)
def test_main_error(capsys, key, option, msg, msg_error):

    setattr(
        sys,
        'argv',
        ['script.py', key, option, msg],
    )

    with raises(SystemExit) as e:
        main()

    captured = capsys.readouterr()

    assert msg_error in captured.out
    assert e.value.code == 1
