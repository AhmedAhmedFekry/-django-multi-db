
def paraMultiValues(filter:dict):
    for x,y in filter.items():
        if type(y)==str and  "," in  y:
        
            l=list()
            for i in  y.split(','):
                if  i=='':
                    pass
                elif i.isdecimal():
                    l.append(int(i))
                else:
                    l.append(i)
            filter.update({x: l})
    return filter