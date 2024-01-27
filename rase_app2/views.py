from django.shortcuts import render, redirect, get_object_or_404
from .form import TimeTableModelForm
from .models import TimeTable
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.http import HttpRequest, JsonResponse, Http404


from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def delete_card(request:HttpRequest):
#     if request.method == 'POST' and request.is_ajax():
#         card_id = request.POST.get('card_id')
#         card = get_object_or_404(TimeTable, id=card_id)
#         card.delete()
#         return JsonResponse({'status': 'success'}, status=200)
#     return JsonResponse({'status': 'failed'}, status=400)

@csrf_exempt
def delete_card(request: HttpRequest):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        card_id = request.POST.get('card_id')
        card = get_object_or_404(TimeTable, id=card_id)
        card.delete()
        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'status': 'failed'}, status=400)

class TimeAdminView(FormView, ListView):
    template_name = 'rase_app2/time_schedule_admin.html'
    form_class = TimeTableModelForm
    success_url = '/time-admin/'
    model = TimeTable
    paginate_by = 8
    context_object_name = 'cartes'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TimeAdminView, self).get_context_data()
    #     query = TimeTable.objects.all()
    #     timetable: TimeTable = query.order_by('-start_time').first()
    #     cart_table = timetable.start_time if timetable is not None else 0
    #     context['cart_table'] = cart_table
    #     return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TableListView(ListView):
    template_name = 'rase_app2/time_schedule_user.html'
    model = TimeTable
    context_object_name = 'cartes'
    paginate_by = 8






