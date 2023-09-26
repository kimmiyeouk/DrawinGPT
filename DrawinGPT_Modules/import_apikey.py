def Import_APIkey():
    file = open("./DrawinGPT_Modules/API_key.txt",'r')
    api_key = file.readline().rstrip('\n')

    return api_key