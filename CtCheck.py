# _*_ coding:utf-8 _*_
import sys  
import jieba
import  codecs
import jieba.analyse
import PymssqlService  
if __name__ == '__main__':
    word_lst = []  
    key_list=[]  
    resList = PymssqlService.main() #codecs.open ( 'ct.txt', 'r', 'utf_8' )

    for (REPORT_OBJECTIVE) in resList:
        #print("key_list:\n")
        s=REPORT_OBJECTIVE[0].encode('latin1').decode('gbk')
        #print (str(REPORT_OBJECTIVE).decode("utf8"))#(REPORT_OBJECTIVE)
        seg_list  = jieba.cut(s, cut_all=False)
        for i in seg_list :
            key_list.append(i)
        #print(key_list)
        # print("Default Mode: " + "\n ".join(key_list))  # 精确模式
    word_dict= {}  
    with codecs.open("wordCount.txt",'w') as wf2: #打开文件  
  
        for item in key_list:  
            if item not in word_dict: #统计数量  
                word_dict[item] = 1  
            else:  
                word_dict[item] += 1  
        #print(word_dict)
        orderList=list(word_dict.values())  
        orderList.sort(reverse=True)  
        # print orderList  
        for i in range(len(orderList)):  
            for key in word_dict:  
                if word_dict[key]==orderList[i]:  
                    wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档  
                    key_list.append(key)  
                    word_dict[key]=0  