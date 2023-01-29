import Ironman
import zipping
def is_plag(path_list):
    boolean = [False for i in path_list]
    # url = [False for i in path_list]
    ctr=0
    for path in path_list:
        d={}
        String = zipping.stringyfy(path)
        # print(path)
        # print(String)
        # exit()
        url_list=Ironman.plag_cheker(String)[0]
        if url_list!=[]:
            boolean[ctr]=True
            d[path]=url_list
            # url[ctr]=[url_list]
        ctr+=1
    # print(boolean)
    print(d)
    return True in boolean,d
# y=zipping.list_files("static\\files\\extracted\\test_dir")
# # print(y)
# print(is_plag(y))