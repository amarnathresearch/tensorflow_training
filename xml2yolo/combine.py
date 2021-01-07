import os
path = "/opt/amarnath/aicopia/idcard/idcardocr/testimages/"
fw = open("/opt/amarnath/aicopia/idcard/idcardocr/train.txt", "w")

for fil in os.listdir(path):
    overall = []
    if fil.split(".")[1] == "txt":
        my_string = fil.replace('.txt','.jpg')+''
    
        f = open(path+fil, "r")

        # print(f.readlines())
        for data in f.readlines():
            print(data.split())
            tmp = ','.join(data.split())
            print("tmp", tmp)
            my_string = my_string + " "+tmp
        print("my_string", my_string)
        fw.write(my_string+"\n")
        
            # data_list.extend()
        # print("data_list", data_list)
    
fw.close()    
