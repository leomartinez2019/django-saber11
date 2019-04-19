from .forms import ColegioForm

def test(request):
    form = ColegioForm()
    context = {"form": form}
    return context
