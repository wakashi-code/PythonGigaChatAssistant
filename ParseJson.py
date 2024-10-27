import json


def parse_doctors(data_string):
    # Парсим входящую строку в JSON-формат
    data = json.loads(data_string)

    # Инициализируем список для хранения имен врачей
    doctors_list = []

    # Проходим по каждому элементу в полученных данных
    for clinic in data['data']['searchClinic']['elems']:
        # Получаем список врачей из каждой клиники
        doctor_list = clinic['clinicDoctorList']['elems']

        # Если список врачей не пуст, добавляем их в общий список
        for doctor_info in doctor_list:
            # Получаем имя врача и его специальность
            doctor_name = doctor_info['doctor']['entity']['person']['entity']['lastName']
            doctor_type = doctor_info['doctor']['entity']['doctorType']['name']

            # Добавляем информацию о враче в список
            doctors_list.append(f"{doctor_name} - {doctor_type}")
    print(*doctors_list)
    # Возвращаем список врачей
    return doctors_list

