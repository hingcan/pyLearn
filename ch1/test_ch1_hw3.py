cameras_list = []


def test_ricoh_camera_includes():
    # открываем файл на чтение
    with open('/Users/romankashlev/PycharmProjects/sandBox/pyLearn/ch1/camera_list.txt', 'r') as file:
        header = file.readline().strip().split('|')
        # читаем остальные строки файла (с данными)
        for line in file:
            # разбиваем строку на отдельные значения
            values = line.strip().split(';')
            # создаем словарь, связывающий заголовок и значение
            record = {header[i]: values[i] for i in range(len(header))}
            # добавляем запись в список данных
            cameras_list.append(record)

    # выводим данные на экран для проверки
    print(cameras_list)

    # проверяем, что в списке есть запись о камере Ricoh GRIIIx
    assert {'Brend': 'Ricoh', 'Format': 'APS-C', 'Model': 'GRIIIx', 'Prise$': '1000'} in cameras_list
