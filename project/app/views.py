from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdForm
from .models import Ad
from django.contrib.auth.decorators import login_required


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_detail', ad.id)
    else:
        form = AdForm()
    return render(request, 'ads/ad_from.html', {'form': form})


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', ad.id)
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_from.html', {'form': form})



