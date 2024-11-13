from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from .models import department,Employee
from datetime import date
from django.urls import reverse
from .serializers import EmployeeSerializer
from rest_framework import status

# Create your tests here.
class EmployeeViewSetTest(APITestCase):
    #defining some function to setup some basic data for testing
    def setUp(self):
        self.department = department.objects.create( departmentName="HR")
        self.Employee = Employee.objects.create(
            EmployeeName = "jackie chan",
            Designation = "kung master",
            DateOfJoining = date(2024, 11, 13),
            departmentId = self.department,
            contact = "china",
            IsActive = True
        )
        self.client = APIClient()
    
    #defining the function to test employeee listing api/end point
    def test_employee_list(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)

    def test_employee_details(self):
        url = reverse('employee-detail',args = [self.Employee.EmployeeId])
        response = self.client.get(url)
        serializer = EmployeeSerializer(self.Employee)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)                                     