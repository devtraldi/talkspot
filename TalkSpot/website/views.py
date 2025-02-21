from django.shortcuts import render, HttpResponse
from app.models import Quote
from django.http import JsonResponse
import random


def index(request):
    return render(request, 'website/index.html')


def get_random_quote(request):
    try:
        quotes = Quote.objects.all()
        if quotes.exists():  # Verifica se há citações no banco de dados
            random_quote = random.choice(quotes)
            data = {
                'text': random_quote.text,
                'character': random_quote.character
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Nenhuma citação encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def bart_game(request):
    return render(request, 'website/bart_game.html')


def em_construcao(request):
    return render(request, 'website/em_construcao.html')
