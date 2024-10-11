import requests

# Endpoint and headers for the API request
base_url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic VGVzdFVzZXI0NjA6ejVtSCtKbWQ9W0ky"
}

# Function to get all employees
def get_all_employees():
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        try:
            employees = response.json()
            return employees
        except ValueError:
            print(f"Failed to parse response as JSON: {response.text}")
            return []
    else:
        print(f"Failed to fetch employees. Status code: {response.status_code}, Response: {response.text}")
        return []

# Function to delete employee
def delete_employee(employee_id):
    delete_url = f"{base_url}/{employee_id}"
    response = requests.delete(delete_url, headers=headers)
    
    if response.status_code == 200:
        print(f"Employee with ID {employee_id} deleted successfully.")
        return True
    elif response.status_code == 404:
        print(f"Employee with ID {employee_id} not found for deletion (404).")
        return False
    else:
        print(f"Failed to delete employee with ID {employee_id}. Status code: {response.status_code}, Response: {response.text}")
        return False

# Function to delete all employees
def delete_all_employees():
    #Get all employees
    employees = get_all_employees()
    
    if not employees:
        print("No employees found or failed to fetch employees.")
        return
    
    # Delete each employee
    for employee in employees:
        employee_id = employee.get('id')
        if employee_id:
            delete_employee(employee_id)
        else:
            print(f"Employee record without ID: {employee}")

def main():
    delete_all_employees()

main()
