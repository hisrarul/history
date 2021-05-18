## To create your Amazon EKS node role in the IAM console

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. Choose Roles, then Create role.
3. Choose EC2 from the list of Common use cases under Choose a use case, then choose Next: Permissions.
4. In the Filter policies box, enter `AmazonEKSWorkerNodePolicy`. Check the box to the left of `AmazonEKSWorkerNodePolicy`.
5. In the Filter policies box, enter AmazonEC2ContainerRegistryReadOnly. Check the box to the left of `AmazonEC2ContainerRegistryReadOnly`.
6. The `AmazonEKS_CNI_Policy` policy must be attached to either this role or to a different role that is mapped to the aws-node Kubernetes service account. We recommend assigning the policy to the role associated to the Kubernetes service account instead of assigning it to this role. For more information, see Configuring the VPC CNI plugin to use IAM roles for service accounts.
7. Choose Next: Tags.
8. (Optional) Add metadata to the role by attaching tags as key–value pairs. For more information about using tags in IAM, see Tagging IAM Entities in the IAM User Guide.
9. Choose Next: Review.
10. For Role name, enter a unique name for your role, such as NodeInstanceRole. For Role description, replace the current text with descriptive text such as Amazon EKS - Node Group Role, then choose Create role.

### Policy: *AmazonEKSWorkerNodePolicy*
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVolumes",
                "ec2:DescribeVolumesModifications",
                "ec2:DescribeVpcs",
                "eks:DescribeCluster"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}

```

### Policy: *AmazonEC2ContainerRegistryReadOnly*
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:DescribeRepositories",
                "ecr:ListImages",
                "ecr:DescribeImages",
                "ecr:BatchGetImage",
                "ecr:GetLifecyclePolicy",
                "ecr:GetLifecyclePolicyPreview",
                "ecr:ListTagsForResource",
                "ecr:DescribeImageScanFindings"
            ],
            "Resource": "*"
        }
    ]
}
```

### Policy: AmazonEKS_CNI_Policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AssignPrivateIpAddresses",
                "ec2:AttachNetworkInterface",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeInstances",
                "ec2:DescribeTags",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeInstanceTypes",
                "ec2:DetachNetworkInterface",
                "ec2:ModifyNetworkInterfaceAttribute",
                "ec2:UnassignPrivateIpAddresses"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:network-interface/*"
            ]
        }
    ]
}
```

#### Summary:
+ Tested on eks cluster 1.19

#### Ref:
+ https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html