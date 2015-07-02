from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {"current_date": now});

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response("hours_ahead.html", {"hour_offset": offset, "next_time": dt})




def product_table(request, num):
	listNums = [];
	num = int(num);
	i = 0;
	j = 1;
	while (i <= num):
                if (j == 1): #this means we're at the beginning of a new row because j = 1, the lowest allowed value. 
			listNums.append("lineBegin")
		val = "{x} * {y}  =  {ans}".format(x=i, y=j, ans=i*j)
		listNums.append(val); #add a new calculation to our list
		j = j + 1;
		if (j>num): #this means we're at the end of a row because j > our limit (num)
			j = 1;
			i = i + 1;
			listNums.append("lineEnd")
	info = {"table": listNums, "limit": num}
	return render_to_response("product.html", info);
       
