from django.shortcuts import render
from django.http import JsonResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@csrf_exempt
def companies(request):
    company = Company.objects.all()
    # company_json = [c.to_json() for c in company]

    if request.method == 'GET':
        company_json = [c.to_json() for c in company]
        return JsonResponse(company_json, safe=False, json_dumps_params={'indent': 5})
    if request.method == 'POST':
        data = json.loads(request.body)

        comp_name = data.get('name', '')
        comp_description = data.get('description', '')
        comp_city = data.get('city', '')
        comp_address = data.get('address', '')

        new_company = Company.objects.create(
            name=comp_name,
            description = comp_description,
            city = comp_city,
            address = comp_address,
        )

        return JsonResponse(new_company.to_json(), safe=False, json_dumps_params={'indent': 5})


@csrf_exempt
def get_company_by_id(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as error:
        return JsonResponse({"error":str(error)}, status=400)
    
    if request.method == 'GET':
        return JsonResponse(company.to_json(), json_dumps_params={'indent': 5})
    elif request.method == 'PUT':
        data = json.loads(request.body)

        new_comp_name = data.get('name', company.name)
        new_comp_description = data.get('description', company.description)
        new_comp_city = data.get('city', company.city)
        new_comp_address = data.get('address', company.address)

        company.name = new_comp_name
        company.description = new_comp_description
        company.city = new_comp_city
        company.address = new_comp_address
        
        company.save()
        # Company.save()

        return JsonResponse(company.to_json(), json_dumps_params={'indent': 5})
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})

@csrf_exempt
def company_vacancies(request, company_id):
    try:
        vacancy = Vacancy.objects.filter(company_id = company_id)
    except Vacancy.DoesNotExist as error:
        return JsonResponse({"error":str(error)}, status=400)
    

    vacancy_json = [v.to_json() for v in vacancy]
    return JsonResponse(vacancy_json,safe=False, json_dumps_params={'indent': 5})
    

@csrf_exempt
def vacancies(request):
    vacancy = Vacancy.objects.all()
    
    if request.method == 'GET':
        vacancy_json = [v.to_json() for v in vacancy]
        return JsonResponse(vacancy_json, safe=False, json_dumps_params={'indent': 5})
    if request.method == 'POST':
        data = json.loads(request.body)

        vac_name = data.get('name', '')
        vac_description = data.get('description', '')
        vac_salary = data.get('salary', '')
        vac_company_id = data.get('company_id', '')

        new_vac = Vacancy.objects.create(
            name = vac_name,
            description = vac_description,
            salary = vac_salary,
            company_id = vac_company_id,
        )

        return JsonResponse(new_vac.to_json(), safe=False, json_dumps_params={'indent': 5})


@csrf_exempt
def get_vacancy_by_id(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as error:
        return JsonResponse({"error":str(error)}, status = 400)
        
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json(), json_dumps_params={'indent': 5})

    if request.method == 'PUT':
        data = json.loads(request.body)

        vac_name = data.get('name', '')
        vac_description = data.get('description', '')
        vac_salary = data.get('salary', '')
        vac_company_id = data.get('company_id', '')

        vacancy.name = vac_name
        vacancy.description = vac_description
        vacancy.salary = vac_salary
        vacancy.company_id = vac_company_id

        vacancy.save()

        return JsonResponse(vacancy.to_json(), safe=False, json_dumps_params={'indent': 5})

    if request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})
    


@csrf_exempt
def get_top_ten_vacancies(request):
    try:
        vacancies = Vacancy.objects.all().order_by("-salary")[:10]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    vacancy = [v.to_json() for v in vacancies]

    return JsonResponse(vacancy, safe=False, json_dumps_params={'indent': 5})