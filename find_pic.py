import gtk
import pygtk
import os 
import glob
import datetime
pygtk.require('2.0')

class Gui:

    def __init__(self):

        # Create an Image object for a PNG file.
        file_name = "/home/developer/Pictures/Building_Native_Android_Libraries_with_0000 .png"
        pixbuf = gtk.gdk.pixbuf_new_from_file(file_name)
        pixmap, mask = pixbuf.render_pixmap_and_mask()
        image = gtk.Image()
        image.set_from_pixmap(pixmap, mask)

        # Create a window.
        window = gtk.Window()
        window.set_title("PNG file")
        window.connect("destroy", gtk.main_quit)

        # Show the PNG file in the window.
        window.add(image)
        window.show_all()

#find all images name in a list 
def find_all_images():
    file_location = "/home/developer/Pictures/"
    os.chdir(file_location)
    file_list = glob.glob("*.png")
    file_list_full = []
    for each in file_list:
        each = file_location + each
        file_list_full.append(each)

    return file_list_full


def debug_list(input_list):
    for each in input_list:
        print(each)
        get_time_stamp(each)


#get the time stamp of a file
def get_time_stamp(file_path):
    stat = os.stat(file_path)
    #print (stat)
    return stat.st_mtime

#create a map
def convert_timestamp(input_timestamp):
    digit = int(input_timestamp)
    readable = datetime.datetime.fromtimestamp(digit ).strftime('%Y-%m-%d %H:%M:%S')
    return readable

#sort the list of time stamp


#get 
if __name__ == "__main__":
    file_map = { }
    time_stamp_list =[]
    list_images = find_all_images()
    #debug_list(list_images)
    for each in list_images:
        time_stamp = get_time_stamp(each)
        time_stamp_list.append(time_stamp)
        file_map[time_stamp] = each

    sorted_time_stamp_list = sorted(time_stamp_list)
    length = len(sorted_time_stamp_list)
    last_100_timestamp_list = sorted_time_stamp_list[length -100 -1 : length -1]

    print ("======== 100 =========")
    for each in last_100_timestamp_list:
        filename_100 = file_map[each]
        modified_time = convert_timestamp(each)
        print (modified_time)
        print(filename_100)

    #Gui()
    #gtk.main()

