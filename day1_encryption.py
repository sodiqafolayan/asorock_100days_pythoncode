from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()


generate_key()

load_key()


def ref_id_encryption(ref_id=input("Please enter your Reference ID: ")):

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(ref_id) != 12:
        print('length should be 12')
        val = False

    if not any(char.isdigit() for char in ref_id):
        print('Reference ID should have at least one numeral')
        val = False

    if not any(char.isupper() for char in ref_id):
        print('Reference ID should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in ref_id):
        print('Reference IDshould have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in ref_id):
        print('Reference ID should have at least one of the symbols $@#')
        val = False

    if val:
        key = load_key()
        encoded_message = ref_id.encode()
        f = Fernet(key)
        encrypted_ref_id = f.encrypt(encoded_message)

        return encrypted_ref_id


print(ref_id_encryption())
