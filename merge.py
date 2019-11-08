import json as json
def merge(a, b,c):
 for key in b:
        if key in a:# if key is in both a and b
            if isinstance(a[key], dict) and isinstance(b[key], dict): # if the key is dict Object
                merge(a[key], b[key])
            else:
              a[key] =a[key]+ b[key]
        else: # if the key is not in dict a , add it to dict a
            a.update({key:b[key]})
 for key in c:
        if key in a:# if key is in both a and b
            if isinstance(a[key], dict) and isinstance(c[key], dict): # if the key is dict Object
                merge(a[key], c[key])
            else:
              a[key] =a[key]+ c[key]
        else: # if the key is not in dict a , add it to dict a
            a.update({key:c[key]})
 return a

with open('C:/Users/mahes/desktop/a.json') as fp1:
    with open('C:/Users/mahes/desktop/b.json') as fp2:
      with open('C:/Users/mahes/desktop/b.json') as fp3:
        jsondata1=json.load(fp1)
        jsondata2=json.load(fp2)
        jsondata3=json.load(fp3)
        with open('./data.json', 'w') as f:
          json.dump(merge(jsondata1,jsondata2,jsondata3),f,sort_keys=True)