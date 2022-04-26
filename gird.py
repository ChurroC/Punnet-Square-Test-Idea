def grid(row, col, length_of_each_couloumn, message_array):
    message=""
    for i in range((row*col)+1):
        if i>len(message_array):
            if length_of_each_couloumn%2==1:
                message_array.append(" ")
            if length_of_each_couloumn%2==0:
                message_array.append("")

    col_drawing="+"
    for i in range(len(message_array)):
        message_array[i]=str(message_array[i])
    for i in range(length_of_each_couloumn):
        col_drawing+="-"

    for i in range(len(message_array)):
        adjust=int((length_of_each_couloumn-len(message_array[i]))/2)
        message_array[i]=message_array[i].ljust(adjust+len(message_array[i]))
        message_array[i]=message_array[i].rjust(adjust+len(message_array[i]))

    for i in range(row):
        message+='\n' + col_drawing*col + '+\n'
        for j in range(col):
            message+='|'+message_array[j+i*col]
        message+='|'
    message+='\n' + col_drawing*col + '+\n'
    return message


print(grid(2,2,4,(['AB', 'AB'])))

