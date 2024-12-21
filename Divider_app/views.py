from django.shortcuts import render
from django.http import JsonResponse
from django.template.defaultfilters import yesno


# Create your views here.
def divide(request):
    try:
        x = float(request.GET.get('x', 0))
        y = float(request.GET.get('y', 0))

        if y == 0:
            return JsonResponse({"error": "You can't divide by 0!"}, status=400)
        result = x / y
        return JsonResponse({"result": result})

    except ValueError:
        return JsonResponse({"error": "Invalid input. Please provide numbers."}, status=400)
