from kubernetes import client, config
import string
import random

# Load the default kubeconfig
config.load_kube_config()

# Define the API client for batch jobs
api_instance = client.BatchV1Api()


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


# Create a new job object
job = client.V1Job(
    api_version="batch/v1",
    kind="Job",
    metadata=client.V1ObjectMeta(name=f"myjob{get_random_string(5)}"),
    spec=client.V1JobSpec(
        ttl_seconds_after_finished=100,
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": f"myjobspod{get_random_string(5)}"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name=f"myjobrunnercontainer{get_random_string(5)}",
                        image="registry.wayl.one/dummypipe:alpine",
                        command=["python", "pipeline.py"],
                        image_pull_policy="Always",
                    ),
                ],
                restart_policy="Never",
                image_pull_secrets=[client.V1LocalObjectReference(name="regcred")],
            ),
        ),
        backoff_limit=1,
    ),
)

# Call the Kubernetes API to create the job
api_instance.create_namespaced_job(namespace="jobrunner", body=job)
