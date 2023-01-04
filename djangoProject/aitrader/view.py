from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from aitrader.services import DnnModel

@api_view(['POST'])
@parser_classes([JSONParser])
def aitrader(request):
    date = request.data
    print(f"******** 리액트에서 넘어온 문장 : {date} ******** ")
    date2 = DnnModel().create(str(date["inputs"]))
    result = date2[0]
    result1 = date2[1]
    result2 = date2[2]
    result3 = date2[3]
    result4 = date2[4]
    print(f'결과: {result} \n '
          f'{result1} \n '
          f'{result2} \n '
          f'{result3} \n '
          f'{result4}')
    return JsonResponse({'result': result,
                         'result1': result1,
                         'result2': result2,
                         'result3': result3,
                         'result4': result4})


