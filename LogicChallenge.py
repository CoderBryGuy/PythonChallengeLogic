_author_ = "dev"

ipAddress = input("Enter ip address: ")
if ipAddress[-1] != ".":
    ipAddress += '.'

segment = 1
segment_length = 0
# char = ""



for char in ipAddress:
    # print("char is: {0}".format(char))
    if char == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length +=1

#unless final character in string was '.' then we have not printed the last segment
# if char != '.':
#     print("segment {} contains {} characters".format(segment, segment_length))
#
