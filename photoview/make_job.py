from kubernetes import client, config

# Load the default kubeconfig
config.load_kube_config()

# Define the API client for batch jobs
api_instance = client.BatchV1Api()

# Create a new job object
job = client.V1Job(
    api_version="batch/v1",
    kind="Job",
    metadata=client.V1ObjectMeta(name="myjob"),
    spec=client.V1JobSpec(
        ttl_seconds_after_finished=100,
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "myjob"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="myjobcontainer",
                        image="busybox",
                        command=["ls", "/"],
                    ),
                ],
                restart_policy="Never",
            ),
        ),
        backoff_limit=1,
    ),
)

# Call the Kubernetes API to create the job
api_instance.create_namespaced_job(namespace="default", body=job)
