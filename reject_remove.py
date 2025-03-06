import requests
import json
import time

PACS_LIST = {
    "1": {"name": "NOME_PACS1", "ae": "AE_PACS1", "ip": "192.168.0.1"},
    "2": {"name": "NOME_PACS2", "ae": "AE_PACS2", "ip": "192.168.0.2"}
}

def get_studies(server_ip, aet, study_date):
    url = f"http://{server_ip}:8080/dcm4chee-arc/aets/{aet}/rs/studies"
    query_params = {"StudyDate": study_date}
    response = requests.get(url, params=query_params)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error when searching for studies: {response.status_code} - {response.text}")
        return []

def reject_study(study):
    reject_url = study['00081190']['Value'][0] + '/reject/113001%5EDCM'
    response = requests.post(reject_url)
    
    if response.status_code == 200:
        print(f"Study {study['0020000D']['Value'][0]} successfully rejected.")
    else:
        print(f"Erro ao rejeitar study {study['0020000D']['Value'][0]}: {response.status_code} - {response.text}")

def delete_study(study):
    delete_url = study['00081190']['Value'][0]
    response = requests.delete(delete_url)
    
    if response.status_code == 204:
        print(f"Study {study['0020000D']['Value'][0]} deleted successfully.")
    else:
        print(f"Error deleting study {study['0020000D']['Value'][0]}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Select PACS:")
    for key, pacs in PACS_LIST.items():
        print(f"{key} - {pacs['name']}")
    
    pacs_choice = input("Enter the PACS number: ")
    pacs = PACS_LIST.get(pacs_choice)

    if not pacs:
        print("Invalid option.")
        exit()

    study_date = input("Enter the date of studies (YYYYMMDD or YYYYMMDD-YYYYMMDD or -YYYYMMDD): ")
    
    studies = get_studies(pacs['ip'], pacs['ae'], study_date)
    
    if not studies:
        print("No exams found for the given parameters.")
    else:
        print(f"{len(studies)} exams found.")
        for study in studies:
            reject_study(study)
            delete_study(study)
            time.sleep(0.5)  # Pause between requests to avoid overloading the server

        print("Process finished.")
