from .models import Category

def categories(request):
    """
    Retrieves a list of categories with no parent category.
    
    :param request: The request object
    :return: A dictionary containing the 'categories' key with a queryset of Category objects
    """
    return {'categories': Category.objects.filter(parent=None)}