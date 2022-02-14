# question37 of doc.
# count the sheeps that are present(means true).
def sheeps():
    list=["True","True","True","False",
          "True","True","True","True",
          "True","False","True","False",
          "True","False","False","True",
          "True","True","True","True",
          "False","False","True","True"]
    count=0
    i=0
    while i<len(list):
        if list[i]=="True":
            count+=1
        i+=1
    print(count)
sheeps()