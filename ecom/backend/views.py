from pyexpat.errors import messages

from django.shortcuts import get_object_or_404, redirect, render

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from backend.models import ProductMainCategory,Product,ProductSubCategory

# Create your views here.





def ecom_dashboard (request):
     return render(request, 'home/home.html')


def paginate_data(request,page_num,data_list):
     items_per_page,max_pages=10,10
     paginator=Paginator(data_list,items_per_page)
     last_page_number=paginator.num_pages

     try:
          data_list=paginator.page(page_num)
     except PageNotAnInteger:
          data_list=paginator.page(1)
     except EmptyPage:
          data_list=paginator.page(last_page_number)

     current_page=data_list.number

     start_page= max(current_page - int(max_pages/2),1) 
     end_page= start_page + max_pages 

     if end_page > last_page_number:
          end_page = last_page_number + 1
          start_page= max(end_page - max_pages,1)
     paginator_list = range(start_page, end_page)
     return data_list, paginator_list, last_page_number

     

def product_main_category_list_view(request):

     product_main_categories= ProductMainCategory.objects.all().order_by('-created_at')
     page_num=request.GET.get('page',1)

     product_main_categories, paginator_list, last_page_number = paginate_data(request, page_num, product_main_categories)

     context= {
          'product_main_categories': product_main_categories,
          'paginator_list': paginator_list,
          'last_page_number': last_page_number
     }

     return render(request, 'product/product_main_category_list.html', context)


def add_product_main_category_view(request):

     if request.method == 'POST':
          main_cat_name= request.POST.get('main_cat_name')
          cat_slug= request.POST.get('cat_slug')

          description= request.POST.get('description')

          product_main_category= ProductMainCategory(
               main_cat_name=main_cat_name,
               cat_slug=cat_slug,
               created_by=request.user,
               description=description
          )
          product_main_category.save()

          messages.success(request, 'Product main category added successfully.')
          return redirect('product_main_category_list')
     return render(request, 'product/add_product_main_category.html')


def product_main_category_detail_view(request, pk):

     data = get_object_or_404(ProductMainCategory, pk=pk)

     context= {
          'data': data}
     return render(request, 'product/product_main_category_detail.html', context)



def product_list_view(request):

     products= Product.objects.all().order_by('-created_at')
     page_num=request.GET.get('page',1)

     products, paginator_list, last_page_number = paginate_data(request, page_num, products)

     context= {
          'products': products,
          'paginator_list': paginator_list,
          'last_page_number': last_page_number
     }

     return render(request, 'product/product_list.html', context)

def add_product_view(request):

     if request.method == 'POST':
          product_name= request.POST.get('product_name')
          price= request.POST.get('price')
          stock= request.POST.get('stock')
          discount_price= request.POST.get('discount_price')
          discount_percentage= request.POST.get('discount_percentage')
          description= request.POST.get('description')
          main_category_id= request.POST.get('main_category')
          sub_category_id= request.POST.get('sub_category')
          image= request.FILES.get('image')


          if not main_category_id or not sub_category_id or not price or not stock:
               messages.error(request, 'Please fill in all required fields.')
               return redirect('add_new_product')
          main_category= get_object_or_404(ProductMainCategory, id=main_category_id)
          sub_category= get_object_or_404(ProductSubCategory, id=sub_category_id)

          product= Product(
               product_name=product_name,
               price=price,
               stock=stock,
               discount_price=discount_price,
               discount_percentage=discount_percentage,
               description=description,
               main_category=main_category,
               sub_category=sub_category,
               created_by=request.user,
               #=image
          )
          product.save()

     main_categories= ProductMainCategory.objects.filter(is_active=True)
     sub_categories= ProductSubCategory.objects.filter(is_active=True)

     context ={
          'main_categories': main_categories,
          'sub_categories': sub_categories
     }
     return render(request, 'product/add_product.html', context)