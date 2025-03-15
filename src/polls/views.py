from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .services import polls_service


@require_http_methods(["POST", "GET", "DELETE"])
def handle_detail_update_delete(request, pk):
    if request.method == "GET":
        return JsonResponse(
            polls_service.retrieve_detail(pk),
            status=200,
        )

    if request.method == "POST":
        result = polls_service.modify(pk, request.POST.get("content"))
        #  TODO: implement result resolver decorator
        if result.is_error():
            return JsonResponse(
                {"error": result.error},
                status=400,
            )
        return JsonResponse(
            result.value,
            status=200,
        )
    if request.method == "DELETE":
        return JsonResponse(
            polls_service.remove(pk),
            status=204,
        )
    return JsonResponse({}, status=405)


@require_http_methods(["GET", "POST"])
def handle_list_create(request):
    if request.method == "GET":
        return JsonResponse(
            polls_service.retrieve_list(),
            status=200,
        )
    if request.method == "POST":
        return JsonResponse(
            polls_service.add(request.POST.get("content")),
            status=201,
        )
    return JsonResponse({}, status=405)


@require_http_methods(["POST"])
def handle_vote(request, pk):
    choice_id = request.POST.get("choice_id")
    return JsonResponse(
        polls_service.vote(pk, choice_id),
        status=200,
    )
