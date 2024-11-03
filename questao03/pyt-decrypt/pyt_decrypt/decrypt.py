import sys
from Crypto.Cipher import AES

KEY_SIZES = [16, 24, 32]


def decrypt_msg(key: str, mode: str, msg: str):
    """
    Descriptografa uma mensagem no padrao AES.

    Args:
        key: Chave da criptografia
        mode: Modo de suporte a criptografia
        msg: Mensagem criptografada

    Returns:
        A mensagem descriptograda

    Raises:
        ValueError: A chave AES deve ter 16, 24 ou 32 bytes.
        ValueError: Modo não suportado.
        ValueError: A mensagem Criptografada deve estar no formato hexadecimal.
    """

    if len(key) not in KEY_SIZES:
        raise ValueError('A chave AES deve ter 16, 24 ou 32 bytes.')

    key_bytes = key.encode('utf-8')

    try:
        msg_bytes = bytes.fromhex(msg)
    except ValueError:
        raise ValueError(
            f'A mensagem Criptografada deve estar no formato hexadecimal.'
        )

    match mode:
        case 'ECB':
            mode = AES.MODE_ECB
        case _:
            raise ValueError('Modo não suportado.')

    cipher = AES.new(key_bytes, mode)

    msg_decrypt = cipher.decrypt(msg_bytes)

    return msg_decrypt.decode('utf-8')


def print_success(msg):
    print('[\033[32m\033[1mSUCCESS\033[0;0m\033[0;0m] {}'.format(msg))


def abort(reason='Falha não esperada.'):
    print('[\033[31m\033[1mABORT\033[0;0m\033[0;0m] {}'.format(reason))
    sys.exit(1)


def main():
    if len(sys.argv) < 4:
        abort('Requeridos: KEY, MODE, MSG_CRYPT')

    key = sys.argv[1]
    mode = sys.argv[2]
    msg = sys.argv[3]

    try:
        print_success(decrypt_msg(key, mode, msg))
    except Exception as e:
        abort(f'{e}')


if __name__ == '__main__':
    main()
