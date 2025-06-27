import subprocess
import json
group_list=[]
def create_resource_group():
    name=input("Enter name of the resource group: ")
    location=input("Enter location (e.g., eastus, westus2,centralindia): ")
    command=f"az group create --name {name} --location {location}"
    process=subprocess.run(command,shell=True,capture_output=True, text=True)
    if(process.returncode==0):
        print("Resource group created successfully")
    else:
        print(process.stderr)
    
def list_resource_group():
    global group_list
    cmd = "az group list --output json"
    process = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    
    if process.returncode == 0:
        groups = json.loads(process.stdout)
        group_list = [group['name'] for group in groups]
        if len(group_list)==0:
            print("No existing resource groups")
        else:
            print("Resource Groups:")
            for i in range(len(group_list)):
                print(i+1,".", group_list[i])
    else:
        print("Error occurred:")
        print(process.stderr)
def create_vm():
    list_resource_group()
    if not group_list:
        print("No resorce group yet. Create one first")
        return
    index=int(input("Choose a resource group(Enter index):"));
    resource_group=group_list[index-1];
    name=input("Enter name for the virtual machine:")
    location=input("Enter location (e.g., eastus, westus2,centralindia): ")
    username=input("Enter admin username for the VM: ")
    command=f"az vm create --resource-group {resource_group} --name {name} --image Ubuntu2204 --location {location} --admin-username {username} --generate-ssh-keys --size Standard_B1s"
    process=subprocess.run(command,shell=True,capture_output=True,text=True)
    if(process.returncode==0):
        print("Virtual Machine Created Successfully!")
        print(process.stdout)
    else:
        print(process.stderr)
vm_list=[]
def list_vm():
    global vm_list
    cmd = "az vm list --output json"
    process = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    
    if process.returncode == 0:
        vms = json.loads(process.stdout)
        vm_list = [(vm['name'], vm['resourceGroup']) for vm in vms]
        if len(vm_list) == 0:
            print("No existing virtual machines")
        else:
            print("Virtual Machines:")
            for i, (name, rg) in enumerate(vm_list):
                print(f"{i + 1}. Name: {name}, Resource Group: {rg}")
    else:
        print("Error occurred:")
        print(process.stderr)
def delete_vm():
    list_vm()
    if not vm_list:
        print("No virtual machine present to be deleted")
        return
    index=int(input("Enter the index of the virtual machine to be deleted: "))
    name,resource_group=vm_list[index-1]
    command=f"az vm delete --name {name} --resource-group {resource_group} --yes"
    process=subprocess.run(command,shell=True,capture_output=True,text=True)
    if(process.returncode==0):
        print("Successfully deleted")
        print(process.stdout)
    else:
        print(process.stderr)
def delete_resource_group():
    list_resource_group()
    if not group_list:
        print("No resorce group present")
        return
    index=int(input("Enter the index of the resource to be deleted: "))
    name=group_list[index-1]
    command=f"az group delete --name {name} --yes"
    process=subprocess.run(command,shell=True,capture_output=True,text=True)
    if(process.returncode==0):
        print("Successfully deleted")
        print(process.stdout)
    else:
        print(process.stderr)
def main():
    while True:
        print("1. Create a resource group")
        print("2. List all resource groups")
        print("3. Create a virtual machine")
        print("4. List all virtual machines")
        print("5. Delete a virtual machine")
        print("6. Delete a resource group")
        print("7. Exit")
        choice=int(input("Choose an option:"))
        if(choice==1):
            create_resource_group()
        elif(choice==2):
            list_resource_group()
        elif(choice==3):
            create_vm()
        elif(choice==4):
            list_vm()
        elif(choice==5):
            delete_vm()
        elif(choice==6):
            delete_resource_group()
        elif(choice==7):
            break
        else: 
            print("Invalid Choice")
        print("\n")
if __name__ == "__main__":
    main()

        



        


