import os


def xor_encrypt_decrypt(text, key):
    """
    XOR шифрование/дешифрование.
    """
    key_length = len(key)
    key_as_int = [ord(k) for k in key]
    text_as_int = [ord(t) for t in text]
    result = ''.join(chr(t ^ key_as_int[i % key_length]) for i, t in enumerate(text_as_int))
    return result


def vigenere_cipher(text, key, mode):
    """
    Шифр Виженера для русских букв.
    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []
    key = key.lower()
    key_indices = [alphabet.index(k) for k in key]

    for i, char in enumerate(text.lower()):
        if char in alphabet:
            char_idx = alphabet.index(char)
            key_idx = key_indices[i % len(key)]
            if mode == "encrypt":
                new_char = alphabet[(char_idx + key_idx) % len(alphabet)]
            elif mode == "decrypt":
                new_char = alphabet[(char_idx - key_idx) % len(alphabet)]
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    print("Выберите алгоритм шифрования:")
    print("1. XOR шифрование")
    print("2. Шифр Виженера (для русских букв)")
    choice = input("Введите номер алгоритма: ").strip()

    if choice not in {'1', '2'}:
        print("Неверный выбор. Завершение программы.")
        return

    mode = input("Выберите режим (encrypt для шифрования, decrypt для дешифрования): ").strip().lower()
    if mode not in {'encrypt', 'decrypt'}:
        print("Неверный режим. Завершение программы.")
        return

    source = input("Введите 'file' для работы с файлом или 'text' для ввода текста вручную: ").strip().lower()
    if source == 'file':
        filename = input("Введите имя файла: ").strip()
        if not os.path.exists(filename):
            print("Файл не найден.")
            return
        text = read_from_file(filename)
    elif source == 'text':
        text = input("Введите текст: ").strip()
    else:
        print("Неверный ввод.")
        return

    if choice == '1':
        key = input("Введите ключ для XOR шифрования: ").strip()
        if not key:
            print("Ключ не может быть пустым.")
            return
        result = xor_encrypt_decrypt(text, key)
    elif choice == '2':
        key = input("Введите ключ для шифра Виженера (на русском): ").strip()
        if not key.isalpha() or not all(c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for c in key.lower()):
            print("Ключ должен содержать только русские буквы.")
            return
        result = vigenere_cipher(text, key, mode)

    if source == 'file':
        output_file = input("Введите имя файла для записи результата: ").strip()
        write_to_file(output_file, result)
        print(f"Результат записан в файл {output_file}.")
    else:
        print("Результат:")
        print(result)


if __name__ == "__main__":
    main()
