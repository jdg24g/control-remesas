from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
import requests
import json
# Create your views here.


def index(request):
    return redirect("/admin")


def handler404(request, exception):
    return render(request, "404.html", status=404)


def home(request):
    return render(request, "home/index.html")


def main_cards(request):
    return render(request, "home/components/main_cards.html")


def login(request):
    if request.method == "POST":
        cedula = request.POST.get("cedula")
        if cedula:
            cookies = {
                "username": "ZGlkaWVy",
                "password": "aG9sYQ==",
            }
            headers = {
                "Accept": "*/*",
                "Accept-Language": "es-US,es-ES;q=0.9,es-419;q=0.8,es;q=0.7",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Origin": "https://playnet.com.py",
                "Pragma": "no-cache",
                "Referer": "https://playnet.com.py/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
            }
            raw_data = '{"cedula":"%s","password":"","token":"","select":0}' % cedula
            data = raw_data.encode("utf-8")
            
            try:
                response = requests.post(
                    "https://playnet.com.py/login",
                    headers=headers,
                    cookies=cookies,
                    data=data,
                )
                response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa

                datos = response.json()  # Parsea la respuesta JSON

                # Retornar los datos como JSON
                return HttpResponse(json.dumps(datos), content_type="application/json")

            except requests.RequestException as e:
                # Manejar errores de solicitud
                return HttpResponseBadRequest("Error en la solicitud: {}".format(str(e)))

            except json.JSONDecodeError as e:
                # Manejar errores de parseo JSON
                return HttpResponseBadRequest("Error al parsear la respuesta JSON: {}".format(str(e)))

        else:
            # Si no se proporciona la cédula en el POST
            return HttpResponseBadRequest("Cédula es requerida")

    else:
        # Si el método no es POST, renderizar el formulario de login
        return redirect(home)

