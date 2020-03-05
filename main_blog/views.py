from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('posts_list_url', permanent=True) # >>> permanent=True - чтоб redirect стал постоянным (301), по умолчанию будет временный (302)
