import os
import csv


class CarBase:
    def __init__(self, car_type=None, brand=None, photo_file_name="", carrying=0):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        file_name = self.photo_file_name
        name, ext = os.path.splitext(file_name)
        if ext == '':
            ext = 'файл без расширения'
            return ext
        else:
            return ext[1:]


class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if body_whl == '':
            self.body_whl = '0x0x0'
            self.body_width = float(0)
            self.body_height = float(0)
            self.body_length = float(0)
        else:
            self.body_width = float(body_whl.split('x')[0])
            self.body_height = float(body_whl.split('x')[1])
            self.body_length = float(body_whl.split('x')[2])

    def get_body_volume(self):
        body_area = self.body_width*self.body_height*self.body_length
        return body_area


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying,  extra):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            if 'car' in row:
                car_list.append(Car(row[0], row[1], row[2], row[3], row[5]))
            elif 'truck' in row:
                car_list.append(Truck(row[0], row[1], row[3], row[4], row[5]))
            elif 'spec_machine' in row:
                car_list.append(SpecMachine(row[0], row[1], row[3], row[5], row[6]))
    return car_list


""""Вариант с добавлением объектов в словарь"""
# def get_car_list(csv_filename):
# with open(csv_filename) as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     next(reader)  # пропускаем заголовок
#     i = 1
#     names_dict = {}
#     for row in reader:
#         if 'car' in row:
#             car = "car_" + str(i)
#             names_dict[car] = Car(row[0], row[1], row[2], row[3], row[5])
#             i += 1
#         elif 'truck' in row:
#             car = "car_" + str(i)
#             names_dict[car] = Truck(row[0], row[1], row[3], row[4], row[5])
#             i += 1
#         elif 'spec_machine' in row:
#             car = "car_" + str(i)
#             names_dict[car] = SpecMachine(row[0], row[1], row[3], row[5], (row[6]))
#             i += 1




