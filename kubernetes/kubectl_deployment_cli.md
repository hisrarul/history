## K8S DEPLOYMENT

<table>
  <thead>
    <tr>
      <th>Verb</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Create</td>
      <td>kubectl create -f deployment-definition.yaml</td>
    </tr>
    <tr>
      <td>Get</td>
      <td>Kubectl get deployment</td>
    </tr>
    <tr>
      <td rowspan="2">Update</td>
      <td>kubectl apply -f deployment-definition.yaml</td>
    </tr>
    <tr>
      <td>kubectl set image deployment/app1 nginx=nginx:1.9.1</td>
    </tr>
    <tr>
      <td rowspan="2">Status</td>
      <td>kubectl rollout status deployment/app1</td>
    </tr>
    <tr>
      <td>kubectl rollout history deployment/app1</td>
    </tr>
    <tr>
      <td>Rollback</td>
      <td>kubectl rollout undo deployment/app1</td>
    </tr>
  </tbody>
</table>
