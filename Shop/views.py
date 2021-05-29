from django.shortcuts import render, redirect
from .forms import CategoryCreateForm, TagCreateForm, ProductCreateForm
from .models import Product, Category, Tag
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required


def category_list(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'Shop/category_list.html', context)


def create_category(request):
    form = CategoryCreateForm()
    context = {'form': form}
    if request.method == 'POST':
        form_data = CategoryCreateForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('Shop:list_category')
    return render(request, 'Shop/add_category.html', context)


def update_category(request, pk):
    context = {}
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found</h1>')
    instance_form = CategoryCreateForm(instance=category)
    context.update({'form': instance_form, 'instance': category})
    if request.method == "POST":
        instance = CategoryCreateForm(request.POST, instance=category)
        if instance.is_valid():
            instance.save()
            return redirect('Shop:list_category')
    return render(request, 'Shop/update_category.html', context)


def delete_category(request, pk):
    try:
        Category.objects.get(id=pk).delete()
        return redirect('Shop:list_category')
    except Category.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found</h1>')


def tag_list(request):
    context = {'tags': Tag.objects.all()}
    return render(request, 'Shop/tag_list.html', context)


def create_tag(request):
    form = TagCreateForm()
    context = {'form': form}
    if request.method == 'POST':
        form_data = TagCreateForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('Shop:tag_list')
    return render(request, 'Shop/add_tag.html', context)


def update_tag(request, pk):
    context = {}
    try:
        tags = Tag.objects.get(id=pk)
    except Tag.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found</h1>')
    instance_form = TagCreateForm(instance=tags)
    context.update({'form': instance_form, 'instance': tags})
    if request.method == 'POST':
        instance = TagCreateForm(request.POST, instance=tags)
        if instance.is_valid():
            instance.save()
            return redirect('Shop:tag_list')
    return render(request, 'Shop/update_tag.html', context)


def delete_tag(request, pk):
    try:
        Tag.objects.get(id=pk).delete()
        return redirect('Shop:tag_list')
    except Tag.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found</h1>')


def create_product(request):
    form = ProductCreateForm()
    context = {'form': form}
    if request.method == 'POST':
        form_data = ProductCreateForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('User:dashboard')
        else:
            context.update({'from': form_data})
            return render(request, 'Shop/add_product.html', context)
    return render(request, 'Shop/add_product.html', context)


def update_product(request, pk):
    context = {}
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found </h1>')
    instance_form = ProductCreateForm(instance=product)
    context.update({'form': instance_form, 'instance': product})
    if request.method == "POST":
        instance = ProductCreateForm(request.POST, request.FILES, instance=product)

        if instance.is_valid():
            instance.save()
            return redirect('User:dashboard')
        else:
            context.update({'form': instance, 'instance': product})
            return render(request, 'Shop/update_product.html', context)
    return render(request, 'Shop/update_product.html', context)


def delete_product(request, pk):
    try:
        Product.objects.get(id=pk).delete()
        return redirect('User:dashboard')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not Found</h1>')
