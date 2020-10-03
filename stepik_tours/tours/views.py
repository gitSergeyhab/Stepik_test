from django.shortcuts import render
from django.views import View
from .utils import *


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={
                'tours': tours,
                'list_variables': list_variables,
                'ran': random_tegs_hotels(list(range(1, 17)), 6),  # рандомные отели в нижней части главной странице
                'cities': cities,
            }
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        rp_city = bad_re(request.path)
        one_city_tours = fun_tours_x(rp_city)  # dict туров для конкретного города
        prices = minimax(one_city_tours, "price")
        nights = minimax(one_city_tours, "nights")
        return render(request, 'tours/departure.html',
                      context={
                          'tours': tours,
                          'cities': cities,
                          'list_variables': list_variables,
                          'prices': prices,
                          "days": nights,
                          'rp_city': rp_city,  # хвост request.path
                          'one_city_tours': one_city_tours,
                          'city': cities[rp_city]  # город по хвосту request.path
                      }
                      )


class TourView(View):
    def get(self, request, *args, **kwargs):
        rp_city = int(bad_re(request.path))
        tour_from_one_city = tours[rp_city]
        return render(request, 'tours/tour.html',
                      context={
                          'cities': cities,
                          'list_variables': list_variables,
                          'rp_city': rp_city,
                          'tour_from_one_city': tour_from_one_city,  # тур по номеру из хвоста request.path
                          'tags1': random_tegs_hotels(random_tag_words, 3),  # рандомные тэги
                          'city': cities[tour_from_one_city["departure"]]  # из какого города
                      }
                      )


class KarantinView(View):
    def get(self, request):
        return render(
            request, 'tours/karantin.html', context={
                'tours': tours,
                'list_variables': list_variables,
                'cities': cities,
            }
        )
