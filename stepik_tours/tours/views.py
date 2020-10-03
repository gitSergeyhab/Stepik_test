from django.shortcuts import render
from django.views import View
from .utils import random_tags_hotels, fun_one_city_tours, minimax
from .data import tours, cities, list_variables, random_tag_words


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={
                'tours': tours,
                'list_variables': list_variables,
                'ran': random_tags_hotels(list(range(1, 17)), 6),  # рандомные отели в нижней части главной странице
                'cities': cities,
            }
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        city_slug = self.kwargs['departure']
        one_city_tours = fun_one_city_tours(city_slug)
        prices = minimax(one_city_tours, "price")
        nights = minimax(one_city_tours, "nights")
        return render(request, 'tours/departure.html',
                      context={
                          'tours': tours,
                          'cities': cities,
                          'list_variables': list_variables,
                          'prices': prices,
                          "days": nights,
                          'city_slug': city_slug,
                          'one_city_tours': one_city_tours,
                          'city': cities[city_slug],
                      }
                      )


class TourView(View):
    def get(self, request, *args, **kwargs):
        city_pk = self.kwargs['pk']
        tour_from_one_city = tours[city_pk]
        return render(request, 'tours/tour.html',
                      context={
                          'cities': cities,
                          'list_variables': list_variables,
                          'city_pk': city_pk,
                          'tour_from_one_city': tour_from_one_city,  # тур по номеру из хвоста request.path
                          'tags1': random_tags_hotels(random_tag_words, 3),  # рандомные тэги
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
