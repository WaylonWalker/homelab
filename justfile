
viz:
    k8sviz -n default --kubeconfig $KUBECONFIG -t png -o kubeviz/default.png
    k8sviz -n ntfy --kubeconfig $KUBECONFIG -t png -o kubeviz/ntfy.png
    k8sviz -n minio --kubeconfig $KUBECONFIG -t png -o kubeviz/minio.png
    k8sviz -n syncthing --kubeconfig $KUBECONFIG -t png -o kubeviz/syncthing.png
    k8sviz -n photoview --kubeconfig $KUBECONFIG -t png -o kubeviz/photoview.png
    k8sviz -n shot --kubeconfig $KUBECONFIG -t png -o kubeviz/shot.png
    k8sviz -n librespeed --kubeconfig $KUBECONFIG -t png -o kubeviz/librespeed.png
    k8sviz -n matrix --kubeconfig $KUBECONFIG -t png -o kubeviz/matrix.png
    k8sviz -n code-server --kubeconfig $KUBECONFIG -t png -o kubeviz/code-server.png
    k8sviz -n jupyter --kubeconfig $KUBECONFIG -t png -o kubeviz/jupyter.png
    k8sviz -n registry --kubeconfig $KUBECONFIG -t png -o kubeviz/registry.png
    k8sviz -n installer --kubeconfig $KUBECONFIG -t png -o kubeviz/installer.png
    k8sviz -n vault --kubeconfig $KUBECONFIG -t png -o kubeviz/vault.png
    k8sviz -n jobrunner --kubeconfig $KUBECONFIG -t png -o kubeviz/jobrunner.png
    # convert image1.png image2.png image3.png -append result/result-sprite.png
