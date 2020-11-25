



def add_line_between_points(fig_object, point_1, point_2, colour):


    middle_point = int((point_1['x'] + point_2['x']) / 2)
    peak_point = int(((point_1['y'] + point_2['y']) / 2) + 4)


    path_string = "M " + str(point_1['x']) \
                  + "," \
                  + str(point_1['y']) \
                  + " Q " \
                  + str(middle_point) \
                  + "," \
                  + str(peak_point) \
                  + " " \
                  + str(point_2['x']) \
                  + "," \
                  + str(point_2['y'])

    #print(path_string)

    fig_object.add_shape(
        type="path",
        path=path_string,
        #fillcolor=colour,
        #opacity=0.1,
    )


