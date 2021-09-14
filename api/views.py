from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import UserSearchHistory, Smartphone
from api.serializers import SearchHistorySerializer, SmartphoneSerializer
from django.db.models import Count 
from rest_framework.views import APIView
from django.http import Http404
from datetime import datetime, timedelta
@api_view(['GET', 'POST'])
def search_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        search_keyword = UserSearchHistory.objects.all().values('search_keyword').annotate(total=Count('search_keyword')).order_by('total') 
        username = UserSearchHistory.objects.values('username').distinct()
        
        key_dict = {}
        u_name = []
        for i in search_keyword:
            key_dict[i['search_keyword']] = i['total']
            
        for i in username:
            u_name.append(i['username'])
        st = ","
        st = st.join(u_name)
        key_dict['username'] = u_name
        
        return Response(key_dict)
        
        ''' serializer = SearchHistorySerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) '''

    if request.method == 'POST':
        print(request.data)
        f_type = request.data.get('f_type')
        stri=""
        k = 0
        u = 0
        d = 0
        st = ""
        et = ""
        u_name = tuple()
        u_key = tuple()
        if 'search_key' in f_type.keys():
            u_key = tuple(f_type['search_key'])
            #keys = UserSearchHistory.objects.filter(search_keyword__in=u_name)
            #print(keys)
            k = 1
        if 'username' in f_type.keys():
            #print(type(f_type['username']))
            u_name = tuple(f_type['username'])
            #username = UserSearchHistory.objects.filter(username__in=u_name)
            #stri = str("username__in=('admin','test2'),")
            #print(username)
            u = 1
        if 'datefrom' in f_type.keys() and 'dateto' in f_type.keys():
            et = f_type['datefrom']
            st = f_type['dateto']
            #date = UserSearchHistory.objects.filter(searched_at__range=[f_type['datefrom'], f_type['dateto']])
            #stri = stri + str("searched_at__range=[f_type['datefrom'], f_type['dateto']]")
            #print(date)
            d = 1
        if 'yesterday' in f_type.keys():
            sd = datetime.today()
            et = str(sd.year)+'-'+str(sd.month)+'-'+str(sd.day)
            ed = sd + timedelta(days=-1)
            st = str(ed.year)+'-'+str(ed.month)+'-'+str(ed.day)
            #date = UserSearchHistory.objects.filter(searched_at__range=[st, et])
            #stri = stri + str("searched_at__range=[f_type['st'], f_type['et']]")
            d = 1
        if 'last_week' in f_type.keys():
            sd = datetime.today()
            et = str(sd.year)+'-'+str(sd.month)+'-'+str(sd.day)
            ed = sd + timedelta(days=-7)
            st = str(ed.year)+'-'+str(ed.month)+'-'+str(ed.day)
            #date = UserSearchHistory.objects.filter(searched_at__range=[st, et])
            #stri = stri + str("searched_at__range=[f_type['st'], f_type['et']]")
            d = 1
        if 'last_month' in f_type.keys():
            sd = datetime.today()
            et = str(sd.year)+'-'+str(sd.month)+'-'+str(sd.day)
            ed = sd + timedelta(days=-30)
            st = str(ed.year)+'-'+str(ed.month)+'-'+str(ed.day)
            #date = UserSearchHistory.objects.filter(searched_at__range=[st, et])
            #stri = stri + str("searched_at__range=[f_type['st'], f_type['et']]")
            d = 1
        #print('----->',stri)
        print('--->', u_name, st, et)
        if (k == 1 and u == 0 and d == 0):
            query = UserSearchHistory.objects.filter(search_keyword__in=u_key)
            #result = table.objects.filter(string__contains='pattern')
        elif (k == 0 and u == 1 and d == 0):
            query = UserSearchHistory.objects.filter(username__in=u_name)
        elif (k == 0 and u == 0 and d == 1):
            query = UserSearchHistory.objects.filter(searched_at__range=[st, et])
        elif (k == 0 and u == 1 and d == 1):
            query = UserSearchHistory.objects.filter(username__in=u_name,searched_at__range=[st, et])
        elif (k == 1 and u == 1 and d == 0):
            query = UserSearchHistory.objects.filter(search_keyword__in=u_key,username__in=u_name)
        elif (k == 1 and u == 0 and d == 1):
            query = UserSearchHistory.objects.filter(search_keyword__in=u_key,searched_at__range=[st, et])
        elif (k == 1 and u == 1 and d == 1):
            query = UserSearchHistory.objects.filter(search_keyword__in=u_key,username__in=u_name,searched_at__range=[st, et])
        

        if(k == 1 or u == 1 or d == 1):
            print('Query: ',query,k,u,d)
            keys=""
            keys1=""
            a=""
            for i in query:
                f_qr = Smartphone.objects.filter(name__contains=i.search_keyword)
                for i in f_qr:
                    if keys1 == "":
                        keys1 = i.name
                    else:
                        keys1 = keys1 + ',' +i.name
                """ if keys == "":
                    keys = i.search_keyword """
                """ else: keys = keys + ',' + keys1 """
                
            print('keys: ',keys1)
            keys = keys1.split(',')
            keys = tuple(keys)
            print('keys: ',keys1)
            f_query = Smartphone.objects.filter(name__in=keys)
            #f_query = Smartphone.objects.filter(name__contains=a)
            print(f_query)
        else: f_query = Smartphone.objects.all()
        serializer = SmartphoneSerializer(f_query, many=True)
        return Response(serializer.data)
        
 
@api_view(['GET', 'POST'])
def smartphone_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Smartphone.objects.all()
        serializer = SmartphoneSerializer(snippets, many=True)
        return Response(serializer.data)
    

    
@api_view(['GET', 'POST'])
def smartphone_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Smartphone.objects.all()
        serializer = SmartphoneSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SmartphoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)