import face_recognition # import face recognition library
import matplotlib.pyplot as plt # import matplotlib plot
import matplotlib.image as mpimg # import matplotlib image
import matplotlib.patches as patches # import matplotlib patch drawing
from PIL import Image # import python image processing library
import os

def face_paths():

    image_upload_dir = "/home/spark/Development/Flatiron/Projects/face-photo-organizer/backend-django/face_photo_organizer/uploads/images/"
    files = os.listdir(image_upload_dir)

    source_file_paths = []
    for i in range(len(files)):
        source_file_paths.append(image_upload_dir + files[i])

    print("these are file names")
    print(files)

    render_file_paths = []
    file_numbers = []
    for i in range(len(files)):
        render_file_paths.append("photos/files/" + str(files[i]))
        file_numbers.append(i+1)

    print("these are render file paths")
    print(render_file_paths)

    print("these are source file paths")
    print(source_file_paths)

    for i in range(len(source_file_paths)):
        PIL_image = Image.open(source_file_paths[i])
        print(PIL_image.size) # gives file size

        image = face_recognition.load_image_file(source_file_paths[i])
        face_locations = face_recognition.face_locations(image)
        # face_locations = face_recognition.face_locations(image, model="cnn")

        print(str(len(face_locations)) + " face(s) detected")
        print(face_locations)

        figure_original, ax_original = plt.subplots() # create figure
        face_regions = [0]*len(face_locations) # populate array for the rectangles to be drawn around the recognized faces

        for j in range(len(face_regions)): # add red rectangles according to the coordinates
            face_regions[j] = patches.Rectangle((face_locations[j][3],face_locations[j][0]),abs(face_locations[j][2]-face_locations[j][0]),abs(face_locations[j][3]-face_locations[j][1]), edgecolor='r', facecolor="none")

        matplotlib_image = mpimg.imread(source_file_paths[i])
        ax_original.set_axis_off() # this removes the axis from the photo

        for j in range(len(face_locations)): # adds red rectangle around found faces
            ax_original.add_patch(face_regions[j])

        ax_original.imshow(matplotlib_image) # show image with found faces


        # export the face-detected photos into files
        save_all_filename = "/home/spark/Development/Flatiron/Projects/face-photo-organizer/backend-django/face_photo_organizer/photos/static/photos/files/" + files[i][slice(-4)] + "_faces_all.jpg"

        figure_original.savefig(save_all_filename, dpi=200, bbox_inches="tight")  # entire photo with all faces with rectangles around found faces

        
        # PIL has (left, top, right, bottom) system. This constructs a rectangle from (left, top) coordinate to (right, bottom) coordinate
        # face-recognition has (top, right, bottom, left) system. This constructs a rectangle from (top, right) to (bottom, left) coordinate

        def coord_transform_face_rec_to_PIL(coord_face_recognition):
            # from (top, right, bottom, left) system to (left, top, right, bottom) system
            (top, right, bottom, left) = coord_face_recognition
            coord_PIL = (left, top, right, bottom)
            return coord_PIL

        # print(coord_transform_face_rec_to_PIL((188, 895, 239, 844)))

        file_path_save_faces = '/home/spark/Development/Flatiron/Projects/face-photo-organizer/backend-django/face_photo_organizer/photos/static/photos/files/'

        for j in range(len(face_locations)): # exports the faces-only cropped region into files
            img_cropped = PIL_image.crop(coord_transform_face_rec_to_PIL(face_locations[j]))
            # img_cropped.show()
            img_cropped.save(file_path_save_faces + files[i][slice(-4)] + "_face_" + str(j) + ".jpg")
    
    return [render_file_paths, file_numbers, source_file_paths]

# [render_file_paths, file_numbers, source_file_paths] = face_paths()
# print("this is render file path")
# print(render_file_paths)
# print("this is source file path")

# print(source_file_paths)