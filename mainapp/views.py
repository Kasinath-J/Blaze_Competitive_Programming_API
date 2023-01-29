from rest_framework.decorators import api_view
from rest_framework.response import Response
from .background_tasks_file import main_background_fn
from background_task.models import Task

@api_view(['GET'])
def InitateUpdate(request):

    if len(Task.objects.all())>0:
        return Response({"message":"Only one tasks will be updated at a time"})

    main_background_fn(schedule=1)
    return Response({"message":"UPdate started successfully"})









# @api_view(['GET'])
# def initiateUpdate(request):

#     instances = BackgroundTask.objects.all()

#     if len(instances)==0:
#         instance = BackgroundTask()
#         instance.isWorking=False  
#         instance.save()

#     else:
#         instance = instances[0]


#     if instance.isWorking==True:
#         return Response({'msg':'Already updating everyday at GMT 19:30.',
#         'stop':'To stop the backgrountask updating, cancel the console for the command python manage.py process_tasks --sleep SLEEP and change the MAX ATTEMPTS to 1 in settings.py and introduce an error such as 1/0 in background_tasks_function and rerun the command python manage.py process_tasks. Now this function stops',
#         'to run again':'Change the MAX ATTEMPTS. remove the error from this function, uncheck (or convert to false ) the fisrt entry in backgroound tasks model, and reload the initiaeupload page.'
#         })

    
#     instance.isWorking=True
#     instance.save() 


#     executed_time = timezone.now()
#     started_time = executed_time
#     # started_time = executed_time.replace(minute=4,second=00)

#     background_update(schedule=started_time,repeat=5)

#     return Response({'msg':'Updating started everyday at GMT 19:30',
#         'stop':'To stop the backgrountask updating, cancel the console for the command python manage.py process_tasks --sleep SLEEP and change the MAX ATTEMPTS to 1 in settings.py and introduce an error such as 1/0 in background_tasks_function and rerun the command python manage.py process_tasks. Now this function stops',
#         'to run again':'Change the MAX ATTEMPTS. remove the error from this function, uncheck (or convert to false ) the fisrt entry in backgroound tasks model, and reload the initiaeupload page.'
#         })

   