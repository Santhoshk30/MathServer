from django.shortcuts import render

def churn_rate(request):
    l = 0
    i = 0
    churnrate = None
    error = ""

    if request.method == "POST":
        try:
            l = float(request.POST.get('initial_cust') or 0)
            i = float(request.POST.get('present_cust') or 0)

            if l <= 0:
                error = "Initial customers must be greater than zero."
            elif i < 0:
                error = "Present customers cannot be negative."
            else:
                churnrate = ((l - i) / l) * 100

        except ValueError:
            error = "Please enter valid numbers."

    return render(
        request,
        'mathapp/math.html',
        {
            'l': l,
            'i': i,
            'churnrate': churnrate,
            'error': error
        }
    )