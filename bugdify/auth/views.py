from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bugdify.auth.repository import AuthRepository
from bugdify.auth.validators import LoginValidator
from rest_framework.decorators import action
from pydantic import ValidationError
import traceback

class AuthViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny,]
    
    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        
        try:
            data = request.data
            repo = AuthRepository()
            user_validated = LoginValidator(**data)
            user_validated = user_validated.model_dump()
            
            user_id = repo.find_user(username=user_validated['username'])
            print("user_id", user_id)
            if not user_id:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
                        
            user_data = repo.authentication_user(data_user=user_validated)
            print("user_data", user_data)
            if not user_data:
                return Response({"error": "Incorrect credentials"}, status=status.HTTP_401_UNAUTHORIZED)
                
            response_data = {
                'user_data': user_data,
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            print("Error...:", e.errors())
            traceback.print_exc()
            return Response({"validation_error": e.errors()}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print("Error...:", e)
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        