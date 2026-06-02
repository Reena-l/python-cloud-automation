# First: gcloud auth application-default login  (one-time setup)
# Then: pip3 install google-cloud-compute

from google.cloud import compute_v1

def list_gcp_instances(project_id, zone):
    client = compute_v1.InstancesClient()
    instances = client.list(project=project_id, zone=zone)
    
    print(f"=== GCP Instances in {zone} ===")
    for instance in instances:
        print(f"  Name: {instance.name} | Status: {instance.status}")

# Usage
list_gcp_instances("your-project-id", "asia-south1-a")