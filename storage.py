import os
import json
import tempfile
import argparse


def create_parser():
    """Функция парсит аргументы"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val', nargs='?')
    return parser


parser = create_parser()
namespace = parser.parse_args()

# Создание временного файла
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def load_data():
    """Функция проверяет наличие хранилища и возврашает либо пустой словарь, либо словарь из хранилища"""
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            data_json = json.loads(f.read())
            return data_json
    else:
        return {}


def fill_new_data():
    """Функция записывает в словарь значение к ключу,
    если он уже существует или добавляет в словарь нокую пару ключ/значение"""
    if namespace.key in dict_from_file.keys():
        list_of_values = dict_from_file[namespace.key]
        list_of_values.append(namespace.val)
        return dict_from_file
    else:
        dict_from_file[namespace.key] = [namespace.val]
        return dict_from_file


def write_new_data():
    """Функция записывает новый словарь в хранилище"""
    with open(storage_path, 'w') as f:
        f.write(json.dumps(updated_dict, ensure_ascii=False))


if namespace.val is None:
    dict_from_file = load_data()
    if namespace.key in dict_from_file.keys():
        values = dict_from_file[namespace.key]
        print(values)
    else:
        print("Ключ \"{}\" отсутствует в хранилище".format(namespace.key))
else:
    dict_from_file = load_data()
    updated_dict = fill_new_data()
    write_new_data()

