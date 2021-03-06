# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

import myfunc

def hello(request):

    return render_to_response('hello.html', {
                                             #'curl': myfunc.curl(),
                                             'store': myfunc.store(),
                                             
                                             })

                
@csrf_exempt
def save(request):
    content = request.FILES['file1']
    
    from os import environ
    online = environ.get("APP_NAME", "") 

    if online:
        import sae.const
        access_key = sae.const.ACCESS_KEY
        secret_key = sae.const.SECRET_KEY
        appname = sae.const.APP_NAME
        domain_name = "code"     
        
        import sae.storage
        s = sae.storage.Client()
        ob = sae.storage.Object(content.read())
        url = s.put(domain_name, content.name.encode('utf-8'),ob)
        return render_to_response('index.html', {"value":url})
    else:
        return render_to_response('index.html', {"value":"save failed"})

@csrf_exempt
def text(request):
    import sae.kvdb
    s=sae.kvdb.KVClient()
    k=request.POST['mem'].encode('utf-8')
    v=request.POST['txt'].encode('utf-8')
    s.add('larus-'+k,v)
    t=s.get_by_prefix('larus-')
    r=[]
    for i in t:
        r.append((i[0].split('larus-')[1],i[1]))
    return render_to_response('text.html',{'value':r})    

@csrf_exempt
def rem(request):
    import sae.kvdb
    s=sae.kvdb.KVClient()
    #引号内添加删除字段
    #larus为前缀
    tmp=u''
    tmp=tmp.encode('utf-8')
    k=s.getkeys_by_prefix(tmp)   
    for i in k:
        s.delete(i)
    return render_to_response('index.html',{'value':'ok'})
