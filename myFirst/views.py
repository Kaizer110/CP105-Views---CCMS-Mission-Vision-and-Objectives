from django.http import HttpResponse

def Vision(request):
    return HttpResponse("The college of Computer Studies shall be a Center of Excellence in information Technology education.")
def Mission(request):   
    return HttpResponse("The College of Computer Studies shall produce technically competent information Technology professionals adequetely prepared in the practice of their profession supportive of national development goals and standards of global excellence.")
def Objective(request):
    return HttpResponse("1.Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions; 2.Embark in lifelong learning or research to attune to the continious innovation in the IT industry in order to adapt to the changing demands of the global market; and 3.Exhibit leadership and teamwork, and commitment to their resoective local or global organizations.")