#!/usr/bin/env python
# coding: utf-8

# In[64]:


if __name__ == "__main__":
    
    number_shirt = input()
    size_shirt = input()
    number_request = input()
    size_request = input()

    size_shirt_list = size_shirt.split()
    size_request_list = size_request.split()

    size_shirt_list_format = []
    size_request_format = []

    for x in size_shirt_list:
        x_split = x.split('X')
        size_shirt_list_format.append([str(x_split.count(''))+x[-1]])
    for x in size_request_list:
        x_split = x.split('X')
        size_request_format.append([str(x_split.count(''))+x[-1]])

    # print(size_shirt_list_format)
    # print(size_request_format)

    if(number_shirt < number_request):
        print("No")
    else:
        count = 0
        for request in size_request_format:
            if(size_shirt_list_format.count(request) > 0):
                size_request_format.pop(count)
            count +=1
        # print(size_request_format)
        for request in size_request_format:
            for shirt in size_shirt_list_format:
                if(int(request[0][0]) <= int(shirt[0][0])):
                    if(request[0][1] == shirt[0][0]):
                        print("Yes")
                        break
                    else:
                        print("No")
                        break
                else:
                    print("No")
                    break

