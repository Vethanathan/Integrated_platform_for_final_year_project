import Ironman
import zipping
def is_plag(dict):
    boolean = [False for i in dict]
    ctr=0
    file_ctr=0
    avg_index=0
    d={}
    for key,value in dict.items():
        url_list,count,index=Ironman.plag_cheker(value)
        if url_list!=[]:
            boolean[ctr]=True
            d[key]=url_list
            file_ctr+=1
            avg_index+=round(float(index))
        ctr+=1
    if file_ctr==0:
        print(True in boolean,file_ctr,0,d)
        return True in boolean,file_ctr,0,d
    else:
        print(True in boolean,file_ctr,avg_index//file_ctr,d)
        return True in boolean,file_ctr,avg_index//file_ctr,d