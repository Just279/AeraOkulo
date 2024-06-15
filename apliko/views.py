from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators import gzip
from django.contrib.auth import logout

from django.core.validators import FileExtensionValidator
from django.http import StreamingHttpResponse

from .forms import ModelVidbendo, ModelFoto, ModelArkivo
from .models import Fotilo, Mesagoj, Vidbendo, Foto, Arkivo

import random
import threading

from .photo import start_photo
from .archive import start_archive
from .archive import create_archive
from .video import start_video
from .converter import convert_avi_to_mp4
from .video_processing import gen_frames



vidbendo_que=[]
vidbendo_prc=False
photo_que=[]
photo_prc=False
archive_que=[]
archive_prc=False

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def logout_view(request):
    logout(request)
    return redirect('/login/')

def index(request):
    if request.user.is_authenticated:
        if is_ajax(request=request):
            v=request.GET['text']
            if v=='?':
                mess=Mesagoj.objects.filter(is_new3=None)
                txt=''
                for mes in mess:
                    txt+='<li class="text">'+mes.name+'</li>'
                data = {'result': txt,'ln':len(mess)}
                return JsonResponse(data)
            else:
                mess=Mesagoj.objects.filter(is_new3=None)
                txt=''
                for mes in mess:
                    mes.is_new3='False'
                    mes.save()
                return JsonResponse({})
        else:
            template='apliko/index.html'
            fots=Fotilo.objects.order_by('name')
            mess=Mesagoj.objects.order_by('-time')
            data={'fots':fots,'mess':mess}
            return render(request,template,data)
    else:
        return redirect('login')

def fotoanalizo(request):
    if request.user.is_authenticated:
        global photo_que
        data={}
        if request.method == 'POST':
            form = ModelFoto(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                f=Foto.objects.first()
                photo_que.append(f.pk)
                threading.Thread(target=th_photo).start()
                name_file=str(f.upload)
                name_file=name_file[name_file.rfind('/')+1:]
                f.name=name_file
                st23=datetime.now().strftime("%m")
                if st23=='01': st23='января'
                elif st23=='02': st23='февраля'
                elif st23=='03': st23='марта'
                elif st23=='04': st23='апреля'
                elif st23=='05': st23='мая'
                elif st23=='06': st23='июня'
                elif st23=='07': st23='июля'
                elif st23=='08': st23='августа'
                elif st23=='09': st23='сентября'
                elif st23=='10': st23='октября'
                elif st23=='11': st23='ноября'
                elif st23=='12': st23='декабря'
                date_file=datetime.now().strftime("%d "+st23+" %Y г. %H:%M")
                return JsonResponse({'status': 'success','leporo':name_file,'new_data':[name_file,date_file]})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
        else:
            form = ModelFoto()
            data['form']=form
            data['leporo']=''
            data['fots']=Foto.objects.order_by('-time')
            data['arvs']=Arkivo.objects.order_by('-time')
            data['mess']=Mesagoj.objects.order_by('-time')
            return render(request, 'apliko/fotoanalizo.html', data)
    else:
        return redirect('login')

def fotoanalizo_leporo(request):
    if request.user.is_authenticated:
        global archive_que
        data={}
        if request.method == 'POST':
            form = ModelArkivo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                a=Arkivo.objects.first()
                archive_que.append(a.pk)
                threading.Thread(target=th_archive).start()
                st=str(a.upload)
                name=st[st.rfind('/')+1:]
                name_file=name[:name.rfind('.')]
                st23=datetime.now().strftime("%m")
                if st23=='01': st23='января'
                elif st23=='02': st23='февраля'
                elif st23=='03': st23='марта'
                elif st23=='04': st23='апреля'
                elif st23=='05': st23='мая'
                elif st23=='06': st23='июня'
                elif st23=='07': st23='июля'
                elif st23=='08': st23='августа'
                elif st23=='09': st23='сентября'
                elif st23=='10': st23='октября'
                elif st23=='11': st23='ноября'
                elif st23=='12': st23='декабря'
                date_file=datetime.now().strftime("%d "+st23+" %Y г. %H:%M")
                return JsonResponse({'status': 'success','new_data':[name_file,date_file]})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
        else:
            form = ModelFoto()
            data['form']=form
            data['leporo']=''
            data['fots']=Foto.objects.order_by('-time')
            data['arvs']=Arkivo.objects.order_by('-time')
            return render(request, 'apliko/fotoanalizo.html', data)
    else:
        return redirect('login')
    
def vidbendoanalizo(request):
    if request.user.is_authenticated:
        global vidbendo_que
        data={}
        if request.method == 'POST':
            form = ModelVidbendo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                v=Vidbendo.objects.first()
                v.in_process='(в обработке)'
                vidbendo_que.append(v.pk)
                threading.Thread(target=th_vidbendo).start()
                name_file=str(v.upload)
                name_file=name_file[name_file.rfind('/')+1:]
                name_file=name_file[:name_file.rfind('.')]
                v.name=name_file
                st23=datetime.now().strftime("%m")
                if st23=='01': st23='января'
                elif st23=='02': st23='февраля'
                elif st23=='03': st23='марта'
                elif st23=='04': st23='апреля'
                elif st23=='05': st23='мая'
                elif st23=='06': st23='июня'
                elif st23=='07': st23='июля'
                elif st23=='08': st23='августа'
                elif st23=='09': st23='сентября'
                elif st23=='10': st23='октября'
                elif st23=='11': st23='ноября'
                elif st23=='12': st23='декабря'
                date_file=datetime.now().strftime("%d "+st23+" %Y г. %H:%M")
                v.save()
                return JsonResponse({'status': 'success','leporo':name_file,'new_data':[name_file,date_file]})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
        else:
            if is_ajax(request=request):
                try:
                    v=Vidbendo.objects.get(name=request.GET['text'])
                    arro=[]
                    arr=[]
                    st=v.st256
                    while st.find('_^_')!=-1:
                        key=st[:st.find('_^_')]
                        arr.append(key)
                        st=st[st.find('_^_')+3:]
                        st2=st[:st.find('&$_')]
                        st=st[st.find('&$_')+3:]
                        while st2.find('&^_')!=-1:
                            st3=st2[:st2.find('&^_')].split()
                            st2=st2[st2.find('&^_')+3:]
                            arr.append([float(st3[0]),float(st3[1])])
                        arro.append(arr.copy())
                        arr=[]
                    return JsonResponse({'result':arro})
                except Exception as e:
                    print(e)
            else:
                form = ModelVidbendo()
                data['form']=form
                data['leporo']=''
                data['vids']=Vidbendo.objects.order_by('-time')
                data['mess']=Mesagoj.objects.order_by('-time')
                return render(request, 'apliko/vidbendoanalizo.html', data)
    else:
        return redirect('login')
    
@gzip.gzip_page
def detect_objects_view(request):
    return StreamingHttpResponse(gen_frames(), content_type="multipart/x-mixed-replace; boundary=frame") # Возвращаем HTML шаблон для отображения результатов

def th_vidbendo():
    global vidbendo_prc
    global vidbendo_que
    if vidbendo_prc==False and len(vidbendo_que)>0:
        vidbendo_prc=True
        numb=vidbendo_que.pop(0)
        v=Vidbendo.objects.get(pk=numb)
        st256=start_video(v.upload)
        name_file=str(v.upload)
        name_file=name_file[name_file.rfind('/')+1:]
        name_file=name_file[:name_file.rfind('.')]
        convert_avi_to_mp4('apliko/static/sv_video/'+name_file+'.avi','apliko/static/sv_video/'+name_file+'.mp4')
        v.in_process=''
        v.st256=st256
        v.save()
        vidbendo_prc=False
        if len(vidbendo_que)>0:
            threading.Thread(target=th_vidbendo).start()

def th_photo():
    global photo_prc
    global photo_que
    if photo_prc==False and len(photo_que)>0:
        photo_prc=True
        numb=photo_que.pop(0)
        f=Foto.objects.get(pk=numb)
        start_photo(f.upload)
        name_file=str(f.upload)
        name_file=name_file[name_file.rfind('/')+1:]
        nm=name_file
        f.name=nm
        nm=nm[:nm.rfind('.')]
        try:
            file=open('apliko/static/sv_imgs/labels/'+nm+'.txt','r')
            st=str(file.read())
            file.close()
        except:
            st=''
        f.labels=st
        f.name_txt=nm+'.txt'
        f.save()
        photo_prc=False
        if len(photo_que)>0:
            threading.Thread(target=th_photo).start()

def th_archive():
    global archive_prc
    global archive_que
    if archive_prc==False and len(archive_que)>0:
        archive_prc=True
        numb=archive_que.pop(0)
        a=Arkivo.objects.get(pk=numb)
        st=str(a.upload)
        name=st[st.rfind('/')+1:]
        name=name[:name.rfind('.')]
        path=st[:st.rfind('/')]
        start_archive(path,name)
        create_archive('./apliko/static/sv_archive/'+name+'/','./apliko/static/sv_archive/'+name+'.zip')
        create_archive('./apliko/static/sv_archive/'+name+'/labels/','./apliko/static/sv_archive/'+name+'_labels.zip')
        a.name=name
        a.name_arch='apliko/static/sv_archive/'+name+'.zip'
        a.name_arch_lbls='apliko/static/sv_archive/'+name+'_labels.zip'
        a.save()
        archive_prc=False
        if len(photo_que)>0:
            threading.Thread(target=th_archive).start()
