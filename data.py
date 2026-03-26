import oci

def list_instances(compartment_id):
    # Use Instance Principals (NO config file, NO keys)
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

    # Create Compute client
    compute_client = oci.core.ComputeClient(config={}, signer=signer)

    # List instances in compartment
    response = compute_client.list_instances(compartment_id)

    for instance in response.data:
        print(f"Name: {instance.display_name}, Status: {instance.lifecycle_state}")

if __name__ == "__main__":
    compartment_id = "ocid1.compartment.oc1..xxxx"  
    list_instances(compartment_id)
############