from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

@csrf_exempt
def create_contact(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            contact = Contact.objects.create(
                name=data.get("name"),
                date_of_birth=data.get("dob"),
                phone_number=data.get("phone"),
                email=data.get("email"),
                comments=data.get("comments", "")
            )

            return JsonResponse({"message": "Contact saved successfully", "id": contact.id}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
