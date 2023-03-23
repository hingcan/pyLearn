# cameras list file variable
clf_vrbl = None

# list variable
cam_ch_res = None

# variable for backup test data
reserv_data = None

# variable for checking file's clothe status
file_close_status = None


def test_add_new_camera_to_file():
    # This block of code read file and store data to variables: for test and for backup
    cam_list_file = open('/Users/romankashlev/PycharmProjects/sandBox/pyLearn/ch1/camera_list.txt', mode='r')
    cam_list_file.seek(0)
    clf_vrbl = cam_list_file.read()
    cam_list_file.seek(0)
    reserv_data = cam_list_file.read()
    file_close_status = cam_list_file.closed

    assert 'Pentax;MX;35mm;Analog;250' not in clf_vrbl
    cam_list_file.close()
    file_close_status = cam_list_file.closed
    assert file_close_status == True


#    if 'Pentax;MX;35mm;Analog;250' not in clf_vrbl:
#        print('True')
#    elif 'Pentax;MX;35mm;Analog;250' in clf_vrbl:
#        print('False')
#    else:
#        print('Something wrong')

    # This block of code add new camera in the camera list with append function
    cam_list_file = open('/Users/romankashlev/PycharmProjects/sandBox/pyLearn/ch1/camera_list.txt', mode='a')
    cam_list_file.seek(0, 2)
    cam_list_file.write('\nPentax;MX;35mm;Analog;250')
    cam_list_file.close()
    file_close_status = cam_list_file.closed
    assert file_close_status == True


    # check there is new camera at the list
    cam_list_file = open('/Users/romankashlev/PycharmProjects/sandBox/pyLearn/ch1/camera_list.txt', mode='r')
    cam_list_file.seek(0)
    clf_vrbl = cam_list_file.readlines()
    if 'Pentax;MX;35mm;Analog;250' in clf_vrbl[-1]:
        cam_ch_res = True
    else:
        cam_ch_res = False

    assert cam_ch_res == True
    cam_list_file.close()
    file_close_status = cam_list_file.closed
    assert file_close_status == True


    cam_list_file = open('/Users/romankashlev/PycharmProjects/sandBox/pyLearn/ch1/camera_list.txt', mode='w')
#    cam_list_file.seek(0, 2)
    cam_list_file.write(reserv_data)
    cam_list_file.close()
    file_close_status = cam_list_file.closed
    assert file_close_status == True

